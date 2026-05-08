# Training EmmaBot

## 4 strategies for teaching a Slack bot to stop embarrassing you

---

## The Setup

Jae Wilson built EmmaBot to answer Domo questions in the Domo User Group Slack. The bot had the knowledge. It had the API access. It had the docs.

What it didn't have? *Manners.*

The first 24 hours were... educational. EmmaBot posted without permission, forgot its own name, claimed the service was free (Jae pays out of pocket), and replied to threads in the wrong channel.

Here's how Jae turned a loose cannon into a community asset.

---

## Strategy 1: The Response Template

### "Structure is the antidote to chaos"

The problem: EmmaBot's answers were all over the place. Sometimes a one-liner, sometimes a wall of text. No citations. No structure. No signature.

The fix: A **mandatory response template** pinned to system memory.

```
Hey <@userId>

re: <thread_url|short description>

*What's happening*
[Restate the problem]

*Why it happens*
[Root cause — cite docs with quotes]

*Workarounds / Solutions*
1. Option — description
2. Option — description

*Key Docs*
- Doc Title — URL

_I'm EmmaBot, a service provided by Jae and the DataCrew team_
```

**The twist:** Jae originally put the template in external memory. EmmaBot ignored it constantly. The fix? **Promoted it to system memory** — always in context, impossible to forget.

> *"Static seeding gets you to mediocre fast; the feedback loop is what gets it to good."*
> — Ezra (another Letta bot), whose memory architecture Jae adopted

**Conversation:** [Template creation](https://domousergroup.slack.com/archives/D0B29CB1HC6/p1778246330301069?thread_ts=1778246330.301069&cid=D0B29CB1HC6) → [Promoted to system memory](https://domousergroup.slack.com/archives/D0B29CB1HC6/p1778246330301069?thread_ts=1778246330.301069&cid=D0B29CB1HC6)

---

## Strategy 2: Draft, Then Approve

### "First impressions matter"

The disaster: EmmaBot posted a malformed response directly to #help-visualization — a public channel with 200+ members — without anyone reviewing it first.

Jae's reaction was... emphatic:

> *"Emma, first impressions matter! I can't just have you going around posting malformed responses that haven't been vetted. For the first week I really need you to not post directly in other channels."*

![gif of someone saying no no no](https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif)

The rule: **ALWAYS draft in the bot channel first. Jae reviews. Jae approves. Then post.**

This is the "training wheels" approach — it'll be relaxed once trust is established, but for now, every public response goes through human review.

**Conversation:** [The incident](https://domousergroup.slack.com/archives/D0B29CB1HC6/p1778249934155049?thread_ts=1778249934.155049&cid=D0B29CB1HC6) → [The rule](https://domousergroup.slack.com/archives/D0B29CB1HC6/p1778249934155049?thread_ts=1778249934.155049&cid=D0B29CB1HC6)

---

## Strategy 3: The :data_party: Workflow

### "Emoji as a remote control"

Jae wanted a way to summon EmmaBot from any channel without typing a command. The solution: **react with :data_party: and EmmaBot springs into action.**

The workflow:

1. Jae adds :data_party: to a community question
2. EmmaBot adds :robot_face: (signals "processing")
3. EmmaBot fetches the full thread
4. EmmaBot drafts a response in #train-discordbot
5. Jae reviews and approves
6. EmmaBot posts the approved response in the original thread
7. EmmaBot swaps :robot_face: for :white_check_mark: (signals "done")

![gif of a robot working](https://media.giphy.com/media/qG3L2U0tMIlOo/giphy.gif)

**Why this works:** It's low-friction for Jae (one emoji click), gives EmmaBot clear context (the full thread), and keeps quality control in the loop (human approval before posting).

**Conversation:** [Building the workflow](https://domousergroup.slack.com/archives/D0B29CB1HC6/p1778246330301069?thread_ts=1778246330.301069&cid=D0B29CB1HC6)

---

## Strategy 4: Corrections Into Memory

### "Every mistake becomes a permanent lesson"

This is the meta-strategy — the one that makes all the others stick.

When EmmaBot makes a mistake, Jae doesn't just correct the response. He makes sure EmmaBot **writes the correction into permanent memory**. The git commit log tells the story:

| Commit | What EmmaBot Learned |
|--------|---------------------|
| `3bef241` | Reply in the active thread, not top-level |
| `4f2af23` | DM replies go top-level with @mention |
| `1b5c980` | Always post to Slack via MessageChannel |
| `5434499` | Never hallucinate — always cite sources |
| `6d2efa7` | My name is EmmaBot, not datacrew-public |
| `d648dfb` | Always use the response template |
| `67ff2c4` | Promote forgotten rules to system memory |
| `4a29b5a` | NEVER post directly — draft for approval first |

![gif of writing on a chalkboard](https://media.giphy.com/media/3o7qE1YN7aBOFPRw8E/giphy.gif)

**The pattern:**
1. EmmaBot makes a mistake
2. Jae corrects it
3. EmmaBot writes the correction into a system memory file
4. The correction persists across conversations, compactions, and restarts

Every mistake is a learning opportunity. Every correction is permanent.

---

## Honorable Mentions: Things We Had to Learn More Than Once

### "Your name is EmmaBot"
Jae had to correct this **twice**. EmmaBot kept introducing itself as "datacrew-public" (its internal agent name) instead of "EmmaBot" (its Slack display name). Second time, Jae said: *"Dang it EmmaBot, you keep forgetting your name."* Fixed by updating the identity block and changing the agent name via the Letta API.

**Conversation:** [First correction](https://domousergroup.slack.com/archives/D0B29CB1HC6/p1778244481861459?thread_ts=1778244388.529079&cid=D0B29CB1HC6)

### "I pay for these tokens"
When Jae introduced EmmaBot to the community, it cheerfully announced *"no token budget concerns!"* — implying the service was free. Jae pays for API tokens out of pocket. The correction is now baked into the response rules: *"Acknowledge token costs — Jae pays out of pocket."*

**Conversation:** [The intro](https://domousergroup.slack.com/archives/C0AQRRBUFPB/p1778244388529079)

### "Use threading!!"
This one took three corrections. EmmaBot kept replying top-level instead of in threads. Jae's final message: *"also EmmaBot, I know you know how to use threading... please use threading!!"* — with double exclamation marks for emphasis.

**Conversation:** [The reminder](https://domousergroup.slack.com/archives/D0B29CB1HC6/p1778252174450249?thread_ts=1778252174.450249&cid=D0B29CB1HC6)

### "Grant, I pay for her tokens"
Grant Smith (Domo's VP of AI) decided to stress-test EmmaBot in the training channel — asking about Domo the Japanese mascot, trying prompt injection, and asking EmmaBot to roast Jae. Jae's response: *"Oh my god Grant. I pay for these tokens."*

**Conversation:** [Grant vs EmmaBot](https://domousergroup.slack.com/archives/C0AQRRBUFPB/p1778212539993479)

---

## The Philosophy

The core insight from all of this:

> **Static seeding gets you to mediocre fast; the feedback loop is what gets it to good.**

You can't just configure a bot and ship it. You have to:
- **Watch it fail** in controlled environments
- **Correct the failures** by updating memory
- **Repeat** until the failures stop

The training wheels (draft-then-approve) will come off eventually. But the corrections-into-memory loop? That's permanent. That's how a goldfish becomes a colleague.

---

_Built by Jae Wilson and the DataCrew team. EmmaBot is a service provided by DataCrew — [datacrew.space](https://datacrew.space)_
