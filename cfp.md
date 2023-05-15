---
layout: page
title: Call for Papers
description: Call for papers and submission information
has_children: true
nav_order: 2
---

{% include splash.html %}

# Subject Areas

We invite submissions relevant to the following broad areas of interest, all
connected with parsimony and learning in modern data science:
- Models and Algorithms 
- Data
- Theory
- Hardware and Systems
- Applications and Science

Please reference the detailed listing [here]({{ site.baseurl }}/subject_areas).


# Submission Tracks and Review Process

We will have a main proceeding track (archival), and a “recent spotlight” track (non-archival). 

## Proceeding Track  (archival)

The submission and review stage will be **double-blind**. We use OpenReview to host
papers and allow for public discussions. Before the end of the
Authors-Reviewers Discussion Stage, besides official reviews, anyone can post
publicly visible comments; and authors can participate in the discussion as
well as update their submission at any time. After that, there will be an
internal discussion period amongst reviewers and ACs with the aim of
summarizing the review process, after which the final decisions are made by
ACs.

After the notification deadline, accepted and opted-in rejected papers will be
made public and open for non-anonymous public commenting. Their anonymous
reviews, meta-reviews, author responses and reviewer responses will also be
made public. Authors of rejected papers will have two weeks after the
notification deadline to opt in to make their de-anonymized rejected papers
public in OpenReview.  

Submissions that are substantially similar to papers previously published, or
submitted in parallel to other peer-reviewed venues with proceedings or
journals may not be submitted to the Proceeding Track. Papers previously
presented at workshops are permitted, so long as they did not appear in a
conference proceedings (e.g., CVPRW proceedings), a journal or a book.

The existence of non-anonymous preprints (on arXiv or other online
repositories, personal websites, social media) will not result in rejection.
Authors may submit anonymized work to CPAL that is already available as a
preprint (e.g., on arXiv) without citing it.

Accepted papers will be published in the [Proceedings for Machine Learning
Research (PMLR)](https://proceedings.mlr.press/). Full proceedings papers can have up to 9 pages with unlimited
pages for references and appendix. Upon acceptance of a paper, at least one of
the authors must join the conference.

### Using Large Language Models (LLMs) 
We follow the rule by NeurIPS 2023, quoted as follows:

*“We welcome authors to use any tool that is suitable for preparing high-quality papers and research. However, we ask authors to keep in mind two important criteria. First, we expect papers to fully describe their methodology, and any tool that is important to that methodology, including the use of LLMs, should be described also. For example, authors should mention tools (including LLMs) that were used for data processing or filtering, visualization, facilitating or running experiments, and proving theorems. It may also be advisable to describe the use of LLMs in implementing the method (if this corresponds to an important, original, or non-standard component of the approach). Second, authors are responsible for the entire content of the paper, including all text and figures, so while authors are welcome to use any tool they wish for writing the paper, they must ensure that all text is correct and original.”*
{: .quote}

## “Recent Spotlight” Track (non-archival)

We meanwhile aim to showcase the latest research innovations at all stages of
the research process, from work-in-progress to recently published papers.
Concretely, we ask members of the community to submit a conference-style paper
(from four to eight pages, with extra pages for references) describing the
work. Please also upload a short (250 word) abstract to OpenReview. OpenReview
submissions may also include any of the following supplemental materials that
describe the work in further detail:

- **A poster** (in PDF form) presenting results of work-in-progress.
- **A link to an arXiv preprint or a blog post** (e.g., distill.pub, Medium) describing results.
- **Appendices** with detailed derivations and additional experiments.

This track is non-archival and has no proceedings. We permit under-review or concurrent submissions. Reviewing will be performed in a single-blind fashion (authors should not anonymize their submissions), and will be held with the same high quality bar with the Proceeding Track. 


# Reviewer Guidelines


## Notable Innovations in Our Review Mechanism

CPAL strives for providing every paper with high-quality, accountable reviews,
and therefore takes the following actions in addition:

- ***Shepherding by an Action PC:*** Every paper’s final decision, after being
  recommended by AC, will go through the direct shepherding of all program
  chairs (led by one “action PC”). The action PC has two main duties:
  - (before final decision released) The action PC will pay particular
  attention to the borderline cases and the dispute (large score variations)
  cases, and will be asked to write additional “meta-meta reviews” in those
  cases and potentially calibrate on top of AC recommendations.  Final
  decisions will be scrutinized and made in a joint meeting by all program
  chairs. 
  - (after receiving the camera-ready) Each accepted paper’s authors will be
  asked to submit a one-page cover letter, summarizing what revisions are made
  between the paper’s submitted and camera-ready versions. The action PC will
  ensure: (1) all “promised” changes by authors during the discussion stage are
  indeed implemented; (2) no change that is “too substantial” and
  “unsoliciated” shall be made to the paper, unless in exceptional
  circumstances where the action PC has to approve case-by-case. The action PC
  reserves the right to reject a camera-ready submission and exclude it from
  the conference proceedings.

- ***Semi-Open Identity for Accountability (Action PC and/or AC)***: For every
  **accepted paper**, the names of its AC and action PC will be publicly released
  on its OpenReview page too. For every rejected paper (excluding withdrawals),
  only the name of its action PC will be displayed. **This decision was not
  reached lightly; but we hope it would meaningfully add credibility and
  accountability for every paper’s final outcome.**

- ***Reviewer Rating and “Dynamic Sparse Selection”:*** each AC will be asked
  to rate every reviewer in their batch, in terms of timeliness and quality.
  Program chairs, who know all reviewers’ identities, will compile a list of
  reviewers sorted by their average ratings received. Reviewers that receive
  consistent low reviewer rating for multiple papers / from multiple ACs will
  be excluded from future review processes.

## General Guidelines

We all like the Acceptance Criteria made by TMLR
[https://jmlr.org/tmlr/acceptance-criteria.html](https://jmlr.org/tmlr/acceptance-criteria.html)
and would instruct our ACs and reviewers to honor the same. In particular we
note: 

*“Crucially, it should not be used as a reason to reject work that isn't
considered “significant” or “impactful” because it isn't achieving a new
state-of-the-art on some benchmark. Nor should it form the basis for rejecting
work on a method considered not “novel enough”, as novelty of the studied
method is not a necessary criteria for acceptance. We explicitly avoid these
terms (“significant”, “impactful”, “novel”), and focus instead on the notion of
“interest”. If the authors make it clear that there is something to be learned
by some researchers in their area from their work, then the criteria of
interest is considered satisfied.*
{: .quote}


# Code of Conduct
*(Adapted from ICML/ICLR/NeurIPS/LoG)*

We strive to hold a conference in which any person can meaningfully participate
in the LoG community through: sharing ideas, presenting their work, meeting
members of the community, learning from other people’s work, and discussing
ways to improve the community. 

This conference will work towards preventing any type of discrimination based
on age, disability, ethnicity, experience in the field, gender identity,
nationality, physical appearance, race, religion, sexual orientation, or other
protected characteristics. We strictly prohibit any actions that may prevent
the participation of any attendee, including: bullying, harassment,
inappropriate media, offensive language, violence, zoom bombing, and so on.

Please report any violations of the code of conduct to the conference
organizers, via email, slack, or any other channels. If requested, we can
handle these reports anonymously, to protect the person making the report.
Violators of the code of conduct will be asked to stop their inappropriate
behavior, and may be removed from their right to participate in the conference.
Further disciplinary action such as bans from future iterations of the
conference may be taken.

