---
layout: page
title: Call for Papers
permalink: /call_for_papers/
parent: Call
nav_order: 1
---

# Call for Papers — CPAL 2027

**The Fourth Conference on Parsimony and Learning**  
**March 23–26, 2027 · Hitotsubashi Hall, Tokyo, Japan**

CPAL 2027 invites research that makes **parsimony central to learning**. Choose the **Proceedings Track** for original, unpublished archival papers or the **Recent Spotlight Track** for non-archival presentations of timely research. Below are the scientific scope, track requirements, deadlines, and review policies in one place.

[Submission portal and templates]({{ '/openreview/' | relative_url }}){: .btn .btn-primary }
[Key Dates]({{ '/deadlines/' | relative_url }}){: .btn }

**On this page**

- [Scope and subject areas](#about-cpal)
- [Compare submission tracks](#submission-tracks)
- [Important dates](#important-dates)
- [Submission requirements](#submission-requirements)
- [Review criteria and process](#review-process)
- [Presentation and attendance](#presentation-and-attendance)
- [AI-assisted tools](#use-of-ai-assisted-tools)
- [Submission and contact](#submission-and-contact)

## About CPAL

Modern learning systems operate in enormous ambient spaces, yet their data, representations, dynamics, and solutions often admit much simpler descriptions. The Conference on Parsimony and Learning (CPAL) brings together researchers seeking to understand, discover, and exploit these structures across machine learning, signal processing, optimization, statistics, applied mathematics, neuroscience, scientific computing, and intelligent systems.

CPAL 2027 invites theoretical, methodological, empirical, and systems contributions in which **parsimony is central**. Parsimony may take the form of sparsity, low rank or intrinsic dimension, symmetry, modularity, compositionality, compressibility, simple mechanisms, or structured computation. Work on foundation, generative, multimodal, and agentic models is encouraged when the underlying parsimony principle is explicit. Authors should explain what the parsimonious structure is, whether it is assumed, learned, or emergent, and what it enables.

### Subject Areas

CPAL 2027 welcomes contributions in which a clear parsimony principle is central. The following list is illustrative rather than exhaustive.

#### Theory and Foundations

- Sparsity, structured sparsity, low rank, subspaces, manifolds, tensors, graphs, latent-variable models, and other low-dimensional structures.
- Statistical and computational foundations of representation and feature learning.
- Identifiability, generalization, robustness, implicit bias, and statistical–computational tradeoffs.
- Symmetry, invariance, equivariance, causality, modularity, and compositional structure.
- Information-theoretic, minimum-description-length, and compression-based views of learning.
- Theoretical neuroscience, cognitive science, and biologically inspired mechanisms for parsimonious learning.

#### Methods and Models

- Sparse coding, dictionary learning, matrix and tensor methods, inverse problems, and structured recovery.
- Optimization and feature-learning dynamics that discover or induce parsimonious structure.
- Interpretable and structured neural architectures, including algorithm unrolling.
- Pruning, quantization, distillation, low-rank adaptation, modular networks, mixtures of experts, and conditional computation.
- Data-, parameter-, memory-, energy-, and compute-efficient training and inference.
- Parsimonious foundation, generative, multimodal, federated, continual, and agentic learning.

#### Systems, Data, and Applications

- Hardware–algorithm and software–system co-design for structured or sparse computation.
- Benchmarks, datasets, and metrics that reveal or evaluate parsimony and accuracy–efficiency tradeoffs.
- Parsimonious learning for perception, action, reasoning, robotics, and control.
- Scientific machine learning, signal and image processing, neuroscience, biology, medicine, engineering, and social science.
- Resource-constrained, distributed, networked, and real-world intelligent systems.

{: .highlight }
Submissions proposing a new notion of parsimony are especially welcome when the connection is clearly motivated. Authors who are uncertain about fit may contact the Program Chairs at [pcs@cpal.cc](mailto:pcs@cpal.cc).

## Submission Tracks

| Feature | [Proceedings Track](#proceedings-track-archival) | [Recent Spotlight Track](#recent-spotlight-track-non-archival) |
|:--|:--|:--|
| Status | Archival | Non-archival presentation track |
| Review | Double-blind | Single-blind; do not anonymize |
| Format | CPAL template; 9 pages of main text | 250-word abstract plus supporting material |
| Prior/concurrent work | No substantially similar prior or concurrent archival submission | Concurrent, under-review, and recently published work permitted |
| Deadline | See [Proceedings dates](#proceedings-dates) | See [Recent Spotlight dates](#recent-spotlight-dates) |
| Publication | [Proceedings of Machine Learning Research (PMLR)](https://proceedings.mlr.press/) | No proceedings or DOI |
| Presentation | Poster; selected papers may receive talks | Poster; selected contributions may receive short talks |

## Important Dates

Unless otherwise stated, submission deadlines are **23:59 Anywhere on Earth (AoE)**.

### Proceedings dates

{% include proceedings_dates.md %}

### Recent Spotlight dates

{% include spotlight_dates.md %}

See [Key Dates]({{ "/deadlines/" | relative_url }}) for the conference, tutorial, and Rising Stars calendars.

## Submission Requirements

### Proceedings Track (archival)

The Proceedings Track is intended for original, unpublished research. The submission and review process is **double-blind** and will be hosted on [OpenReview](https://openreview.net/). Proceedings submissions must use the CPAL 2027 LaTeX style. The main text may contain up to **nine pages**, including figures and tables; references and appendices do not count toward the limit. The main text should be self-contained, and reviewers are not required to read appendices.

- Submissions must be anonymized.
- A public preprint does **not** violate the anonymity policy. Authors should refer to their own work in the third person where appropriate.
- A submission must not be substantially similar to work already published, accepted, or simultaneously under review at another archival conference or journal.
- Prior presentation at a non-archival workshop is permitted provided that the work did not appear in archival proceedings, a journal, or a book.

### Recent Spotlight Track (non-archival)

The Recent Spotlight Track showcases timely research at different stages of development, from technically mature work in progress to recently accepted or published results. It is a **presentation track** and has no proceedings or DOI.

Each submission includes a **250-word abstract** and one of the following:

- a conference-style manuscript describing the work;
- a poster PDF presenting work in progress; or
- the camera-ready version of recently accepted or published work.

Authors may additionally provide appendices or public links that help explain the work. Concurrent or under-review submissions are permitted, as is work accepted or published at an archival venue within the 12 months preceding the [Recent Spotlight deadline](#recent-spotlight-dates). Reviewing is **single-blind**, so authors should not anonymize their submissions.

Selection considers CPAL fit, clarity, technical credibility, timeliness, and discussion value, calibrated to the stated stage of the work. Authors remain responsible for complying with the policies of any other venue to which the same work is submitted.

## Review Process

OpenReview hosts submissions, reviews, author responses, and discussion.

### Review Model

- **Proceedings Track:** double-blind review.
- **Recent Spotlight Track:** single-blind review; authors do not anonymize their submissions.
- Proceedings authors may respond to reviewers and update their manuscript during the published author–reviewer discussion period.
- After author discussion, reviewers and Area Chairs discuss the submission and prepare recommendations.
- Final decisions are made by the Program Chairs with Area-Chair recommendations and paper-level shepherding.

### What CPAL Reviews For

Reviewers should assess whether a submission is:

- technically sound;
- clearly presented;
- relevant to CPAL and explicit about its connection to parsimony;
- appropriately supported by theory, experiments, or evidence for the claims being made; and
- of genuine interest or discussion value to the CPAL research community.

CPAL does **not** require novelty for novelty's sake or a new benchmark state of the art. A strong submission should make clear what new understanding, method, evidence, or scientific perspective the community gains from the work.

For Recent Spotlight submissions, judgments should be calibrated to the stated stage of the project. Work in progress is not expected to have the same degree of completion as an archival Proceedings submission, but it should still be technically credible, clear, timely, and valuable for discussion.

Reviewers should promptly report conflicts of interest or assignment problems through the OpenReview process. Questions about review policy may be directed to the Program Chairs at [pcs@cpal.cc](mailto:pcs@cpal.cc).

## Presentation and Attendance

At least one author of every accepted Proceedings or Recent Spotlight contribution must register for CPAL 2027 and present the work **in person**. All accepted paper-track contributions are expected to be presented as posters; selected Proceedings papers and Recent Spotlight contributions may additionally be invited for oral presentation.

## Use of AI-assisted tools

Authors may use AI-assisted tools in conducting research and preparing manuscripts, but remain fully responsible for the accuracy, originality, citations, ethics, and scientific integrity of all submitted content. Important, original, or non-standard methodological use of such tools should be disclosed sufficiently for readers to understand and reproduce the work. Routine spelling, grammar, formatting, or basic coding assistance need not be disclosed. AI systems should not be listed as authors.

Reviewers and committee members must preserve submission confidentiality and may not upload unpublished submission material to external AI systems.

## Submission and Contact

Proceedings and Recent Spotlight submissions will be handled through **OpenReview**. The CPAL 2027 submission portal and LaTeX/Overleaf template links are collected on the [CPAL OpenReview page]({{ site.baseurl }}/openreview/) as they become active.

For questions about scientific scope or submission policy, contact the Program Chairs at [pcs@cpal.cc](mailto:pcs@cpal.cc).

All participants are expected to follow the [Code of Conduct]({{ "/code_of_conduct/" | relative_url }}).

<script src="{{ site.baseurl }}/assets/js/cpal-countdown.js"></script>
