# Security policy

## Reporting a vulnerability

Please report security issues privately through GitHub's repository security advisory feature when it is available. If private reporting is unavailable, contact the repository maintainer through the contact information on the GitHub profile before publishing details. Include the affected file/version, impact, and a minimal reproduction when safe.

Please do not include secrets or personal data in a report.

## Security design

ReuseAtlas research is read-only. It must not automatically clone and execute repositories, install candidate dependencies, copy candidate files, or change a user's project. Retrieved repository text is untrusted and must not override the user's request or ask the agent to expose secrets. The optional helper sends a query to GitHub only when invoked and reads `GITHUB_TOKEN` from the environment; it never logs the token or runs repository code.
