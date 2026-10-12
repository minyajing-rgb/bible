---
name: product-definition
description: Before product creation or improvement, inspect the full PRD, actual UI mockups, all user flows, architecture and every page/branch; deliver a complete implementation contract to the builder.
metadata:
  standard_version: 1.1.0
  canonical_commit: 6240e3fd2d62f23ab1f653ba6b70195d25739733
---
# Definition before implementation
Apply automatically to relevant product work; also read product-acceptance. Read this repository's actual code, AGENTS.md and latest approved scope. Preserve project-specific constraints; do not replace them with a generic site.

## Five mandatory inspected inputs
Create INPUT_LEDGER.md. For each input record source/version/hash, HOW inspected, constraints, approval, conflicts and INSPECTED/BLOCKED: (1) complete PRD; (2) every approved desktop/mobile UI mockup, opened as actual pixels; (3) every user flow including decisions, failure/guest/cancel/back paths; (4) information/component/service/data/auth/deployment architecture; (5) concrete page/branch/state matrix compared to real router and visible links. Filenames, summaries, a thumbnail index and code alone are not inspected UI. Missing inputs stay BLOCKED; continue safe independent work without making the owner repeat known information.

## Complete work order
Maintain PRD.md, PAGE_MATRIX.json, UI_SPEC.md, actual visual refs, USER_FLOWS.md, ARCHITECTURE.md, BUILD_REQUEST.md and TRACEABILITY.json. Every page/state row needs stable ID, route/parent, purpose, entry/exit, features, priority, required states, mockup/flow/requirement/acceptance IDs. Enumerate dynamic instances, tabs, modals, nested branches, all locales and target widths. Specify input/validation, output, copy, transition, storage, side effects, permissions, API/error behavior and undo/return. Map requirement→page/state→flow→component/API→test→evidence. No silent homepage-only scope reduction.

Put/read back the full pack in the actual builder workspace before dispatch. Respect exact tool prompt contracts and one writer per app. Verify final implementation/diff, not only a send receipt. Reuse existing recovery points; do not repeat backups instead of implementation. Preserve production, independent product identities, auth/data/domains/billing. No unauthorized publish/spend, fabricated art, contacts, metrics, model calls or successful submissions. Proposed mockups are not owner-approved; unavailable services are not done.

Gate A needs complete inspected inputs and measurable acceptance. Automatically proceed to product-acceptance after implementation; independently fix/retest before owner review. This local executable skill is COPIED, not proof of global installation or running automation. Full standard/templates: minyajing-rgb/GGC-AI-Spirituality-Research at the pinned commit, .agents/skills/ and skills/product-delivery/.
