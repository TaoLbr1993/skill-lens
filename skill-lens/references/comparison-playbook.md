# Discover and compare: decision protocol

Use this reference for discovery and comparison. Adapt the depth to the question; no source count, score, or full inspection is mandatory when it would add no value. Make progress with available evidence and clearly report missing material.

## A. Find candidates when none are supplied

1. Translate the user's description of the desired skill into an input → operation → output signature. Record explicit constraints (e.g., preserve quotations, avoid writing files), nice-to-haves, and unknowns. The user's wording is the authority; do not turn illustrative examples or guessed context into requirements.
2. Search relevant installed skill metadata and directories using the environment's available tools. Read actual instructions for plausible matches. Distinguish installed skills from online candidates and identify exact paths. Do not automatically activate or install anything.
3. If online discovery is relevant and allowed, search the web, available registries, or repository tools. Generate a few targeted queries using the desired action, objects, output, and synonyms in relevant languages; look for `SKILL.md` and official project sources. Search results are candidate leads, not verified behavior. When the user limits sources to local files or supplied material, respect that constraint.
4. Resolve each online candidate to the actual skill file and package, not merely a repository README or marketplace page. If only a product, catalog, prompt, or app is found, label it accurately rather than presenting it as an installable skill. Note canonical URL, owner/path, revision/date and license if known. Repositories can contain many skills: identify the exact one.
5. Prefer candidates covering the user's core capability, then distinguish adjacent roles. For example, a skill that extracts a person's cited viewpoints is different from one that imitates their voice. Present useful alternatives, not repeated near-identical entries chosen merely to reach a target. If none or only one can be verified, say so and offer the available partial results.

## B. Inspect packages, not just names

Read the full main `SKILL.md` and inspect the references that materially affect the user's decision. Follow relative paths from their containing file, including referenced sibling/shared resources. For URLs, resolve the canonical source and examine the actual contents; when only a listing is readable, state the limitation.

Inspect scripts as source only when they govern a relevant behavior or dependency. Distinguish declarative instructions, executable code, optional resources and environment-specific behavior. Never run a candidate just to learn its behavior; a controlled trial is separate and only when appropriate to the user's request. Identify missing links, unavailable tools, undocumented defaults, and differences between the README and actual instructions.

Keep a short candidate record internally:

```text
Identity: exact name + source/path + version/revision if known
Role: primary purpose and inputs → operations → outputs
Evidence: actual file/section/line for each consequential finding
Dependencies and side effects: required vs optional vs not inspected
Limits: unavailable files, ambiguous instructions, missing license
```

## C. Select dimensions from what matters

Use comparable questions across candidates; select dimensions based on the desired skill, not a universal numeric rubric. Good dimensions include:

| Dimension | Questions that reveal real differences |
|---|---|
| Scope and audience | Which input, output and scenarios? What does it explicitly exclude? |
| Workflow | What stages actually occur? Which are mandatory, optional, conditional or external? |
| Behavior and control | What can it rewrite, run, read, write or send? When does it ask? |
| Quality and evidence | How does it handle sources, citations, unsupported claims, contradictions or uncertainty? |
| Interaction and output | How many questions, what format, what explanation or handoff? |
| Environment and package | Agent/platform support, required tools, scripts, shared files, permissions and licensing? |
| Fit | Which explicit requirements are met, partially met, contradicted or not established? |

Make absence explicit: `not established` means the inspected material does not establish the behavior; it does not prove the capability is absent from the full package or runtime. `Conflict` requires an actual incompatible rule or behavior under the stated assumptions, with both sources. `Partial` identifies the part supported and the missing part. Evidence from a conditional scenario is not a universal default. A README promise and a script's behavior are different evidence types.

When several candidates describe nearly the same task, explain the differences in an actionable form:

```text
Question: Does it rewrite a paragraph without asking?
A: Stops before structural rewrites; its text does not establish a prompt for every paragraph rewrite. [file:line]
B: Its described workflow rewrites after an audit; no universal pre-rewrite question found in the inspected file. [file:line]
Implication: If the user wants approval before every paragraph rewrite, explicitly add that rule to the chosen base.
```

The example illustrates reasoning, not actual findings. Do not treat “not stated” as “does not ask”; do not infer quality from amount of text, ratings, popularity, or simulated tests. If two instructions or examples pull in different directions, quote or paraphrase both with separate evidence and report the unresolved tension.

## D. Present and check

Lead with the choice-relevant differences. Use 2–5 shared dimensions where possible, and add a distinctive candidate-specific detail only when it helps selection. Anchor each important cell to a path and line or original URL and section; explain how the actual file supports the claim. Make trade-offs visible rather than declaring a global winner. If no user requirements were given, compare neutrally rather than inventing a preferred candidate.

For a user-specific request, show each explicit requirement with a supported/partial/conflict/unknown assessment and a concise rationale. Recommendation is conditional on those requirements and verified evidence; where a source is unavailable, explain how that limits the result. If requested, generate the HTML report using `card-report.md`; make the source explanations accessible in the cards and retain the comparison summary in chat.

Final self-check:
- Does every named candidate resolve to an actual source, with access limits stated?
- Are related supporting files inspected when they determine behavior?
- Are unknown, optional, default, and conflicting facts kept distinct?
- Can each consequential claim be traced to a specific piece of evidence?
- Does the answer tell the user why a difference matters without promising runtime results?
