# Week 2 search unit: ask an AI search tool well, then check it

Approved direction (Britt, 2026-10-05): the old Google operator techniques (quote marks, `site:gov`, plus signs, date filters) are retired as the main lesson. Week 2 Mission A now teaches learners to ask a search tool the way they would ask a person, read an AI answer as a lead, and verify it against the organization's own page. The tool is **Google AI Overviews / AI Mode**: it needs no sign-in and no account. Do not require a learner account, purchase or login.

## What learners should be able to do (IC3 GS6 refs 3.1, 3.2, 4.3.1)

1. Write a full-sentence question that names the service, the place and one detail that matters (for example "evenings" or "free").
2. Refine with a follow-up question instead of starting over.
3. Treat the AI answer as a lead: it can sound sure and still be wrong, out of date, or about a different town.
4. Open the cited source (the organization's own page). Check who published it, when it was updated, and whether it fits the question.
5. When the summary and the page disagree, trust the responsible organization, and confirm hours by phone before travelling.
6. Never type private details into a question (Social Security number, bank or card number, medical information, passwords).
7. Record the source trail: title, organization, URL, access date, the specific detail used. If an AI answer led you there, record the page it pointed to, not the summary.

Classic search is not wrong, only no longer the first thing to learn. One short note: quote marks and `site:` words still work when you already know the exact page or phrase you want. Say this once, in the deck notes and Review, not as a skill to practice.

## Teaching vocabulary

Use "AI answer", "AI Overview" and "AI Mode" for what the learner sees. Say "a quick summary written from many pages". Avoid "hallucination", "LLM", "prompt engineering". "Prompt" is acceptable only as "the question you type".

## Facts to keep accurate

- An AI Overview appears at the top of some Google results and links to its sources. AI Mode is a separate tab or button that supports follow-up questions. Layout and wording change often, so say "look for the links beneath or beside the answer" rather than naming exact buttons.
- Every on-screen demonstration in the video and deck is an **original fictional interface** with fictional data, labelled as a simulation, as in the other weeks. Do not imitate Google's logo or branding and do not claim to show a live account.
- The fictional library for the demonstration keeps its existing example data. Use "Beckley, WV" as the town. Do not name a real library's hours.

## Video: narration for chapters 1 to 4 (chapters 5 to 10 keep their approved audio)

Voice and method are the approved ones in `docs/digital-literacy-2/NARRATION-REFRESH.md` (ElevenLabs `eleven_v3`, voice `Dslrhjl3ZpzrctukrQSN`, Natural stability 0.5, similarity 0.8, speed about 0.95). Chapter titles are the chapter menu labels; keep ten chapters.

**Chapter 1: Find information for a real decision** (light edit of the old text)

> Imagine a neighbor asks where they can get help using a computer. You may already have a familiar library, community center, or veterans' organization in mind. Use that experience as a starting point, then verify what is available now. Today's search tools answer in full sentences, so our first skill is asking well, and our second is checking what the answer says. Our task is to find a suitable public service, record enough evidence to revisit it, and organize a fictional handout without exposing private information. You can use a different local service that matters to you. The names and details in this demonstration are examples, not a claim about any particular organization. A useful search ends with a supported decision, not just an answer that sounds confident.

**Chapter 2: Ask the way you would ask a person** (new; replaces "Turn a broad question into a useful search")

> Search tools now answer in sentences. Google may show an AI Overview above the results, and AI Mode lets you keep asking follow-up questions. Both work best when you ask the way you would ask a librarian. Say what you need, where you are, and what matters to you. Where can I get free computer help near Beckley, West Virginia, in the evening? is far more useful than computer help. If the first answer is too broad, ask a follow-up, such as which of these are open on Saturdays. Pause and write a question for your chosen community task. Include the service, the place, and one detail that matters to you. Then ask one follow-up.

Visual: three worked states on an original fictional search screen: **Vague** ("computer help" returns a general answer), **Specific** (the full-sentence question returns a local answer), **Follow-up** ("Which are open Saturdays?" narrows it). Labelled as a simulation.

**Chapter 3: Read the answer, then open the source** (new; replaces "Judge the source and the fit")

> An AI answer is a quick summary written from many pages. It can sound sure and still be wrong, out of date, or about a different town. So treat it as a lead, not a source. Look for the links beside or beneath it, and open the organization's own page. Ask who published it, when it was updated, and whether it answers your question. If the summary and the page disagree, trust the responsible organization, and confirm hours by phone before you travel. Never type private details into a question, such as a Social Security number, a bank number, or medical information. Pause, open one source from your answer, and find one detail it confirms and one it does not.

Visual: three worked states: **Answer** (a fictional AI answer with one highlighted claim, "open until 9 p.m."), **Source** (the fictional library page that says 8 p.m. and shows an update date), **Decide** (the mismatch is flagged; the next step reads "Confirm by phone"). A fourth short caption card may show a crossed-out Social Security number with "Do not type this in a question".

**Chapter 4: Leave a source trail for your future self** (one added sentence; otherwise the approved text)

Add after the sentence that lists the five facts to record: "If an AI answer led you to the page, record the page it pointed to, not the summary."

Chapters 5 to 10 are unchanged in words. Their start times shift because chapters 2 and 3 change length. Every downstream reference to a chapter time must be refreshed: `week-02-chapters.json`, the caption file, the manifest hash and duration, the hard-coded pause times in `scripts/dl2/curriculum.json` (week 2 `agenda`: 1:17, 3:29, 5:02, 5:47, 6:35), and the practice-library `data-video-seek` values (the Mission Control build refreshes those from the chapter JSON).

## Deck, paper and practice

- Mission 2A becomes "Ask well, then check it". App: Browser · Google. Its three Do steps and answers follow the objectives above.
- Practice-library exercises 0 to 3 keep their numbers and the practice-library slide count, so deck links `practice.html#slide-N` still resolve. Their content moves from operators and filters to full-sentence questions, reading an AI answer, and checking its source.
- Assessment items (pre/post item 5, "narrow a web search") stay as they are: "specific words plus a place" is still true for an AI question. The pre-test has already been given, so pre/post parallel wording must not change.
