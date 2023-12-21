---
layout: page
title: Spotlight Track
description: Accepted papers for CPAL 2024 Spotlight Track
parent: Accepted Papers
---

{% include splash.html %}

# Spotlight Track: Accepted Papers

## Presentation Format

Accepted papers will be presented in one of two spotlight poster sessions
during the conference.

The ordering of session numbers matches their chronological ordering.
See the [full program]({{ site.baseurl }}/program_schedule/) for the precise
time and location of each spotlight presentation session.

## Spotlight Poster Session 1

{% assign papers = site.spotlight | where: 'session', '1' %}
{% for paper in papers %}

### [{{ paper.title }}]({{ paper.link }})
{{ paper.authors }}

{: .fs-2 }
Keywords: *{{ paper.keywords }}*

{% endfor %}

## Spotlight Poster Session 2

{% assign papers = site.spotlight | where: 'session', '2' %}
{% for paper in papers %}

### [{{ paper.title }}]({{ paper.link }})
{{ paper.authors }}

{: .fs-2 }
Keywords: *{{ paper.keywords }}*

{% endfor %}
