# Customize and maintain a personal skill

Use this reference only when the user requests adaptation, feedback-based improvements, or version maintenance. Different candidates may contain useful designs, but compatible ideas do not automatically form a coherent skill.

## A. Build the adaptation plan

1. Identify the chosen base and inspect the relevant instruction, supporting files, dependency paths and current local changes. If no base is chosen, suggest a base with evidence and offer a proposed plan; do not silently modify a candidate.
2. Break down the user's desired changes into durable versus task-specific requirements. Map each requirement to the existing rule: already met, absent/unknown, partially met, or in conflict. A rule that is already present may indicate an execution problem rather than a missing instruction.
3. For each useful other candidate, identify the exact idea, procedure, or text to borrow and why it helps. Check whether it creates incompatible output, permissions, workflow, tool dependencies, or attribution/license obligations. Unknown license or unavailable source remains unknown; do not assume copied content can be redistributed.
4. Design the smallest consistent change that addresses the requirement. Show old rule or gap, proposed rule, its location, source for borrowed ideas, expected effect and a concrete trade-off. When directions conflict, present options and their consequences instead of combining them blindly. Avoid duplicate or mutually exclusive instructions.

Example plan (illustrative, not a claim about any named skill):

```text
Requirement: keep all existing references and preview before changing files.
Base A: defines concise language editing but does not specify an edit preview. [A: section]
Candidate B: demonstrates a before/after explanation. [B: section]
Proposal: add a pre-edit preview step and a rule preserving citation identifiers.
Boundary: apply to this personal copy; no claim that actual execution improves.
```

## B. Separate feedback from causes

Analyze only history the user provides or identifies as accessible and relevant. A single follow-up may be a one-off new request, not a persistent preference. Group recurring feedback only when the evidence supports grouping, cite a minimal non-sensitive excerpt or summary, and classify it as:

| Observation | Possible cause | Next action |
|---|---|---|
| Repeated preference across contexts | Durable personal preference | Propose a personal default and ask the user to resolve ambiguity if needed. |
| New requirement for this task | Task-specific constraint | Apply now; do not automatically add a permanent rule. |
| Existing instruction was ignored | Execution or trigger problem | Identify the existing rule and recommend a targeted execution/activation fix. |
| Tool or dependency fails | Environment problem | Diagnose the dependency; do not append unrelated prose rules. |
| Feedback is sparse or ambiguous | Insufficient evidence | Mark uncertain and propose a reversible option. |

Do not automatically collect, copy or store conversation history. Ask before treating an inferred durable preference as established if the user did not authorize that interpretation. Report what was and was not available.

## C. Produce a reviewable change

For advice alone, provide the proposed patch or a before/after preview in the conversation, without changing candidate files. When the user explicitly asks to create a customized version, create a new personal copy at the requested or reasonably inferred safe location and make the changes; do not impose extra confirmation after the user has already authorized creation. If the user explicitly asks to edit an existing original, honor that instruction and preserve unrelated changes.

A skill may rely on sibling resources outside its directory. Copy the complete necessary package and preserve working relative paths where feasible; otherwise list missing/shared dependencies and avoid claiming the copy is self-contained. Do not overwrite an existing personal copy. Include a concise provenance note adjacent to the copy with the original source and version/revision when known, what was changed and why, relevant candidate sources, what was copied versus adapted, date, and license/dependency uncertainties. Do not store private history by default.

Check that the updated entrypoint points to existing packaged references, keeps required metadata, does not introduce contradictory rules, and implements the user's requested boundary. Report what was created or edited, what was validated, and any unresolved gaps.

## D. Update an existing personal copy

If available, compare three inputs: the original baseline used for customization, the current personal copy, and the new upstream version. Classify changes as upstream-only, personal-only, overlapping but compatible, or overlapping and conflicting. Preview the effect; preserve originals and resolve conflicts only as authorized. If the original baseline or an entire package is missing, do not present a two-way diff as a complete three-way merge, and do not claim recovery or automatic synchronization. Maintain only the scope actually inspected and preserved.
