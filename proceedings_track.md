---
layout: page
title: Proceedings Track
description: Accepted papers for CPAL 2024 Proceedings Track
parent: Accepted Papers
---

{% include splash.html %}

# Proceedings Track: Accepted Papers

## Presentation Format

Accepted papers will be presented in one of six oral sessions during the conference.

Presentations are ten minutes in duration, with two minutes for Q&A.

The ordering of session numbers matches their chronological ordering, and
presentations will be delivered in the order they are listed.
See the [full program]({{ site.baseurl }}/program_schedule/) for the precise
time and location of each oral session.

## Oral Session 1

{% assign papers = site.proceedings | where: 'session', '1' | sort: 'order' %}
{% for paper in papers %}

### {{ paper.order }}. [{{ paper.title }}]({{ paper.link }})
{{ paper.authors }}

{: .fs-2 }
Keywords: *{{ paper.keywords }}*

{% endfor %}

## Oral Session 2

{% assign papers = site.proceedings | where: 'session', '2' | sort: 'order' %}
{% for paper in papers %}

### {{ paper.order }}. [{{ paper.title }}]({{ paper.link }})
{{ paper.authors }}

{: .fs-2 }
Keywords: *{{ paper.keywords }}*

{% endfor %}

## Oral Session 3

{% assign papers = site.proceedings | where: 'session', '3' | sort: 'order' %}
{% for paper in papers %}

### {{ paper.order }}. [{{ paper.title }}]({{ paper.link }})
{{ paper.authors }}

{: .fs-2 }
Keywords: *{{ paper.keywords }}*

{% endfor %}

## Oral Session 4

{% assign papers = site.proceedings | where: 'session', '4' | sort: 'order' %}
{% for paper in papers %}

### {{ paper.order }}. [{{ paper.title }}]({{ paper.link }})
{{ paper.authors }}

{: .fs-2 }
Keywords: *{{ paper.keywords }}*

{% endfor %}

## Oral Session 5

{% assign papers = site.proceedings | where: 'session', '5' | sort: 'order' %}
{% for paper in papers %}

### {{ paper.order }}. [{{ paper.title }}]({{ paper.link }})
{{ paper.authors }}

{: .fs-2 }
Keywords: *{{ paper.keywords }}*

{% endfor %}

## Oral Session 6

{% assign papers = site.proceedings | where: 'session', '6' | sort: 'order' %}
{% for paper in papers %}

### {{ paper.order }}. [{{ paper.title }}]({{ paper.link }})
{{ paper.authors }}

{: .fs-2 }
Keywords: *{{ paper.keywords }}*

{% endfor %}
