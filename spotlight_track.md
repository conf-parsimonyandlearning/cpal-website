---
layout: page
title: Spotlight Track
description: Accepted papers for CPAL 2024 Spotlight Track
parent: Accepted Papers
---

{% include splash.html %}

# Spotlight Track: Accepted Papers

{% assign papers = site.spotlight %}
{% for paper in papers %}

### [{{ paper.title }}]({{ paper.link }})
{{ paper.authors }}

{: .fs-2 }
Keywords: *{{ paper.keywords }}*

{% endfor %}