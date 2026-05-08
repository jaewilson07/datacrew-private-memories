---
description: Matt Wolfe's "Build A Second Brain That Remembers Everything" — chapter-chunked transcript with extracted functionality requirements for a second brain system. Source: https://www.youtube.com/watch?v=yke4fLQUsh4 (Matt Wolfe, 2026-05-06)
---

# Build A Second Brain That Remembers Everything

**Video:** https://www.youtube.com/watch?v=yke4fLQUsh4
**Channel:** Matt Wolfe
**Published:** 2026-05-06
**Duration:** 33:56

---

## Chapter 1: Intro (00:00–01:07)

So, I just built a second brain knowledge management system that has an entire wiki built in that I can chat with. It will pull any information from that second brain when I chat. It's got a built-in CRM. I can journal and it will actually look at my wiki knowledge base and try to help me with whatever issues I'm going through from my journal by looking inside of the wiki. And of course, it's got all of the content that I've saved from around the web, including YouTube videos and articles and tweets and podcasts and just tons of stuff that I've injected into this that is all accessible directly from a chat or from journaling. It is really, really sweet. And I'm going to break down how the whole thing works and how you could build one for yourself right now. Most second brain systems are just like storage, right? You dump your YouTube transcripts and your articles and your blog posts and your podcasts and just everything that you're interested in. You just dump it all into one place. Problem is, that's kind of where the information just goes to die. Unless you're like actively going back through and reviewing the notes all the time and searching through your second brain. It's just a dumping ground for information that I never go back and look at later.

---

## Chapter 2: The System Overview (01:07–06:14)

For the knowledge management system that I'm going to build, there's three core pillars:

**Pillar 1 — Wiki/Knowledge Base:** This is where I'm going to store like everything from around the web that I find. YouTube transcripts, articles, podcast transcripts, tweets, you name it, it all goes into this wiki knowledge base section.

**Pillar 2 — CRM:** So, whenever I go to events and I meet people or I jump on Zoom calls with people, I want to remember those conversations and I want to be able to recall them in the future. I also want to store details about those people. How I met them, where I met them, some of the discussions we had, any sort of contact details I got from them, email, phone number, address, whatever. They can all live in the sort of CRM element of this bigger second brain that I'm building.

**Pillar 3 — Journal:** And the third element is where this all gets pulled together, and that's the journal. When I have good days, I journal about what went right, the things I'm excited about, gratitude, that sort of stuff. When I have rough days, I journal about the things that are bothering me. My videos not performing as well as I want them to. Having a creative block and not knowing what to make videos about. I do a lot of travel and I debate a lot about whether the travel is going to be worth it or not. I journal about pretty much everything in my business.

The point is the knowledge base sits at the center and then everything else sort of connects to it. The two elements that I think are probably the most useful to the most amount of people are going to be the wiki and the journal. Maybe the CRM isn't what you need. Again, maybe it's your classroom notes, your workouts, your recipes, etc.

So, you've got your knowledge base that lives at the center of all of this. All of this knowledge is going to live in Obsidian. You're going to save articles from around the web, YouTube videos, you know, podcast notes, whatever you find around the web that's relevant to you. You're going to save it with a simple Chrome web clipper and it's going to save into your knowledge base. The CRM that I just mentioned, notes about people you met and where you met them and all that kind of stuff gets saved to the knowledge base. Meeting notes, I personally use Granola to record my meetings and take notes for me. Those meeting notes can automatically be injected into the knowledge base. And then you have journal entries. This is the layer where you actually interact with your knowledge base. You journal on what you're dealing with right now. And ideally, it's going to pull from the knowledge base that has all of this other information in it to ground the responses to your journal entries.

