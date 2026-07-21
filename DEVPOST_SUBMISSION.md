# Devpost Submission Copy

## Project name
ConceptLab AI

## Tagline
Learn by Building. Teach by Sharing.

## Track
Education

## One-line description
ConceptLab AI turns any topic into an interactive learning lab, verifies
understanding through Teach Back, and lets learners publish reusable Learning
Cards that help the wider community.

## Inspiration
AI tutors can explain almost anything, but explanation is not proof of learning.
Learners understand more deeply when they experiment, retrieve knowledge, and
teach it back. Yet most AI learning sessions remain private and disappear when
the chat ends. We wanted to turn each session into both evidence of understanding
and a reusable contribution to the learning community.

## What it does
A learner enters a topic and level. GPT-5.6 generates an explanation, analogy,
key concepts, Mermaid visualization, runnable Python experiment, and quiz. After
exploring the lesson, the learner explains the concept in their own words.
GPT-5.6 evaluates accuracy, missing ideas, misconceptions, and clarity, producing
a mastery score, corrective explanation, and next challenge. The learner can
then explicitly publish the lesson and Teach Back result as a community Learning
Card for others to discover and eventually fork or improve.

## How we built it
The MVP uses FastAPI, the official OpenAI Python SDK, the Responses API,
GPT-5.6, browser JavaScript, and Mermaid. The backend exposes separate lesson,
Teach Back, publish, and community endpoints. The interface presents one
coherent learning journey rather than a general-purpose chatbot.

Codex was used throughout implementation to convert product requirements into
the working application, create and revise API routes, connect the frontend and
backend, improve structured prompts, handle failure cases, and document a
reproducible setup. The central product choices—Teach Back, explicit publishing,
community Learning Cards, and the narrow end-to-end MVP—were human decisions.

## Challenges
The main challenge was generating several educational artifacts in a single
request while keeping the result structured and renderable. We addressed this
with a strict JSON contract and defensive extraction. Another challenge was
avoiding a feature-heavy but incomplete platform, so we reduced the product to
one complete loop: Learn, Build, Test, Teach Back, and Share.

## Accomplishments
- A working topic-to-learning-lab flow
- Visual and code-based learning artifacts
- A Teach Back evaluator that checks actual explanations
- Explicit publishing into a community feed
- A clear product architecture that can grow into collaborative learning graphs

## What we learned
The strongest educational use of generative AI is not simply producing more
content. It is creating active learning experiences and making learner reasoning
visible. Teach Back changes the model from an answer engine into a formative
assessment partner. Community publishing turns transient chats into knowledge
that compounds.

## What's next
We plan to add persistent accounts, safe code execution, lesson forking,
educator rubrics, voice Teach Back, community moderation, and a learning graph
that connects prerequisites, misconceptions, and mastery evidence.

## Built with
GPT-5.6, Codex, OpenAI Responses API, OpenAI Python SDK, FastAPI, JavaScript,
HTML, CSS, Mermaid, Python

## Repository URL
[PASTE PUBLIC GITHUB URL]

## Demo URL
[PASTE DEPLOYED APP URL]

## Public YouTube demo
[PASTE YOUTUBE URL]

## Codex /feedback session ID
[PASTE SESSION ID]
