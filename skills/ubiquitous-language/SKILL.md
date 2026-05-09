---
name: ubiquitous-language
description: >
  Extract and refine project-specific domain language from the current conversation
  into a lean LANGUAGE.md glossary. Use when terminology, domain model,
  naming, overloaded words, or repeated project concepts need to be made explicit.
---

# Ubiquitous Language

Use this skill after enough conversation has happened for real project language to emerge. Do not force terminology work at project start.

Extract domain terms from the conversation and relevant project docs. Focus on words a future agent could misunderstand from code alone.

Be opinionated, but conversational:

- Propose canonical terms when several words compete.
- Flag overloaded or vague terms explicitly.
- Recommend better names when the current wording hides an important distinction.
- Ask targeted questions only when the ambiguity would change future implementation.

Write or update `LANGUAGE.md` in the working directory. Keep it lean:

- Terms with one-sentence definitions.
- Aliases or words to avoid when useful.
- Important relationships or lifecycle rules.
- Flagged ambiguities and their resolution.
- A short example dialogue only when it clarifies boundaries between concepts.

Skip generic programming terms unless the project gives them domain-specific meaning.

When updating an existing glossary, preserve settled language unless the conversation clearly changes it. End with a short summary of added, changed, and still-ambiguous terms.
