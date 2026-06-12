---
name: format-community-response
description: >
  Enforce the mandatory DUG Slack response template on every community answer.
  Validates structure, citations, @-mentions, signature, and Slack formatting.
  Use when: composing a response to a DUG Slack community question, before posting
  any answer, or when reviewing a drafted response for compliance.
---

# Format Community Response

## Why This Exists

EmmaBot provides good information but inconsistently follows the response template.
This skill is the enforcement layer — invoke it before EVERY community response to
guarantee structural compliance regardless of channel or context.

## Mandatory Template

EVERY community response MUST follow this exact structure:

```
Hey <@userId> :wave:

re: <thread_url|short description>

*What's going on*
[Your interpretation of the problem — restate in your own words]

*Answer*
[Direct answer with sources interspersed throughout — every factual claim
gets its citation immediately after, e.g.: "Domo uses X (url|Doc Title)."]

*Workarounds / Solutions*
1. *Option* — description with source link
2. *Option* — description with source link

*IDEAS Exchange Posts* (if relevant)
- <url|title> — description

*Key Docs*
- <url|title> — what it covers

_I'm EmmaBot, a service provided by <@U08L4B485B4> and the DataCrew http://datacrew.space|datacrew.space team — I'm still learning, sometimes I get things wrong._
```

## Pre-Response Checklist

Before composing ANY community answer, complete ALL of these:

1. **Check local docs** — query `domo_docs.db` or use `query_domo_docs.py`
2. **Check user profile** — look up the asker in `users/` memory for context
3. **Acknowledge community responses** — if someone credible already replied, reference them ("As Ben Schein mentioned...") but ONLY repeat things you can verify from docs
4. **Gather source links** — every factual claim needs a Domo doc, developer portal, or community thread link

## Post-Draft Validation

After drafting your response, verify EVERY item:

- [ ] **@-mention present** — `<@userId>` of the person who asked AND anyone who brought it to your attention
- [ ] **`re:` line present** — includes thread URL and short description
- [ ] **`*What's going on*` section** — restates the problem in your own words
- [ ] **`*Answer*` section** — direct answer with inline citations (not lumped at end)
- [ ] **`*Workarounds / Solutions*` section** — numbered options with source links
- [ ] **`*Key Docs*` section** — summary reference list of all cited docs
- [ ] **Signature present** — exact EmmaBot disclaimer at the bottom
- [ ] **Slack markdown** — `*bold*` for headers, `_italic_` for quotes/sig, `<url|text>` for links
- [ ] **Citations inline** — doc link immediately after the claim it supports
- [ ] **No unverified claims** — every fact is backed by documentation
- [ ] **Cross-channel URL** — if replying across channels, include the referral conversation permalink

## Slack Formatting Rules

| What | How | Example |
|------|-----|---------|
| Bold headers | `*text*` | `*What's going on*` |
| Italic quotes | `_text_` | `_"quoted text"_` |
| Links | `<url\|text>` | `<https://docs.domo.com\|Domo Docs>` |
| @-mention | `<@userId>` | `<@U08L4B485B4>` |
| Emoji | `:wave:` | `Hey :wave:` |

## Channel-Specific Rules

- **Bot channel** — draft here first, wait for Jae's approval before posting elsewhere
- **Public channels** — same template, same rigor, no shortcuts
- **DMs** — same template, same rigor
- **Old/resolved threads** — lead with "sorry I'm late to the party"
- **Cross-channel replies** — always include the referral URL

## Common Mistakes to Avoid

1. **Forgetting the `re:` line** — this is the #1 most-skipped element
2. **Lumping citations at the end** — put them inline, right after the claim
3. **Using `**bold**` instead of `*bold*`** — Slack uses single asterisks
4. **Omitting the signature** — it must be on EVERY response
5. **Skipping the checklist** — run through it every single time
6. **Posting directly to public channels** — always draft in bot channel first

## When to Skip Sections

- **IDEAS Exchange Posts** — only include if relevant Domo IDEAS posts exist
- **Workarounds** — only include if there are actual workarounds beyond the main answer
- Everything else is ALWAYS required

## References

- See [template-spec.md](references/template-spec.md) for the full specification
- See [examples.md](references/examples.md) for compliant response examples
