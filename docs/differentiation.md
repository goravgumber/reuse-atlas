# Ecosystem review and differentiation

Research snapshot: 2026-11-27. This is a bounded review of the three projects named in the brief, based on their public GitHub README/repository views and visible skill descriptions. It is not a full code audit. ReuseAtlas does not copy their implementations.

## Prior-Scout

[orange-clockwork/prior-scout](https://github.com/orange-clockwork/prior-scout) is a lightweight Agent Skill that searches for similar software, skills, and research methods using the host's existing search tools. Its README describes first-party-source review, feature checks, short source-linked comparisons, bounded queries, and honest handling of unknowns. It is MIT licensed and explicitly says it does not install candidates. Its core workflow already overlaps with prior-art discovery and evidence-based comparison. The README identifies host search availability as a limitation and says the tested configuration is Codex CLI; other hosts are unverified.

## Skillhub `/priorart`

[duthaho/skillhub](https://github.com/duthaho/skillhub) is a Claude Code skills collection. Its README describes `/priorart` as a locator-backed landscape that ends in one Build/Fork/Contribute/Use/Investigate verdict. It relies on native Claude research tools and frames its workflow around citations and honest source failures. The repository is MIT licensed. It provides a strong decision and evidence pattern, but the repository-level description does not promise a capability-by-capability implementation map with exact reusable components, integration points, dependency impact, and license implications.

## reuse-first

[beingaeditor/reuse-first](https://github.com/beingaeditor/reuse-first) combines a Claude Code skill with a Python MCP server, GitHub repository search, heuristic ranking, a blueprint tool, and project scaffolding. The README documents CLI/demo use, optional GitHub token, a test suite, and a scaffold that copies structure/dependency names rather than source. It is MIT licensed. This is the most tool-assisted and action-oriented of the three. Its focus is GitHub discovery and choosing/scaffolding from one best project; ReuseAtlas instead emphasizes cross-source comparison and a granular synthesis of license-compatible pieces from multiple candidates. The README itself cautions that ranking is heuristic.

## What ReuseAtlas adds

Discovery, prior-art verdicts, and scaffolding already exist in the ecosystem. ReuseAtlas should not recreate a search engine, MCP service, or project scaffold in V1. Its intended value is the bridge from “these projects are relevant” to “these exact parts can safely fit this request”: a capability matrix, implementation evidence (real paths or docs), composability/integration caveats, license-aware reuse map, and explicit remaining build gaps. The workflow stays portable and host-tool agnostic, with a lightweight optional GitHub metadata fallback only.

## Sources

- [Prior-Scout README](https://github.com/orange-clockwork/prior-scout)
- [Skillhub README](https://github.com/duthaho/skillhub)
- [reuse-first README](https://github.com/beingaeditor/reuse-first)
- [Agent Skills specification](https://agentskills.io/specification)
