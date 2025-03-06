---
layout: page
title: Proceedings Track
description: Accepted papers for CPAL 2024 Proceedings Track
parent: Accepted Papers
---

{% include splash.html %}

# Proceedings Track: Accepted Papers

Accepted Proceedings Track papers are presented as
[posters]({{site.baseurl}}/posters) at CPAL 2025.
A select number of accepted Proceedings Track papers will be presented as
[orals]({{site.baseurl}}/orals); they are labeled below with ***(Oral)***.
See the [full program]({{ site.baseurl }}/program_schedule/) for the precise
time and location of each oral and poster session.

{% assign papers = site.proceedings | sort: 'id' %}
{% for paper in papers %}

{% assign suffix = '' %}
{% if paper.type == 'oral' %}
  {% assign suffix = '(Oral)' %}
{% endif %}

### [{{ paper.title }}]({{ paper.link }}){% if suffix != '' %} ***{{suffix}}***{% endif %}
{{ paper.authors }}

{: .fs-2 }
Keywords: *{{ paper.keywords }}*

{% endfor %}
