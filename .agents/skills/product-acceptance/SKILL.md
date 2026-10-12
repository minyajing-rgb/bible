---
name: product-acceptance
description: Independently inspect every product page, state, control, flow and actual UI against the complete definition; fix and retest before owner review, then verify the actual live version after authorized release.
metadata:
  standard_version: 1.1.0
  canonical_commit: 6240e3fd2d62f23ab1f653ba6b70195d25739733
---
# Acceptance is not a build-success label
Apply automatically after relevant builds/changes and authorized releases. Read product-definition plus full PRD/mockups/flows/architecture. Record exact repo/source commit/build/URL/environment/time/browser/device/locale/width. Distinguish implementation, local/preview testing, internal acceptance, owner review, deployed and live-verified.

## Every page and function
Use ALL concrete route instances, nested branches, tabs, modals and required states as denominator; compare router and visible links, add discovered routes. Create a PAGE_REVIEW_CARD for each page: identity and requirement/flow/mockup IDs; expected vs actual; desktop AND mobile pixel comparison; content truth/translation/source/imagery; every control's real destination/side effect; every required state; keyboard/names/focus return/reduced motion/touch target/zoom; console/network/private access/metadata; evidence commit and defect IDs. PASS/FAIL/BLOCKED/NA_WITH_REASON only. Untested is BLOCKED. Report numerator/denominator, not just a big passing-test count.

Open actual renders alongside approved mockups. Inspect hierarchy, whitespace, typography, contrast, images/cropping/readability, clipping/overlap, long content and sticky bars. Captured screenshots, DOM assertions, HTTP200 and builder self-report do not certify visuals. Low-resolution previews are not restored originals. Emulated widths are not physical-device QA.

Exercise all positive/alternative/failure flows: empty/invalid/long input, loading/success/no-results/errors/timeouts/offline/retry, denied permissions/storage, guest/auth, cancel/back/refresh/deep links and repeat actions. Check actual data/network outcomes, applicable RLS/model/forms/payments with safe test data; never charge/send/mutate private records or weaken permissions without authorization. Check visitor value, architecture, privacy, complete locales, SEO and measured performance.

## Defect loop and gates
DEFECTS.json: severity, page/state/requirement, reproduction, expected/actual, screenshot/log, owner, fixing commit and same-case RETEST plus affected regressions. P0 security/data loss; P1 missing/broken required flow or critical visual evidence/misleading success; P2 nonblocking quality. Fix authorized defects then retest; untested fixes stay open. Gate B: implemented and built. Gate C INTERNALLY_ACCEPTED: 100% agreed coverage, actual pixels inspected, zero open P0/P1, P2 exceptions explicitly accepted. Otherwise NOT_READY, with exact remaining scope; never quietly waive it.

Gate D LIVE_VERIFIED only after separately authorized release: fetch real published/custom domains, redirects/body/title/asset hashes; compare tested build; rerun every live route/locale and critical flow, console/network, SEO/canonical/lang/OG and auth boundary. SPA HTTP200 can be wrong page. Absent candidate is NOT_DEPLOYED. Preview success is not live success. Rebuilt production needs new tests. Preserve old site; do not publish or repeat backups just to make a check pass.

Evidence belongs to a commit. Reuse only when diff proves page AND shared data/styles/translations unchanged; unknown mappings fail closed. Label method (browser/logic/server-render/visual) and reused version. Hand over only self-checked candidate with actual previews, coverage, defects and exact build; do not repeatedly ask owner to request review. Templates: input ledger, page review card, acceptance report at pinned canonical .agents/skills. Local COPIED is distinct from ACTIVATION_TESTED or AUTOMATION_RUNNING; no automatic global-runtime claim.
