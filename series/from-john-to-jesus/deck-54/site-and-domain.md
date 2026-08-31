# Text History Site and Custom Domain

## Current production Site

- Title: `From John to Jesus · Text History`
- Production URL: `https://from-john-to-jesus-text-history.joycw.chatgpt.site`
- `#card` is a browser fragment that jumps directly to the page section whose
  HTML id is `card`; it is not a separate deployment.
- Current access: owner-only custom access. Public access is available but has
  not been enabled.

## Requested custom domain

`bible.saga1001.com` was registered with the Site on 2026-08-31. It remains
pending until these DNS records are present:

| Type | Name | Value |
|---|---|---|
| CNAME | `bible` | `custom-domains.chatgpt.site.` |
| TXT | `_openai-site-verification.bible` | `openai-site-verification=MCl6xJYUBrGZBDPNGKIEiKdNlz1_9UnW4ZfEZJvk3Gg` |
| TXT | `_cf-custom-hostname.bible` | `cffae614-bf0e-4cf8-97da-a53858d8df16` |

If the DNS provider requires fully qualified names, use
`bible.saga1001.com`, `_openai-site-verification.bible.saga1001.com`, and
`_cf-custom-hostname.bible.saga1001.com` respectively.

After DNS validation succeeds, SSL is issued automatically. Making the Site
public is a separate access-policy decision and is not implied by domain
binding.