I imagine you save your articles, your transcripts, etc. into this system. We'll do that using a web clipper. The AI layer in the background that we're going to build then summarizes this stuff for us. So, it's not just a giant transcript. It's actually sort of the bullets and just the information we need to know. The AI is also going to extract people, companies, tools, ideas, and themes and sort of break those off. That's where it becomes kind of like a wiki. You could click into the tools page and it will list off all the tools that have been mentioned across everything that we've saved. You can click into one of the tools and it will mention where and what video that came from. And that goes for all of these little categories here. I also wanted to autolink related notes. So if I have multiple videos about how to build something with openclaw, they all get cross referenced to each other and I can click around and sort of jump into others.

I'm then going to let the journal directly into the system. So when I do write journals, it responds like chat gpt, but it's actually grounded in my own saved knowledge. So, it's not going to just respond with what chat GPT would have responded with. It's going to respond with something like, "I see you're struggling with ideas for videos. Well, you saved this video 3 days ago that says you should do this, this, and this. You also saved this video 2 weeks ago that gave this advice when you're struggling with video ideas." And it will actually pull from the knowledge that I've saved, making it more tailored to exactly what interested me and what I found valuable over time as I save stuff into the system.

It's also going to use AI to find patterns from past journal entries. So, if I'm constantly journaling on the same thing over and over again, the same struggle, it's going to see that as a pattern and take that into account when it's responding to my next journal entries. It should resurface relevant ideas when I need them. And it should also let me save notes about people and connect those people to ideas, companies, events, and conversations. So, the CRM and the meeting notes that I'm constantly saving, that should also be connected to ideas and journal entries and all of it sort of pulled together in this big mashup of like here's the conversations I've had, here's what I'm journaling on, here's what I've saved that I found interesting, and it's all in this big old soup of content that I'm saving. But that big old soup of content that I'm saving is the grounded information that is getting pulled when I write my journal entries and then get a chat response based on those journal entries.

---

## Chapter 3: OpenClaw on Hostinger (06:14–08:03)

*[Sponsor segment — Hostinger/OpenClaw deployment. Not relevant to second brain functionality.]*

---

## Chapter 4: Karpathy LLM Wiki Concept (08:03–08:27)

This whole LLM knowledge base idea came straight from Andre Karpathy. I specifically took the idea of using Obsidian as the front end. Obsidian sort of helps organize and easily read markdown files. I'm just sort of extrapolating off of this idea and adding my journaling element and my CRM element to the wiki concept that Andre laid out here.

---

## Chapter 5: Tools Needed (08:27–09:41)

In order to build this, you're going to need a couple tools:

- **Codex** (OpenAI) — IDE of choice for coding projects like this. Free to download, you get a certain amount of usage on the free ChatGPT plan.
- **Obsidian** — Giant markdown organizer and reader. Totally free at obsidian.md.
- **Obsidian Web Clipper** — Chrome extension that automatically creates a new markdown note for whatever page you're on. Automatically pulls transcripts from any YouTube video.

---

## Chapter 6: The Buildout (09:41–18:19)

Once you have Obsidian installed, create a brand new vault. The architecture from Karpathy's LLM wiki:

- **`raw/`** — Immutable source material. This is where the original stuff goes.
- **`raw/assets/`** — Optional local Obsidian attachments.
- **`wiki/`** — AI-generated markdown files that pull from the raw content.
- **`agents.md`** — Explains how the whole thing works. Operations: when the user adds a source and asks LLM to process it, it does all these things. When the user asks a question, it queries it this way. Basically tells the agent how to operate.
- **`index.md`** — Catalog of everything in the wiki.
- **`log.md`** — Whenever you make updates or changes or add things, it updates the log file.

The Obsidian Web Clipper settings: add the vault name, set default template to pull in source title, source URL, date created, and an automatic "web clip" tag. Note location set to `RAW` folder.

When processing files, the AI:
1. Reads the source from raw
2. Creates or updates wiki pages
3. Updates relevant entity, concept, topic, overview, synthesis, or comparison pages
4. Updates index.md
5. Appends an entry to log.md
6. Moves the source file from raw/ to raw/processed/

