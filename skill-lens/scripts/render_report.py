#!/usr/bin/env python3
"""Render an evidence-backed Skill Lens comparison as a standalone HTML report."""
import argparse
import json
from pathlib import Path


def require_text(data, key, where):
    if not isinstance(data.get(key), str) or not data[key].strip():
        raise ValueError(f"{where}.{key} must be nonempty text")


def render(data):
    if not isinstance(data, dict):
        raise ValueError("report must be a JSON object")
    require_text(data, "title", "report")
    candidates = data.get("candidates")
    if not isinstance(candidates, list) or not candidates:
        raise ValueError("report.candidates must be a nonempty array")
    for i, candidate in enumerate(candidates):
        if not isinstance(candidate, dict):
            raise ValueError(f"candidate {i} must be an object")
        require_text(candidate, "name", f"candidate {i}")
        rows = candidate.get("rows")
        if not isinstance(rows, list) or not rows:
            raise ValueError(f"candidate {i}.rows must be a nonempty array")
        for j, row in enumerate(rows):
            if not isinstance(row, dict):
                raise ValueError(f"candidate {i}.row {j} must be an object")
            for field in ("label", "value", "evidence"):
                require_text(row, field, f"candidate {i}.row {j}")
            if row.get("kind", "neutral") not in ("positive", "caution", "neutral"):
                raise ValueError(f"candidate {i}.row {j} has an invalid kind")
    template = (Path(__file__).resolve().parent.parent / "assets" / "report-template.html").read_text(encoding="utf-8")
    marker = "__SKILL_LENS_REPORT_DATA__"
    if template.count(marker) != 1:
        raise ValueError("report template must contain exactly one data marker")
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    payload = payload.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    return template.replace(marker, payload)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8-sig"))
        html = render(data)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w" if args.overwrite else "x", encoding="utf-8", newline="\n") as output:
            output.write(html)
    except (OSError, ValueError, TypeError) as exc:
        parser.exit(2, f"Error: {exc}\n")
    print(f"Report created: {args.output.resolve()}")


if __name__ == "__main__":
    main()
