---
layout: page
title: Tutorials
description: Information about last-day tutorials at CPAL (open to the public)
parent: Conference Program
nav_order: 4
---

{% include splash.html %}

# Tutorials

The final day of the conference features tutorial presentations, which are open
to the public.
These tutorials present an up-to-date account of the intersection between
low-dimensional modeling and deep learning in an accessible format.

The tutorials consist of two parallel tracks, respectively titled
***Learning Deep Low-dimensional Models from High-Dimensional Data: From Theory to Practice***,
and ***Recent Advances in Machine Learning for Image Reconstruction: Sparse Models to Deep Networks***.

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


## Track: Recent Advances in Machine Learning for Image Reconstruction: Sparse Models to Deep Networks

The tutorial is divided into two sessions. Sessions 1 and 2 cover a diverse
spectrum of topics across sparse modeling and
deep learning and theory with applications in medical imaging and image
restoration/computer vision. A subset of papers across several topics will be
discussed including contributing works from tutorial presenters.

{% assign tutorials = site.tutorials | where: 'track', 2 | sort: 'order' %}
{% for tutorial in tutorials %}

### Lecture {{ tutorial.order }} -- {{ tutorial.tutorial }}

{{ tutorial }}

<!-- #### Time and Location: [Day {{ speaker.day }}, {{ speaker.start }} HKT]({{ site.baseurl }}/program_schedule/), {{ speaker.location }}-->

#### Abstract
{{ tutorial.abstract }}

{% endfor %}