Additional refinements:
- For YouTube videos, also pull the channel name and add it to the original source page front matter
- Cross-link any wiki pages generated or updated to the original source page (no orphaned pages)

---

## Chapter 7: Querying the Wiki (18:19–19:28)

You can chat with the wiki. Ask questions like "what are some tips for motivation when I don't feel like doing the hard task today?" The AI treats it as a wiki query — checks the vault index, then answers from anything already captured and adds the reusable bit back into the wiki if it isn't there yet. The response is grounded from the wiki, but it also updated the wiki based on the question asked. It changed the index.md file, the log.md file, and created new wiki pages. As you ask questions, the wiki further and further builds out based on the questions you were asking.

---

## Chapter 8: Manually Updating the Agent (19:28–21:25)

You can manually update the agents.md file to change how the system operates. For example, adding a "processed" folder so processed files get moved out of raw. Or fixing instructions about where to add channel names (original source vs. wiki page). Or adding cross-linking rules so wiki pages link back to their source material.

---

## Chapter 9: Letting AI Update the Agent & Building Journal / CRM (21:25–24:46)

**Journal rules added to agents.md:**
- If I start a chat with "journal", add the text of that chat and subsequent conversation as a new MD file within the journal folder
- The entire conversation should be added to the markdown file
- Create an index file in the journal folder similar to the wiki index file
- Each new journal entry gets added to the index file
- Decide on a short title for the journal entry based on the contents and use the date + title as the filename
- Add the date and title to the index and link to the entry
- Log the journal entry title and short summary in log.md
- Response to journal entries should be grounded in content from the wiki
- Provide advice and insights based on what's available from the wiki as well as your own LLM knowledge
- Look in past journal entries for relevant context
- Look at CRM for relevant conversations

**CRM rules added to agents.md:**
- If I tell you I'm giving you information for the CRM, either update the person in the CRM or add the person to the CRM
- CRM files should always be a person's name
- Store: name, contact details, where/how we met, things I know about them
- Create or update the contact record
- In the CRM folder, create an index file with people listed alphabetically and a short bio
- This allows asking questions about contacts in the CRM

---

## Chapter 10: Testing the CRM (24:46–26:01)

Demo: "Add to CRM: Matthew Berman. Met at Qualcomm event in 2024. Hung out at CES in 2025. Got lunch during TechCrunch Disrupt in 2025."

The AI creates a CRM record with summary, contact details, how we met, relationship context. Then you can query: "Where did I meet Matthew Berman?" → "You met Matthew Berman at Qualcomm event in 2024. According to your CRM note..."

---

## Chapter 11: Testing the Journal (26:01–29:11)

Demo journal entry: "I have a ton of ideas for videos, but decide not to make them because I'm worried they won't get a good view count. I also talk about how I know how to write titles that will get a lot of clicks, but I also hate the whole clickbait thing..."

The AI response: "I think there are two fears braided together here. Creative integrity and channel safety. One part of you does not want to betray the video with a title that feels gross. Another part is afraid that a few underperformers will teach YouTube not to trust you. The creator notes in the vault push back on the second fear. YouTube valley of death and creator persistence both frame visible metrics as lagging indicators..."

The response is grounded in the wiki content AND uses LLM knowledge. The journal entry gets saved with the assistant's reply, synthesis, and related content.

---

## Chapter 12: Automating The Wiki Linking (29:11–30:30)

Use Codex's "Automations" feature to set up recurring tasks:
- Automation title: "Process second brain raw files"
- Runs hourly (or whatever cadence you want)
- Prompt: "If there are any unprocessed files inside the raw directory, please process them."
- Use the strongest model available (GPT 5.5, high reasoning)
- After processing, commit and push to GitHub for backup

---

## Chapter 13: Backing it all up to GitHub (30:30–31:41)

Create a private GitHub repository. Push the entire vault. Update the automation to also commit and push after processing, so backup happens every hour automatically.

