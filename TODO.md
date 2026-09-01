# AI Bible product requirements TODO

This list tracks product requirements that should not be confused with the current public-reading experience.

## Later: account and paid membership system

- [ ] Define a member-only value proposition before adding login: saved reading progress, bookmarks, purchased downloads, private annotations, or member-only research releases.
- [ ] Keep account/transactional email separate from content marketing consent. Creating an account must not silently subscribe a reader to updates.
- [ ] Add bilingual sign-up, sign-in, password recovery, account deletion, privacy controls, and session/security handling.
- [ ] Define paid membership tiers, recurring deliverables, cancellation/refund rules, billing portal, entitlement checks, and failed-payment handling.
- [ ] Use Stripe-hosted Checkout and Customer Portal for recurring billing; do not expose secret keys in this repository.
- [ ] Add moderation and anti-spam controls before any public comment wall. Private reader reflections remain the default until then.
- [ ] Verify accessibility, mobile flows, privacy terms, tax/registration obligations, and end-to-end sandbox/live-mode separation before launch.

## Activation gate

Do not build this phase until readers need at least one persistent account feature and there is a recurring paid benefit that can be delivered reliably.
