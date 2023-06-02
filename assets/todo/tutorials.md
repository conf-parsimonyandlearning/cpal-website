---
layout: page
title: Tutorials
description: A listing of the tutorials that will be presented at the conference.
nav_order: 3
nav_exclude: true
search_exclude: true
---

{% include splash.html %}

# TODO for this page:
- Do we want to offer our existing course?
- Do we want a call?

# Tutorials

The first day of the workshop features tutorial presentations from a subset of
the organizers. These tutorials present an up-to-date account of the
intersection between low-dimensional modeling and deep learning in an
accessible format. 

The tutorials are summarized below.
See [the schedule]({{ site.baseurl }}/schedule) for the precise times of each
tutorial.
Some of the tutorials draw on material from [an ICASSP 2022 short
course](https://highdimdata-lowdimmodels-tutorial.github.io/).

{% assign organizers = site.tutorials %}
{% for organizer in organizers %}

### {{ organizer.tutorial }}

{{ organizer }}


{{ organizer.abstract }}

{% endfor %}