---

## Chapter 14: Recap and Final Thoughts (31:41–33:56)

The whole second brain process: not only do you have a wiki of all the information you're finding and saving from around the internet, but now you have a journal and a CRM that's built on top of it as well. If you ever want to tweak how it operates, just open up Obsidian, go into agents.md and tweak the instructions. This is all just prompts at the end of the day. You just change how it gets prompted. You could even dial it in more by building in separate folders and telling it to break out people from different pieces of content and break out companies from different pieces of content and really really dial in that wiki more and more. All you really need is Obsidian and Codex. Anthropic Cowork or Claude Code also works. Over time, it just gets smarter and smarter and smarter and more and more powerful.

---

# Extracted Second Brain Functionality Requirements

Based on the video, here's what a second brain system needs:

## Core Architecture

1. **Markdown-based storage** — All content lives as markdown files, organized in folders
2. **Raw source layer** — Immutable source material (transcripts, articles, web clips) stored in `raw/`
3. **Wiki/knowledge layer** — AI-generated summaries, concepts, entities extracted from raw sources into `wiki/`
4. **Agent instructions** — `agents.md` file that defines how the AI processes, queries, and manages the system
5. **Index/catalog** — `index.md` that tracks everything in the wiki with links
6. **Activity log** — `log.md` that records all changes, additions, queries

## Input Methods

7. **Web clipping** — Browser extension to save articles, YouTube transcripts, web content directly into `raw/`
8. **YouTube transcript ingestion** — Automatically pull full transcripts from YouTube videos
9. **Manual input** — Direct chat interface to add content, CRM entries, or journal entries
10. **Meeting notes integration** — Connect to tools like Granola for automatic meeting note ingestion

## Processing Pipeline

11. **AI summarization** — Raw content gets summarized into key points, not just stored as giant transcripts
12. **Entity extraction** — Automatically extract people, companies, tools, ideas, themes from content
13. **Wiki page generation** — Create structured wiki pages for each concept/entity/tool
14. **Cross-linking** — Auto-link related notes across the wiki (Zettelkasten-style interlinking)
15. **Source linking** — Wiki pages link back to their original source material
16. **Processed file management** — Move processed files from `raw/` to `raw/processed/` to track what's been ingested

## Query & Retrieval

17. **Natural language querying** — Chat with the wiki, ask questions in plain language
18. **Grounded responses** — AI answers are grounded in the actual saved knowledge, not just LLM training data
19. **Index-based retrieval** — Check the index first, then pull relevant wiki pages
20. **Query-triggered wiki growth** — Asking questions creates new wiki pages and updates the index

## Journal System

21. **Journal entries** — Start a chat with "journal" to create a dated, titled journal entry
22. **Wiki-grounded journaling** — Journal responses pull from the wiki to give personalized advice
23. **Pattern detection** — AI finds patterns across past journal entries (recurring struggles, themes)
24. **Idea resurfacing** — When journaling about a problem, resurface relevant saved ideas/content
25. **Journal index** — Track all journal entries with date, title, summary
26. **Cross-referencing** — Journal entries link to relevant wiki pages, CRM contacts, and past journals

## CRM System

27. **Contact records** — Store person details: name, contact info, how/where you met, relationship context
28. **Contact queries** — Ask "where did I meet X?" and get grounded answers from the CRM
29. **CRM index** — Alphabetical list of contacts with short bios
30. **CRM-to-wiki linking** — Connect people to ideas, companies, events, and conversations

## Automation

31. **Scheduled processing** — Automatically process new raw files on a recurring basis (hourly, etc.)
32. **Automated backup** — Push to GitHub (or equivalent) after processing
33. **Incremental updates** — Only process new/unprocessed files, not re-process everything

## Visualization

34. **Graph view** — Visualize connections between notes, entities, and concepts
35. **Obsidian as UI** — Use Obsidian as the visibility/reading layer for the markdown vault
