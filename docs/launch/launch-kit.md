# ReuseAtlas launch kit

Drafts for a future release-candidate announcement. Nothing below has been posted. Adapt each message to the venue, check current community self-promotion rules, and avoid posting identical copy across communities.

**Repository:** https://github.com/goravgumber/reuse-atlas
**Release candidates:** https://github.com/goravgumber/reuse-atlas/releases
**Real demonstration:** [Self-hosted URL shortener discovery](../examples/url-shortener-discovery.md)

## Reddit

**Suggested title:** I made an Agent Skill that researches existing projects before an AI coding agent starts building

AI coding tools are good at implementing a brief, but they can skip the first question: has someone already built most of this?

I built ReuseAtlas, a portable Agent Skill that guides an agent to search for candidate projects, inspect their sources, compare capabilities and licenses, and map what could be reused before coding. It does bounded research and does not claim to search every repository.

I tried it on a real request for a self-hosted URL shortener. It compared Kutt, Shlink, Dub, and YOURLS and recommended **ADAPT Kutt**, while calling out where the report had README-level evidence rather than verified implementation paths. The complete report is linked below.

It has been tested with Codex, with some evidence-depth cases still partial. Claude activation is unverified. I’d appreciate feedback on where the source-verification bar should be stronger.

Repo: https://github.com/goravgumber/reuse-atlas
Demo: [URL-shortener report](https://github.com/goravgumber/reuse-atlas/blob/develop/docs/examples/url-shortener-discovery.md)
Install (Codex, from the repo): `mkdir -p ~/.agents/skills && cp -R skills/reuse-atlas ~/.agents/skills/reuse-atlas`. The README has PowerShell and Claude Code paths.
Release candidates: https://github.com/goravgumber/reuse-atlas/releases

Please follow each subreddit’s self-promotion and project-posting rules; share only where this kind of post is welcome.

## Hacker News — Show HN

**Title:** Show HN: ReuseAtlas – research existing software before your coding agent builds a new one

I built ReuseAtlas because coding agents often jump from a project brief straight into implementation without checking prior art.

ReuseAtlas is a portable Agent Skill that guides bounded discovery, primary-source inspection, capability and license comparison, and an implementation reuse map. It reports what is documented versus verified and leaves implementation to the user's direction.

The real demo starts with a self-hosted URL-shortener request and compares Kutt, Shlink, Dub, and YOURLS. It recommends adapting Kutt provisionally, while recording that auth and QR implementation paths still need source verification. No candidate was integrated or tested.

Current evidence: tested with Codex; some source-depth cases remain partial. Claude activation has not been verified.

Repo: https://github.com/goravgumber/reuse-atlas
Demo: https://github.com/goravgumber/reuse-atlas/blob/develop/docs/examples/url-shortener-discovery.md
Install (Codex, from the repo): `mkdir -p ~/.agents/skills && cp -R skills/reuse-atlas ~/.agents/skills/reuse-atlas`. Windows and Claude Code steps are in the README.
Release candidates: https://github.com/goravgumber/reuse-atlas/releases

## Dev.to

**Title:** Before your coding agent builds it, ask what already exists

### The problem

An implementation can be technically sound and still duplicate mature work. A short prompt rarely tells an agent to inspect existing source, compare license terms, or explain how pieces would fit together.

### What ReuseAtlas does

ReuseAtlas is a portable Agent Skill for bounded prior-art research. It guides an agent to compare relevant projects, distinguish README claims from implementation evidence, build a capability matrix, and map reusable components and genuine gaps before coding.

### A real test

I used a request for a self-hosted URL shortener with custom domains, analytics, QR codes, authentication, and an admin dashboard. The report compared Kutt, Shlink, Dub, and YOURLS and recommended **ADAPT Kutt** provisionally. It also disclosed that several Kutt capabilities were documented but their implementation files were not verified. That limitation is part of the report, not hidden behind a confident recommendation.

### Current limits

The skill has been exercised with Codex, but some source-evidence cases remain partial. Claude activation is not verified. The explicit-invocation URL-shortener demo does not prove automatic activation.

Install and inspect the skill: https://github.com/goravgumber/reuse-atlas
Read the full demo: https://github.com/goravgumber/reuse-atlas/blob/develop/docs/examples/url-shortener-discovery.md
Release candidates: https://github.com/goravgumber/reuse-atlas/releases

For Codex, clone the repository, then run `mkdir -p ~/.agents/skills && cp -R skills/reuse-atlas ~/.agents/skills/reuse-atlas` from its root. The [README installation section](https://github.com/goravgumber/reuse-atlas#installation) includes Windows PowerShell and Claude Code instructions.

## LinkedIn

I’ve been working on a small open-source project addressing a common step missing from AI-assisted development: checking what already exists before building.

ReuseAtlas is a portable Agent Skill that guides coding agents through bounded project discovery, source inspection, feature and license comparison, and a practical reuse map before implementation.

For a real demonstration, I asked for research on a self-hosted URL shortener. ReuseAtlas compared Kutt, Shlink, Dub, and YOURLS, recommended adapting Kutt as a provisional base, and made the limits clear where source paths were not verified.

It has been tested with Codex; some evidence-depth cases remain partial. Claude activation is still unverified. I’m sharing the work for thoughtful feedback, especially on the research and verification workflow.

Project: https://github.com/goravgumber/reuse-atlas
Demo report: https://github.com/goravgumber/reuse-atlas/blob/develop/docs/examples/url-shortener-discovery.md
Install (Codex, from the repo): `mkdir -p ~/.agents/skills && cp -R skills/reuse-atlas ~/.agents/skills/reuse-atlas`. See the README for Windows and Claude Code.
Release candidates: https://github.com/goravgumber/reuse-atlas/releases

## X

Coding agents can start building before checking what already exists. ReuseAtlas is an open-source Agent Skill for bounded prior-art research, source-backed comparisons, license notes, and a reuse map before coding.

Real demo: a self-hosted URL shortener compared Kutt, Shlink, Dub, and YOURLS; provisional verdict: ADAPT Kutt. Some implementation paths still need verification. Tested with Codex; Claude activation unverified.

https://github.com/goravgumber/reuse-atlas

Install (Codex, from the repo): `mkdir -p ~/.agents/skills && cp -R skills/reuse-atlas ~/.agents/skills/reuse-atlas`. Windows and Claude Code steps: https://github.com/goravgumber/reuse-atlas#installation

## Posting checklist

- Read the target community's current promotion, link, and AI-content rules.
- Use the audience-specific draft as a starting point; do not mass-post identical text.
- Link to the release page only when a release candidate is actually available.
- Describe the research as bounded and keep source-verification limitations visible.
- Do not request artificial stars, votes, or engagement, and do not imply that any post has already been published.
