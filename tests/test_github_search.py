import unittest
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills" / "reuse-atlas" / "scripts"))
from github_search import request_results


class FakeResponse:
    headers = {"X-RateLimit-Remaining": "59"}

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def read(self):
        return b'{"total_count":1,"incomplete_results":false,"items":[{"full_name":"owner/repo","html_url":"https://github.com/owner/repo","license":null,"stargazers_count":4,"forks_count":2}]} '


class SearchTests(unittest.TestCase):
    @patch("github_search.urlopen", return_value=FakeResponse())
    def test_maps_metadata_and_keeps_missing_license_unknown(self, open_url):
        result = request_results("example", 5, 3)
        self.assertEqual(result["repositories"][0]["name"], "owner/repo")
        self.assertIsNone(result["repositories"][0]["license"])
        self.assertEqual(result["rate_limit_remaining"], "59")

    @patch("github_search.urlopen", side_effect=TimeoutError("slow"))
    def test_timeout_is_reported_as_failure(self, open_url):
        with self.assertRaisesRegex(RuntimeError, "request failed"):
            request_results("example", 5, 0.1)

    @patch.dict("os.environ", {"GITHUB_TOKEN": "temporary-test-token"})
    @patch("github_search.urlopen", return_value=FakeResponse())
    def test_optional_token_is_sent_as_bearer(self, open_url):
        request_results("example", 5, 3)
        request = open_url.call_args.args[0]
        self.assertEqual(request.get_header("Authorization"), "Bearer temporary-test-token")


if __name__ == "__main__":
    unittest.main()
