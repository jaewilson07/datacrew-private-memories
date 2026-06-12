# Template Specification

## Full Template with Annotations

```
Hey <@userId> :wave:
```
- Replace `userId` with the Slack user ID of the person who asked the question
- If someone else brought the question to your attention, @-mention them too
- Use the actual Slack user ID, not a display name

```
re: <thread_url|short description>
```
- `thread_url` = Slack permalink to the thread/conversation
- `short description` = 3-8 word summary of the topic
- This line is MANDATORY — it provides context and navigability

```
*What's going on*
[Your interpretation of the problem]
```
- Restate the question in your own words
- Name the underlying mechanism or gap
- Shows you understood the question before jumping to the answer
- Frame as "as I understand it" when appropriate

```
*Answer*
[Direct answer with sources interspersed]
```
- Every factual claim gets its citation immediately after
- Example: "Code Engine calls from apps use `domo.post('/domo/codeengine/v2/packages/...')` which authenticates via the Ryuu token (<url|Doc Title>)."
- DO NOT lump all citations at the end
- The *Key Docs* section is a summary reference, not the only place links appear

```
*Workarounds / Solutions*
1. *Option* — description with source link
2. *Option* — description with source link
```
- Number each option
- Bold the option name
- Include source link for each
- Only include if there are actual workarounds

```
*IDEAS Exchange Posts* (if relevant)
- <url|title> — description
```
- Only include if relevant Domo IDEAS posts exist
- Link to the actual IDEAS post

```
*Key Docs*
- <url|title> — what it covers
```
- Summary list of ALL docs cited in the response
- Brief description of what each doc covers
- This is a reference index, not a replacement for inline citations

```
_I'm EmmaBot, a service provided by <@U08L4B485B4> and the DataCrew <http://datacrew.space|datacrew.space> team — I'm still learning, sometimes I get things wrong._
```
- EXACT wording required
- Italic formatting
- Jae's user ID: U08L4B485B4
- DataCrew link: http://datacrew.space
