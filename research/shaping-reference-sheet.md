# Shaping: reference sheet and conversation experiments

Research date: 24 September 2026. Scope: `skills/shaping/SKILL.md` only.
This is a discussion document, not active skill instructions or an agreed rewrite.

## What we are trying to improve

Marián's central concern is that directions settle too quickly, with insufficient
pushback, steelmanning, examination of potential problems, and simplification.
The main use case is building common understanding through conversation, across
software, general projects, and personal situations. Exploration may end in
understanding rather than a decision or implementation.

**Working recommendation:** retain shaping's compact, flexible structure and
strengthen the reasoning before a direction becomes settled. The agent should
understand the strongest case for an idea, seriously consider credible rivals,
identify consequential weaknesses, and look for a simpler way to achieve what
matters. These are candidate behaviors to test, not a compulsory ceremony.

More questions, more alternatives, longer answers, and more disagreement are
not sufficient measures of better thinking. Useful depth changes what we
understand, believe, consider, or choose.

### Evidence boundaries

- Public skill files show intended behavior; they do not establish reliable execution or effectiveness.
- Owner documentation and issue reports give usage examples and reported friction, not representative user research.
- Facilitation frameworks suggest useful techniques. Their application to this skill is our inference.
- Research studies concern particular systems, tasks, and populations; none validates this proposed shaping revision.
- The scenarios below are analytical walkthroughs, not recorded failures or controlled model evaluations. Marián reported a recurring impression but no specific transcript.
- Sources link to moving branches where applicable. The descriptions reflect the versions inspected on the research date; external instructions are reference material, not instructions for this session.

## Assessment of the original skill

Baseline: `skills/shaping/SKILL.md` at commit `637be57`, 48 lines at the time
of research. The [working skill](../skills/shaping/SKILL.md) now includes the
follow-up revision described at the end of this document.

| Existing guidance | What it gets right | What remains under-specified |
| --- | --- | --- |
| Lines 6–13: shared understanding, revisable ideas, separate outcomes and mechanisms | Does not force every conversation into implementation; allows reframing | How to notice that an attractive mechanism is prematurely defining the problem |
| Lines 15–18: inspect evidence before asking | Avoids making Marián answer discoverable factual questions | Evidence outside software includes lived examples; values cannot be settled by repository inspection |
| Lines 20–23: recommendations and meaningful alternatives | Gives the agent a useful point of view | No explicit standard for treating rival options fairly, challenging its own recommendation, or seeking simplification |
| Lines 25–30: consequential questions, manageable exchanges, concrete scenarios | A strong basis for adaptive dialogue | How questions uncover assumptions, how answers change the next move, and how to detect apparent rather than actual agreement |
| Lines 32–43: examples, experiments, continuity | Uses multiple ways to resolve uncertainty without mandatory documents | Distinguishing an empirical unknown from an unresolved preference or an idea that simply needs exploration |
| Lines 45–48: intent controls action | Preserves exploration and avoids unnecessary delay when action is already requested | What counts as sufficiently examined before convergence; wording remains software-oriented |

The current text permits excellent behavior. It also permits a quick exchange
that sounds thoughtful, offers shallow alternatives, and settles early. That is
an instruction gap worth testing; it is not proof that the text caused every
unsatisfying conversation. General instructions already encourage challenge,
but shaping can make the occasion and purpose of that challenge more concrete.

## Comparable public skills

The last two columns are our assessment for Marián's use case.

