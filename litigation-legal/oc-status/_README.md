# oc-status/ — weekly OC status-request drafts

Output from `「oc-status」工作流（加载 litigation-legal/skills/oc-status/SKILL.md）`. Per-run folders dated by day; each contains one markdown file per matter drafted, plus a `_summary.md`.

## Layout

```
oc-status/
├── _README.md                       # this file
└── [YYYY-MM-DD]/
    ├── _summary.md                  # what ran, what was skipped and why
    ├── [slug-1].md                  # one email draft per matter
    ├── [slug-2].md
    └── ...
```

When the Gmail 插件 is authenticated, Gmail drafts are also created in the user's inbox. The markdown files are the persistent record; Gmail drafts are the action layer.

## Cadence

Weekly (Monday AM) when scheduled. Register the schedule with `「oc-status」工作流（加载 litigation-legal/skills/oc-status/SKILL.md） --setup-schedule`.

Ad-hoc any time with `「oc-status」工作流（加载 litigation-legal/skills/oc-status/SKILL.md）` (default filter) or `「oc-status」工作流（加载 litigation-legal/skills/oc-status/SKILL.md） --slug=[slug]` (one matter).

## Housekeeping

Old dated folders accumulate. Nothing needs them after OC has responded and matter history is updated. Feel free to delete older than 30 days.
