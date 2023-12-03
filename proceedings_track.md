---
layout: page
title: Proceedings Track
description: Accepted papers for CPAL 2024 Proceedings Track
parent: Accepted Papers
---

{% include splash.html %}

# Proceedings Track: Accepted Papers

{% assign papers = site.proceedings %}
{% for paper in papers %}

### [{{ paper.title }}]({{ paper.link }})
{{ paper.authors }}

{: .fs-2 }
Keywords: *{{ paper.keywords }}*

{% endfor %}
