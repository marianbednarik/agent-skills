---
name: leaving-pr-comments
description: Use whenever you post a comment, review, or reply on a pull request or issue on the user's behalf, on GitHub or any other code host, including explanations left before resolving or dismissing feedback.
---

Readers of a comment should know an agent wrote it, not mistake it for the user's own words. Start every comment you post on the user's behalf with this note:

```md
> [!NOTE]
> 🤖 **<model> responding on behalf of <user>**

Actual comment starts here.
```

Use the public name of the model that wrote the comment as the harness reports it, and the user's name or login. If the harness does not expose the model, name the harness instead; do not guess. Keep the attribution inside the note and the reply outside it, with no extra heading, rule, signature, or second attribution. On a host that does not render GitHub alerts, keep the same line as a plain quote.

This covers top-level comments, inline review comments, replies to reviewers and bots, and written reasons for resolving or dismissing feedback. It does not cover PR descriptions, commit messages, or text the user asked you to post verbatim without attribution.

Write the comment itself plainly: lead with the conclusion, cite the code, behavior, check, or reproduction it rests on, and keep verified facts apart from judgment. Leave out filler, canned thanks, and status narration. Before posting, check the whole comment, including quotes and attachments, for secrets and private details, and make sure the Markdown renders as intended. After posting, confirm the host returned the comment's URL, and resolve a thread only once its reply is posted.
