---
layout: page
title: Conference Vision
description: A short essay on the organizers' vision for the conference
nav_order: 0
---

{% include splash.html %}

# Conference Vision

{: .quote}
> *“Entities should not be multiplied unnecessarily.”* <br>
> {: .text-left .fs-4}
> -- William of Ockham 
> {:.text-right}

The ways we process, interpret, and predict with data in engineering and
scientific applications have changed immeasurably since the advent of the deep
learning era. The ‘traditional’ approach to algorithm design, based around
parametric models for structured signals and measurements – say sparse and
low-rank models – and the associated optimization toolkit, is now regularly
supplemented with data-driven learning-based techniques, where large-scale deep
networks are pretrained and then adapted to a variety of tasks. The successes
of both paradigms have depended crucially on the low-dimensional structure
present in real-world data, to the extent that we view the roles of *parsimony*
of data processing algorithms – whether explicit or implicit, as with deep
networks – and *learning* as inextricably linked.

Over the last ten or so years, several rich lines of research, both applied and
theoretical, have explored the interplay between these two principles. Some
works explore the role of signal models in the era of deep learning, attempting
to understand the interaction between deep networks and nonlinear, multimodal
data. Others have applied these insights to the principled design of deep
architectures that incorporate known structures in data into the learning
process. Still others have considered the parameters of generic deep networks
as first-class citizens in their own right, exploring ways to compress and
sparsify models for greater efficiency, often accompanied with hardware or
system-aware co-designs. Across each of these settings, theoretical works have
begun to explain the foundations of efficient learning – from optimization to
generalization – in spite of “overparameterization” and other obstructions. And
most recently, the advent of foundation models has led some to posit that
parsimony itself is a fundamental part of the learning objective of an
intelligent system, connecting to ideas from neuroscience on compression as a
guiding principle for the brain representing the sensory data of the world.

By and large, these lines of work have developed in isolation from one another,
in spite of their common basis in parsimony and learning. Our intention in
organizing this conference is to address this: *we envision the conference as a
general forum where researchers in machine learning, applied mathematics,
signal processing, optimization, hardware & systems, and all associated science
and engineering applications can gather, share insights, and ultimately work
towards a common data-centric understanding of modern parsimonious learning
frameworks.*
