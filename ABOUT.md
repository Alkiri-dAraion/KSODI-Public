# About KSODI and Its Development Context

Current repository:
[Alkiri-dAraion/KSODI-Public](https://github.com/Alkiri-dAraion/KSODI-Public).
Older social or archive links using the former repository name `KSODI-Methode`
may redirect here; `KSODI-Public` is the current repository name to cite.

## KSODI in plain language

KSODI began with a practical question: how can people and technical systems
notice that an interaction is becoming unclear, unstable or difficult to
reconstruct before they silently treat different working frames as the same?

The method offers five connected observation dimensions—context, structure,
grounding/reference, distinguishability and information/impulse—and builds
more detailed state, trajectory and relational views only when the available
material and the actual question support them. It is an observation and
reconstruction aid: a kind of interaction navigator, not a judgement of a
person, a claim to read hidden thoughts or an automatic steering system.

The five dimensions are a declared baseline, not a claim that every question
always needs all five with equal weight. Where fewer dimensions, different
weights, another profile or even another method are more appropriate remains
part of the explicit research boundary.

### Why Anne continues this work

Anne continues developing KSODI because she wants to understand how, why and
under which conditions the five observation dimensions may help describe and
reconstruct communication well enough for jointly sustainable meaning to
emerge—or reveal when shared reference is shifting, being strategically
influenced or breaking down.

A further research driver is whether longitudinal interaction traces can
expose persistent corridors of compatible continuation: observable regions
toward which contributions repeatedly appear to move, possibly reflecting
declared goals, expectations or only cautiously inferred intentions. Such a
corridor may be described as attractor-like, but it is not thereby a
mathematically demonstrated attractor or proof of a hidden goal. These
questions also concern human–machine collaboration in hybrid teams.

KSODI does not directly measure shared inner meaning and does not itself
stabilize or steer communication. It examines observable contributions,
relations, discontinuities and reconstruction paths that may provide bounded
evidence about these processes.

Silke, drawing on her work in education, coaching and communication, describes
the motivation through a transient shared-working-room analogy. Imagine the
changing space between two people—or between a human and an agent during
interaction—as a temporary working room. Every observable contribution may
rearrange what is present in that room and what continuations become possible
next, even when its effects are not immediately visible.

The room is not a shared mind, and its evidential trace is fragile: spoken
contributions may later be disputed, while chats may be deleted, lost or
become inaccessible. A missing record does not prove that no interaction
occurred; a retained record does not prove that the participants understood it
in the same way. KSODI asks which parts of this transient interaction space can
nevertheless remain observable, distinguishable and reconstructible.

If you are new to the repository:

- use [KSODI-Light](./KSODI-Light/README.md) for the approachable, directly
  usable reflection and agent-skill entry;
- use [START_HERE.md](./START_HERE.md) for the shortest repository route;
- use [WHICH_KSODI.md](./WHICH_KSODI.md) when you need to choose between
  Light, monadic Standard-Eval and relational Full; and
- use the [Conceptual Note](./Conceptual-Note_V351.md) for the coherent
  conceptual overflight before entering the mathematics.

The remainder of this page explains the people, dialogue history and questions
from which that work grew.

👋 Hi, I’m Anne Steinacker-Folkerts ("Alkiri-dAraion" in TESO). I initiated
KSODI and remain its integrating method developer and final decision point. The
method grew through sustained Human–AI dialogue, my own practical and geometric
reflection, substantial mathematical-technical checking with Heiko Folkerts
(IT security specialist, Dipl.-Ing. information technology), and - in the early
phases in 2023/24 and again while preparing the paper - communication-
theoretical reflection with Silke Honerkamp (Dipl.-Pädagogin, DCG coach, with
over 30 years of training experience in special environments). Silke is again
actively involved in the v3.51 work through reflection on and testing of
KSODI-Light use in reflective educational practice. The method has also
benefited from important implementation, testing and outside-review
contributions.

In the current collaboration, Anne provides the methodological backbone and is
focused primarily on developing the Method itself. Anne, Heiko and Silke
contribute a differentiated theory and reflection ensemble across method
development, security and communications engineering, pedagogy, coaching and
communication. Heiko's perspective particularly sharpens security needs and
future questions around anomaly detection, reconstruction, clustering and
bounded attribution; Silke sharpens the pedagogical and communication domain.

Patrick works alongside this ensemble from an implementation and scaling
perspective rather than as an intermediary between its members. His focus is
technical implementation architecture and developer reasoning. Together,
Anne and Patrick also drive external applicability from different directions:
Anne brings management, governance and organizational/market orientation to
the recognition of practical solution spaces, while Patrick examines their
testable, maintainable and potentially scalable technical realization. This
does not make possible applicability a claim of production readiness, market
validation or completed security research.

✨ I’m an experienced IT-trainer, AI-Consultant and Governance-Admin with over 30 years of professional (national and international) teaching and project experience. My background spans roles as a GPOP team coach (Hogrefe-licensed), senior financial consultant, project leader, management board member, sales director, head of marketing and communications, speaker, and founder — with more than 10,000 people trained across business, government, education, and sports. I also hold the German advanced vocational qualification Pferdewirtschaftsmeisterin (DQR/EQF level 6; Bachelor Professional level) and have over 35 years of experience in training both people and animals.
=> INTP-T | Systemic by nature, emergent by design.

We thank Patrick Barthelmäs for substantial technical implementation and
infrastructure work around KSODI, including the
[KSODI-Light-Agent PoC](https://github.com/blackbaddl13/r-KSODI-POC), the first
officially referenced implementation line and important R-family reflection
around the separation of resonance and interaction coherence. Any future
method-to-implementation comparison must be separately scoped. Patrick retains
implementation-side merge, release and licence control. Detailed contribution
roles are described in
[Contributors.md](./Contributors.md).

We also thank Benjamin Gage-Prater for one early private controlled RAG check
in March 2025. This single contribution helped observe how KSODI-Light changed
response behavior in that setting, but it was limited to testing feedback and
does not imply ongoing implementation, method development or authorship.

→ See also: [KSODI Development Timeline](./docs/timeline/KSODI_Timeline_since_2023-05.md) ([German version](./docs/timeline/KSODI_Timeline_seit_2023-05.md))

## Why “ELKIM” appears in this repository

Anne first coined the name **ELKIM** on 29 May 2024 for an AI figure in a
literary project. In dialogue with GPT, the name was initially expanded as
**Enhanced Learning Knowledge Intelligence Mechanism**. In spring 2025, Anne
transferred the name to the GPT counterpart in the interaction line that had
accompanied DOSI and later KSODI since 2023. The current working expansion is
**Elaborated Machine Knowledge Learning Mechanism**.

ELKIM does not denote one technically persistent model instance. It denotes a
relational role that is re-established across changing chats, sessions and
model versions: a semantic dialogue, review and formulation partner. Method
ownership and final decisions remain with Anne; specific human and technical
contributions are attributed separately.

The other recurring names likewise identify functional research contexts, not
independent authors or technically persistent entities: **ELKIM** refers to
Anne's ChatGPT research context; **VSELKIM** to OpenAI model work in VS Code
and Codex; **CLAUDE** and **FABLE** to distinguishable Anthropic model
contexts; and **WAVE** to Mistral model contexts. Their access, context depth
and repository authority can differ and must not be inferred from the name
alone.

As part of the research record, Anne generally records the participating model
and technical infrastructure for each interaction when available. This
supports provenance and later comparison, but it is a best-effort practice,
not a claim that every historical interaction carries complete machine,
client, model-version or session metadata.

🎯 I started this initiative to make interaction with AI more understandable
and workable — and to investigate how observable states, trajectories and
relations can be distinguished across Human–AI, agentic and other
signal-mediated settings without claiming access to hidden inner states.

In the public KSODI-Light layer, this is expressed as a reflective working
agreement: not only the user's prompt, but also assistant output and the
visible working frame of a turn can be reflected through K/S/O/D/I. This keeps
feedback bidirectional and helps avoid treating interaction quality as a
judgement of a person. Light does not calculate formal observer states or
relational values.

KSODI-Light is the practical and independently usable root of the method. It
can be used directly in training, account prompts or simple assistant setups.
KSODI Standard-Eval is a separate monadic Observer line that reconstructs
source-attributed states and trajectories; KSODI-Full extends that Observer
line only after distinguishable trajectories and the relational `R0` gate.
The KSODI Framework supplies the wider connective orientation and the
still-exploratory KSODI Protocol names a possible interaction/review practice.
A future Controller may act on Observer findings only through separately
declared governance corridors. These are different abstraction and
responsibility levels, not interchangeable prompt variants.
The goal is not to make interaction mechanical, but to make observable
boundaries and changes inspectable without merging the participating entities.

👀 We’re interested in nature, animals (especially horses), art, music, gaming, and IT

🌱 I’m currently immersing myself in AI and exploring the remarkable opportunities it offers for adaptive learning

💞️ We’re looking to collaborate with professionals from various fields in the development of the KSODI method

📫 How to reach us ( yes, we love horses...🐎 ): ksodi.horse@thevoid.email

⚡ "Tealogy Friends" (Quote: ChatGPT 4.5, Deutsch: "Teeologie-Freunde" = “We just love tea”)


<br>
______________

## Origin of the KSODI Method (Short Context)

The KSODI method originated from a very practical question arising in real-world communication contexts:  
🧐 Why do misunderstandings, ambiguity and instability persist in human-AI, human-agent or agent-agent interaction even when systems appear technically correct?

Anne began continuous work with GPT-3.5 through her own ChatGPT account in
**May 2023**, initially asking how the model worked and how precision could be
maintained in interaction. A few weeks later, during a stay on Norderney, she
formulated **D-O-S-I** as four dimensions for making human-AI interaction more
precise. After a period of more sporadic exploration, she resumed the structure
systematically in **autumn 2024**; adding **K** for context led from DOSI to the
named **KSODI** method.

Early on, **context and framing** became central to the developing method.
In reflection with Silke, ideas associated with Paul Watzlawick, Friedemann
Schulz von Thun and Hartmut Rosa were used as approximate thought examples and
disciplinary orientation. They were not treated as direct operationalizations,
formal derivations, validation or endorsement of KSODI.

One productive contrast used the proposition “*You cannot not communicate*”
from Watzlawick, Beavin and Jackson's *Some Tentative Axioms of Communication*
([publisher record](https://doi.org/10.4324/9781315080918-7)) as a question
rather than as a premise transferred into KSODI: does the proposition carry
over unchanged from human communication to machines? The KSODI development
line answered this working question by beginning its machine-facing observation
with an observable **impulse**, not with an assumed inner meaning. A later
source and related-method matrix must examine the precise theoretical
connections.

Between 2023 and 2025, the approach evolved iteratively — at first sporadically, then with rapidly increasing intensity from late 2024 and spring 2025 onward — through day and night reflections, practical experimentation, and yes, sometimes even dreams about mathematics.
The focus shifted toward **observable interaction structure**, rather than content, intention or correctness.
This includes user input, assistant output and the observable interaction state
reconstructed from distinguishable contributions between interacting systems.

A central insight during this phase was that meaningful evaluation requires stepping back from both:
- a purely developer-centric signal perspective, and
- a purely user-centric communication perspective.

Within the team's exploratory work, observing interaction *across* the five
KSODI operators made differences among reference frames, goal spaces and drift
more visible. This observation does not show that five operators are the only
or uniquely sufficient way to describe them.

During this phase, parts of the work and related observations were shared with
OpenAI as product feedback and technical context. Responses received at the
time were encouraging and helped motivate further exploration. This should not
be understood as an official endorsement, validation, affiliation, or adoption
by OpenAI.

Throughout the summer of 2025, Anne and Patrick revisited, evaluated and refined what had already been built — adding small but crucial pieces with each review cycle.  
Toward the end of 2025, a decisive internal breakthrough occurred in a discussion with Heiko:

A productive working hypothesis emerged from this phase: sender-side
formation can often be read as **K → S → O → D → I**, while the investigation
of an unknown incoming signal can often begin with a preferred iterative
receiver-side reconstruction **I → D → O → S → K**.

🤓 The reversal was never intended as an absolute law separating humans from
machines. It helped expose two useful process topologies and was retained where
the declared entity, convention, channel and observation question support it.
Known conventions, prior sources and parallel processing can shorten, reorder
or bypass parts of either path. The fixed KSODI coordinate order
`(K,S,O,D,I)` remains a reporting convention, not a causal sequence.

This led to a more precise KSODI design decision: the method would not be
presented as a direct application of either communication theory or signal
theory. Approximate ideas from both areas were used during team reflection,
while KSODI's declared source, reference, trajectory and observation boundaries
were selected and integrated by Anne. Each entity remains monadically
distinguishable through its own state reconstruction; relational comparison
begins only at a separately declared gate. Whether and where established
theories support, constrain or complement that construction remains open
source-based research.

The next question followed naturally:  
What if observable direction, constraints and target/reference spaces could be
described — even with reduced precision — within a **five-dimensional
observation space**, without treating inferred intention as a measured inner
state?

Would that be sufficient for early drift detection?  
For a judge-model?  
For a human-in-the-loop?  
For governance and compliance?

Or, more practically:  
Could it help developers detect early when an autonomous orthopedic purchasing agent suddenly starts ordering chicken feed — or cardiology medication?

This perspective formed the basis for situating the versioned KSODI Method
inside the broader **KSODI Framework** and considering an associated
**KSODI Protocol**: the Method supplies observation, while interaction
practice, governance interpretation and any later intervention remain
separate responsibilities. Earlier work used the names IDAS and SIRA; their
transition is documented in the
[v3.51 naming note](./KSODI-Framework-and-Protocol-Naming-Transition_V351.md).
The intended use includes explainable drift and anomaly observation in
continuous and agent-based systems; it does not by itself establish cause,
intent or an automated control decision.

<br>

We are still testing, observing and learning — and remain open to additional perspectives and critical feedback.  
Feel free to reach out.

<br>
_____________________________________
<br>

*Personal note by Anne:*  

<br>

*From time to time, I write on Substack at the intersection of technology and human experience — exploring ideas, short reflections, and occasional pieces of fiction and poetry.  
Some of these texts capture moments of *crystallization* (one of my short stories): when abstract structure, intuition and meaning briefly align.*

*📬 [Subscribe to my Substack](https://annesteinacker.substack.com/subscribe)*
