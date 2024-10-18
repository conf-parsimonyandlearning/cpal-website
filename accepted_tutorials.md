---
layout: page
title: Accepted Tutorials
description: Information about last-day tutorials at CPAL (open to the public)
parent: Tutorials
nav_exclude: true
---

{% include splash.html %}

# Tutorials

The final day of the conference features tutorial presentations, which are open
to the public.
These tutorials present an up-to-date account of the intersection between
low-dimensional modeling and deep learning in an accessible format.

The tutorials consist of two parallel tracks, respectively titled
***[Learning Deep Low-dimensional Models from High-Dimensional Data: From Theory to Practice]({{ site.baseurl }}/tutorials/#track-learning-deep-low-dimensional-models-from-high-dimensional-data-from-theory-to-practice)***,
and ***[Advances in Machine Learning for Image Reconstruction: Sparse Models to Deep Networks]({{ site.baseurl }}/tutorials/#track-advances-in-machine-learning-for-image-reconstruction-sparse-models-to-deep-networks)***.

Each track consists of four lectures.
The planned content of the two tracks is summarized below.
See the schedule for the precise times of each tutorial.

## Track: Learning Deep Low-dimensional Models from High-Dimensional Data: From Theory to Practice

{% assign tutorials = site.tutorials | where: 'track', 1 | sort: 'order' %}
{% for tutorial in tutorials %}

### Lecture {{ tutorial.order }} -- {{ tutorial.tutorial }}

{{ tutorial }}

<!-- #### Time and Location: [Day {{ speaker.day }}, {{ speaker.start }} HKT]({{ site.baseurl }}/program_schedule/), {{ speaker.location }}-->

#### Abstract
{{ tutorial.abstract }}

{% endfor %}


## Track: Advances in Machine Learning for Image Reconstruction: Sparse Models to Deep Networks

Lectures 1-3 will cover a diverse spectrum of topics across sparse modeling and
deep learning and theory with applications in medical imaging and image
restoration/computer vision. A subset of works across topics will be discussed
including works from tutorial presenters.

{% assign tutorials = site.tutorials | where: 'track', 2 | sort: 'order' %}
{% for tutorial in tutorials %}


{% if tutorial.tutorial %}

### Lecture {{ tutorial.order }} -- {{ tutorial.tutorial }}

{% endif %}

{{ tutorial }}

<!-- #### Time and Location: [Day {{ speaker.day }}, {{ speaker.start }} HKT]({{ site.baseurl }}/program_schedule/), {{ speaker.location }}-->

{% if tutorial.abstract %}

#### Abstract
{{ tutorial.abstract }}

{% endif %}

{% endfor %}
