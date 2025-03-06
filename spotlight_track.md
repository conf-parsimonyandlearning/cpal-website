---
layout: page
title: Spotlight Track
description: Accepted papers for CPAL 2024 Spotlight Track
parent: Accepted Papers
---

{% include splash.html %}

# Spotlight Track: Accepted Papers

Accepted Spotlight Track papers are presented as
[posters]({{site.baseurl}}/posters) at CPAL 2025.
See the [full program]({{ site.baseurl }}/program_schedule/) for the precise
time and location of each poster session.

{% assign papers = site.spotlight | sort: 'id' %}
{% for paper in papers %}

### [{{ paper.title }}]({{ paper.link }})
{{ paper.authors }}

{: .fs-2 }
Keywords: *{{ paper.keywords }}*

{% endfor %}