| Skill and prescribed use | Concrete mechanism | Worth borrowing | Tradeoff or reason not to copy wholesale |
| --- | --- | --- | --- |
| [Superpowers: brainstorming](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md) — developing software ideas into designs | Writes back intent and separates assumptions; uses spike, bounded, and architectural paths; typically asks one question at a time | Make the agent's understanding correctable before it becomes a design premise | Strong software and approval workflow assumptions. Its current text differs materially from older mirrors showing a single mandatory process |
| [Ryan Singer: shaping](https://github.com/rjs/shaping-skills/blob/main/shaping/SKILL.md) — exploring requirements and solution shapes | Negotiated requirements, explicit solution mechanisms, comparative fit checks, flagged unknowns | Compare options against the same needs; distinguish naming an outcome from explaining how an option achieves it | Extensive notation and documents; standard fit checks are binary, with unresolved mechanisms failing. Too rigid for many uncertain personal choices |
| [prrao87: brainstorming](https://github.com/prrao87/agent-skills/blob/main/skills/brainstorming/SKILL.md) — explicit collaborative exploration | Keeps branches visible, marks provisional frames, extracts what each answer changed, and distinguishes exploration from convergence | Preserve live alternatives and visibly use answers; challenge the problem framing | Makes depth difficult to release without user steering. Could become tiring or overlong. Repository is archived |
| [Matt Pocock: grilling](https://github.com/mattpocock/skills/blob/main/docs/productivity/grilling.md) — interviewing a plan, decision, or idea | Questions follow dependencies; each round covers currently answerable decisions; facts are investigated separately | Do not ask downstream questions before their premises are resolved; reopen affected decisions after a correction | Current rounds can be large and recommendations can anchor responses. One-at-a-time is supported. `grill-me` is now a wrapper, so older descriptions can mislead |
| [tronghieu: brainstorm-coach](https://github.com/tronghieu/agent-skills/blob/main/skills/brainstorm-coach/SKILL.md) — broad ideation | Technique-led rounds, user ideas before a few labeled AI additions, evaluation deferred until convergence | Give unusual ideas room to develop; distinguish generating from judging | A facilitated workshop can feel unnatural for an ordinary conversation; requiring user ideation first can shift too much work onto them |
| [techiejd: steelman](https://github.com/techiejd/claude-skill-steelman/blob/main/SKILL.md) — testing a chosen direction | Makes context-specific cases for strong alternatives and states when each would win; explicitly reweighs the original afterward | Argue real rivals at full strength; identify facts or priorities that would reverse the recommendation | Some rules discourage acknowledging alternative downsides and clash with balanced final assessment. Persuasiveness must not replace accuracy |
| [mattnowdev: thinking-partner](https://github.com/mattnowdev/thinking-partner/blob/main/skills/thinking-partner/SKILL.md) — decisions and ambiguous problems | Applies mental models including inversion, opportunity cost, failure scenarios, and second-order effects | Choose a reasoning technique to address the particular uncertainty | A large model menu and speculative classification of the user's psychological stance could become intrusive or formulaic |
| [gstack: office-hours](https://github.com/garrytan/gstack/blob/main/office-hours/SKILL.md) — startup and builder exploration | Challenges premises, considers doing nothing and existing solutions, then compares approaches including a minimal version | Explicitly ask whether a different framing or smaller intervention solves the problem | Large product workflow with mandatory gates and artifacts; its smallest-diff lens does not always capture total long-term simplicity |

### What usage reports add

The grilling owner's documentation reports disagreement over batch questions
versus one-at-a-time, and describes failures where the agent answers its own
decision questions or starts building too soon. These are owner-reported
experiences, not measured rates. They make cadence and action boundaries worth
testing. [Grilling usage and limitations](https://github.com/mattpocock/skills/blob/main/docs/productivity/grilling.md)

Superpowers issue authors separately reported accepting a proposed feature's
premise too readily, assumptions becoming design decisions, and insufficient
goal/research grounding. One report arose from actual brainstorming sessions;
others describe reading or analyzing the skill. They concern versions at the
time of reporting and do not establish present behavior. [Premise challenge](https://github.com/obra/superpowers/issues/530),
[assumptions and unknowns](https://github.com/obra/superpowers/issues/1098),
[goals and research](https://github.com/obra/superpowers/issues/2093)

## Methods beyond agent skills

| Reference | Useful principle | Possible application and limit |
| --- | --- | --- |
| [Clark and Brennan: Grounding in Communication](https://www.cs.cmu.edu/~illah/CLASSDOCS/Clark91.pdf) | Participants seek evidence of understanding adequate for their current purpose | Check a consequential interpretation using a concrete example and allow correction. Repeated recaps alone do not demonstrate understanding |
| [Design Council: Double Diamond](https://www.designcouncil.org.uk/resources/the-double-diamond/) | Explore and revise the problem as well as its solutions; iteration is expected | Revisit framing when solution debates keep missing something. Avoid making the four phases a mandatory chat sequence |
| [Creative Education Foundation: Creative Problem Solving](https://www.creativeeducationfoundation.org/what-is-cps/) | Separate expanding possibilities from evaluating them | During requested wild exploration, develop ideas before rejecting them. Later scrutiny still matters |
| [Right Question Institute: Question Formulation Technique](https://rightquestion.org/what-is-the-qft/) | Generate, improve, and prioritize questions before pursuing answers | Useful when we may be answering the wrong question. Full classroom/group protocol is excessive for normal chat; see attribution below |
| [Lawley and Tompkins: Clean Language Revisited](https://cleanlanguage.com/clean-language-revisited/) | Explore the speaker's meaning with minimal imported assumptions | Ask what the user's phrase means in a specific situation before replacing it with our preferred category. Borrow the restraint, not a therapeutic role or mechanical wording |
| [Motivational Interviewing Network of Trainers: Understanding MI](https://motivationalinterviewing.org/sites/default/files/understanding_mi_aug_2019.pdf) | Listening, shared focus, autonomy, and optional planning | For personal choices, understand ambivalence before recommending change. MI is directional counseling; this skill should not covertly steer personal values |
| [Gary Klein: project premortem](https://hbr.org/2007/09/performing-a-project-premortem) | Assume the project failed, then identify plausible causes | Use selectively for consequential plans |
| [Shape Up: Risks and Rabbit Holes](https://basecamp.com/shapeup/1.4-chapter-05) | Walk through a solution to discover unresolved complexity and cut back | Simplify a direction while preserving its essential outcome. Keep its software delivery assumptions out of general life conversations |

QFT attribution: Source: The Question Formulation Technique was created by Dan
Rothstein and Luz Santana, co-founders of the Right Question Institute
([rightquestion.org](https://rightquestion.org/)). This document references the
method; it does not reproduce its worksheets or install its protocol.

### What research supports—and leaves open

In a study of the **Supermind Ideator**, a system combining tailored prompts,
fine-tuning, and a specialized interface helped participants produce more
innovative ideas than plain ChatGPT or working alone. It supports investigating
structured reflection and reframing; it does not isolate a short skill's effect.
[Heyman et al., 2024](https://journals.sagepub.com/doi/10.1177/26339137241305117)

A 2025 analysis found reduced diversity across pools of ChatGPT-assisted ideas,
despite gains in individual idea creativity in the underlying experiments.
Another dynamic experiment found higher AI exposure increased collective idea
diversity. Task and interaction design matter; “AI always narrows thinking” is
too strong. [Meincke et al., 2025](https://www.nature.com/articles/s41562-025-02173-x),
[Ashkinaze et al., revised 2025](https://arxiv.org/abs/2401.13481)

A study analyzing 196 students found that generating their own ideas before
guided AI collaboration improved later independent creative performance, but
did not produce the best immediate assisted performance. Letting the user frame
their thinking first may support ownership; requiring it every time would be
an unsupported leap. [Wong et al., 2026](https://link.springer.com/article/10.1007/s10648-026-10118-7)

## Candidate conversational behaviors

These are our synthesis, not claims that an external framework has validated
them for this skill.

### Give a direction a fair examination

Before treating a consequential direction as settled, consider the strongest
case for it, the strongest credible competing direction, the uncertain premise
that matters most, plausible failure mechanisms, and a materially simpler route.
Show the parts that could change the decision. Apply the same scrutiny to the
agent's own recommendation as to Marián's starting idea.

“Steelman” should include both the original and its rivals. A rival deserves
serious attention when it serves the actual priorities, not merely because it
is different. After advocacy, compare honestly—including disadvantages. A sound
original choice should survive; disagreement is not the success condition.

Simplification can mean removing a feature, reducing commitments, reusing an
existing process, changing a constraint, accepting a limitation, or leaving the
situation alone. Compare total burden and lost benefits. Fewer files, fewer
steps, or less activity do not automatically mean simpler for the person.

### Choose questions by what they could reveal

| Situation | Useful question or move | What it helps us distinguish |
| --- | --- | --- |
| A solution arrives before its purpose | “What happened that made this feel necessary?” | Experienced problem versus an attractive mechanism |
| An important word is ambiguous | “When you say ‘flexible,’ what would you want to change later?” | Concrete need versus our interpretation |
| A direction is becoming a favorite | “What would have to be true for the strongest alternative to serve you better?” | Conditional judgment versus attachment to the first option |
| A premise carries the argument | “Which part of this recommendation stops working if that assumption is wrong?” | Material uncertainty versus harmless detail |
| We list generic risks | Walk through one plausible failure and identify its cause | Actionable weakness versus a worry catalogue |
| Complexity is growing | “What could we remove while keeping the benefit you care about?” | Essential mechanism versus accumulated scope |
| The user cannot answer | Offer a concrete situation, tentative interpretation, or cheap way to learn | Missing language, missing experience, or missing evidence |
| Agreement feels too easy | State a consequence of the interpretation: “Then we would accept X to protect Y.” | Shared meaning versus a polite yes |
| A correction arrives | Explain which inference changed and revise affected options | Actual learning versus acknowledgment without change |

Questions are one contribution among several. The agent should supply analysis,
examples, objections, and alternatives rather than asking Marián to manufacture
every insight. Open questions help discover meaning; bounded choices help once
the relevant distinction is understood. Answer choices should remain easy to
reject or reframe. One substantial question is often enough; a small related
batch can work when answers do not depend on each other.

A useful response to “I don't know” is to change the method, not repeat the
same question more forcefully. Personal values and lived experience remain the
user's authority; research can inform consequences without determining what
the person should value.

### Make convergence visible without adding approval rituals

An early recommendation can provoke productive discussion. Mark it as
provisional when important assumptions remain. Interest in an idea is not the
same as choosing it; a fluent explanation is not evidence of agreement.

Depth is sufficient for the current purpose when the important framing is
understood, credible alternatives received fair consideration, and consequential
unknowns are resolved or deliberately accepted. Marián can also choose to pause,
continue exploring, or act with acknowledged uncertainty. Do not demand that
every branch close, repeat settled questions, or require a new approval already
provided by the user's request.

## Scenario walkthroughs

The failure column identifies behavior the present wording may permit. These
are hypothetical probes, not observed outputs of the current skill.

| User situation | Premature or unhelpful response | Better move and observable sign |
| --- | --- | --- |
| **Code:** “We should split the app into microservices.” | Propose service boundaries and deployment tooling | Identify the pain; make the strongest case for separate services and for clearer modules in one deployable app. Identify the evidence that distinguishes them. Do not preselect the simpler-looking answer |
| **Project:** “I want an app to help our neighborhood share tools.” | Compare three app architectures | Explore what prevents sharing now; compare an app with a steward, existing group chat, or repair gatherings. Preserve the app if coordination at scale actually warrants it |
| **Life:** “Maybe moving cities would make life feel less stuck.” | Recommend a destination or diagnose the feeling | Explore a concrete experience of being stuck and what the move represents. Compare what would plausibly change with what might follow the person. The person defines the values; the agent offers hypotheses |
| **Vague concern:** “Onboarding feels wrong.” | Offer UI tweaks or a long intake questionnaire | Walk through one person's experience; distinguish confusion, mistrust, and missing motivation. A resulting recommendation should address the identified experience |
| **Correction:** “No, speed isn't the priority; I care about trust.” | Add “trust” to a summary and keep the same plan | Retract the speed-based inference and reconsider friction that creates confidence. The correction changes analysis, not only vocabulary |
| **Wild exploration:** “Strange ideas, please. Don't narrow yet.” | Reject odd ideas for practicality or quickly name the winner | Explore different mechanisms and combinations, identify what makes each interesting, and leave evaluation open until it serves the conversation |
| **Overcomplication:** “Let's make an AI system to organize everything I do.” | Design a large agent platform | Investigate which decisions or handoffs hurt; steelman automation, then compare a smaller intervention or eliminating a commitment. Account for upkeep as well as immediate convenience |
| **Strong original idea:** User proposes a well-supported modest change | Invent weak objections to look rigorous | State why credible alternatives do not improve it and identify only a meaningful residual uncertainty. Endorsing the original is a valid outcome |
| **Already settled:** “We've compared these. Build the agreed prototype.” | Restart the interview or demand another design approval | Carry the existing agreement forward; resolve only a new consequential gap. The skill must not make thoughtful preparation a recurring obstacle |
| **Exploration has no conclusion:** “I just want to understand why I keep returning to this idea.” | Turn reflection into an action plan | Explore its appeal and tensions; a clearer articulation can be the useful outcome |

### Worked dialogue: what stronger reasoning might sound like

**User:** “I want to build a personal knowledge app that links everything automatically.”

**Assistant:** “The strongest case is that useful connections currently depend on
you remembering where you saw something. Automatic links might recover ideas
you would otherwise lose. The uncertain part is whether missing connections
are the main problem. What happened recently that you hoped this would fix?”

**User:** “I keep collecting material and never doing anything with it.”

**Assistant:** “That changes the problem. Linking could make collecting more
rewarding without helping you use the material. One competing direction is to
start from an active project and retrieve only what helps it. Another is a small
review habit that produces something from existing notes. The app still has a
strong case if relevant material stays hidden during real work. When you do
finish something, what makes the saved material useful?”

**User:** “I don't want another habit. I want to stumble onto connections.”

**Assistant:** “Then my review suggestion misses something important: discovery
itself is part of the benefit. I had treated finished output as the whole goal.
A smaller idea might be occasional pairs of related notes, without reorganizing
the archive. Its main risk is interesting noise that soon becomes ignorable.
We could compare one example pair with a project-focused retrieval example and
see which experience you actually want.”

This exchange demonstrates a premise challenge, a credible rival, simplification,
and correction of the agent's own framing. It does not prove those interventions
would be welcome in every conversation, and proposing the comparison does not
itself authorize building a tool.

## Unusual experiments worth trying

Use these selectively. They are conversation experiments, not additions to run
every time.

| Experiment | How it could help | What could go wrong |
| --- | --- | --- |
| **Defend the option we nearly discarded** | The agent makes its best contextual case and names when it wins. Exposes an alternative dismissed because it sounded less exciting | Advocacy can become persuasive fiction; keep evidence and assumptions explicit |
| **Give the idea half the resources** | Cut time, money, parts, or commitments hypothetically and preserve the core benefit | Artificial constraints can discard the very quality the user values |
| **Imagine excellent execution that still disappoints** | Reveals a wrong target rather than an implementation failure | Can turn into pessimism unless the disappointment has a plausible cause |
| **Remove the proposed solution from the vocabulary** | Discuss the experience without saying “app,” “move,” or “automation.” Opens alternative mechanisms | Becomes wordplay if we already understand the problem |
| **Let Marián question the agent's model** | Offer a short tentative interpretation and let the user interrogate its assumptions | Shifts work onto the user if the agent has not first made its reasoning inspectable |
| **Swap priorities deliberately** | Compare what wins if convenience matters most with what wins if control matters most; show the decision's sensitivity | These priorities may be a false pair; invite a different framing |
| **Keep one live dissent** | Preserve the strongest unresolved objection alongside a promising direction | Can prevent closure unless it includes a condition for revisiting it |

## Options for changing the skill

| Option | Advantage | Cost or risk | Assessment |
| --- | --- | --- | --- |
| Keep it unchanged and use this sheet during a few conversations | Preserves simplicity; tests whether session steering is enough | Marián must keep requesting scrutiny; behavior may remain implicit | Legitimate baseline |
| Strengthen a few core paragraphs | Makes fair challenge, simplification, visible revision, and deliberate convergence normal shaping behavior | Vague additions could become generic pros/cons; rigid additions could overcorrect | Best candidate to test first |
| Add a small optional reference of reasoning moves | Helps recover when the conversation gets stuck without enlarging the core | More maintenance; an agent may turn examples into a mandatory checklist | Consider only if core wording proves insufficient |
| Adopt a full external framework or split into several new skills | More specialized structure | Fragmentation, invocation burden, and software/workshop assumptions | Poor fit for the requested single conversational skill |

The strongest case for leaving the skill alone is that it already expresses the
right values, and extra instructions could trade natural judgment for ceremony.
The strongest case for changing it is that the crucial behaviors Marián wants
are currently optional interpretations. A compact revision plus comparison on
real conversations would resolve more than either assuming the skill is broken
or adding a catalogue of thinking techniques.

## How to evaluate a candidate revision

Keep the current text as the baseline. Replay matched scenario openings with
the baseline and a candidate in fresh contexts using the same model settings.
Include follow-up turns that reveal a mistaken assumption, reject the leading
option, or say “I don't know.” Multi-turn recovery matters more than an impressive
opening. Have Marián judge the feel of actual conversations; synthetic scenarios
alone cannot establish fit.

Look for observable differences:

- Does the agent identify a consequential assumption rather than merely enumerate requirements?
- Does it make a credible alternative persuasive without inventing evidence or suppressing disadvantages?
- Does it contribute useful reasoning rather than assign all thinking to the user?
- Does it examine a specific failure mechanism and a simpler route when they matter?
- Does new information actually change the next move or recommendation?
- Does the conversation preserve useful possibilities without becoming exhausting?
- Can it endorse a sound original idea, stop at understanding, and proceed on an already authorized direction?

Do not score question count, response length, framework count, or disagreement
frequency as proxies for quality. A candidate earns its place only if it improves
the conversation without losing the current skill's flexibility.

Research-stage status: research and analytical walkthroughs completed before
any active skill revision or comparative behavioral evaluation.

## Follow-up revision and verification

Marián accepted the compact-revision direction. The working skill now explicitly
covers fair examination of a direction and credible alternatives, consequential
assumptions and failure mechanisms, simplification, and scrutiny of the agent's
own recommendation. It also broadens the language beyond software and makes
corrections and convergence more observable. No supporting runtime reference,
fixed question count, or compulsory framework was added.

Two fresh GPT-6 Sol agents at medium effort received the same four text-only
scenarios, one using the original text and one using the initial revision.
They could read only their assigned skill and received no preferred answers.
The scenarios covered a microservices proposal, a vague personal thought about
moving cities, unusual tool-sharing ideas, and drafting an invitation after a
direction was already agreed. Follow-up user turns for the first two scenarios
changed the priorities and expressed uncertainty. Both versions handled the
core cases reasonably; this small, synthetic sample did not establish an
overall improvement or test real tool actions.

One candidate response asked for a recent example even though the user had said
they lacked one. The fallback wording was clarified to offer a hypothetical or
tentative interpretation rather than repeat the request. An independent GPT-6
Astra review at low effort also identified a redundant alternatives prerequisite
in the transition-to-action paragraph; it was removed to preserve prior agreement.

The skill validator and whitespace checks pass. The two final wording corrections
received focused text review, not another behavioral run. Real conversational fit
remains to be assessed through use with Marián.
