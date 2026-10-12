---
name: product-acceptance
description: Automatically inspect all product pages/features/states/flows after implementation; independently fix and retest before owner review, and verify actual live versions after authorized release.
metadata:
  standard_version: 1.0.0
---
Read definition/full PRD/UI/flows/architecture. Record exact commit/build/environment/URL/browser/device/viewport/locale. ALL concrete pages, nested branches, tabs/modals and required states are the denominator; PASS/FAIL/BLOCKED/NA_WITH_REASON. Untested never passes.
Open actual desktop/mobile screenshots against mockups: hierarchy/layout/spacing/type/color/contrast/owned imagery/readability/controls/clipping/overlap/zoom/focus/reduced motion. DOM-only tests and builder claims are not visual review. Exercise each CTA and happy/error/empty/loading/timeout/permission/cancel/back/refresh/deeplink/storage-denied/repeat path. Check real applicable auth/RLS/data/API/model/form/payment outcomes safely; no unauthorized side effects or weakened permissions.
Defects need severity, reproduction, expected/actual, evidence, fixing commit and RETEST. Check visitor value and architecture/privacy/locale/performance/SEO. Fix/retest regressions. No internal acceptance with missing coverage/visuals, open P0/P1 or unaccepted P2.
Separate implementation, preview, internal/owner review, deployed and live-verified. After authorized release inspect actual live version/hash, routes and critical flows; preview is not live evidence. Preserve old site, no repeat backup diversion or repeated review reminders. Deliver only self-checked candidate; unfinished stays NOT_READY.
Full standard/templates: minyajing-rgb/GGC-AI-Spirituality-Research @ b50cc78567641341419c45a5759811b70f9d0456, .agents/skills/product-acceptance/SKILL.md and skills/product-delivery/.
