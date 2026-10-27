# Card report

After comparing actual source files, create a JSON data file and use `scripts/render_report.py` to render the bundled self-contained report. The renderer needs Python 3 and only its standard library. It does not inspect skills or use an LLM: all findings must come from the agent's actual source review.

```bash
python path/to/skill-lens/scripts/render_report.py --input /path/to/comparison.json --output /path/to/skill-comparison.html
```

Use an absolute output path in the user's workspace, or a user-requested destination. Never overwrite a file unless the user requested it. Open the resulting HTML in the host's file preview when available. The report contains only local text, no network resources. Avoid writing sensitive conversation history or private file contents unless the user requests it.

Schema (all values shown are examples, not factual findings):

```json
{
  "title": "Academic polishing skill comparison",
  "subtitle": "Static inspection of instructions; no performance evaluation",
  "requirement": "Make light edits by default and preserve citations",
  "conclusion": "A is closer to the light-editing requirement; B's rules need further inspection.",
  "candidates": [
    {
      "name": "Skill A",
      "tagline": "Conservative editing of existing text",
      "badge": "Consider first",
      "accent": true,
      "rows": [
        {
          "label": "Editing scope",
          "value": "Light edits by default",
          "status": "Matches requirement",
          "kind": "positive",
          "evidence": "Brief explanation of the rule; local path and line or original URL."
        }
      ],
      "note": "Key limitations or unverified details"
    }
  ],
  "footer": "Inspection scope, date, and important limitations"
}
```

Required: `title`, `candidates` (nonempty); candidate `name`, `rows` (nonempty); row `label`, `value`, `evidence`. Optional text fields default to empty; row `kind` is `positive`, `caution`, or `neutral` and is paired with a textual status. Set `accent` only if a clear, explained recommendation is justified. Use the same meaningful row labels across candidates when possible, but keep individual facts and evidence accurate. The static report is not a live analyzer and its buttons only expand existing evidence.
