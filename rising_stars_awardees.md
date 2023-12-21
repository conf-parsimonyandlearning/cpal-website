---
layout: page
title: Awardees
parent: Rising Stars Award
nav_order: 2
---

{% include splash.html %}

# CPAL Rising Stars Awardees

CPAL is excited to announce the CPAL Rising Stars awardees for 2024. 
The awardees showcase expertise in fields such as machine learning, applied 
mathematics, signal processing, optimization, systems, and more
interdisciplinary fields. Together, they exemplify outstanding research
potential for the CPAL community.

CPAL Rising Stars will attend the CPAL conference in person and present a short
overview of their research. Awardees are listed below, along with their planned
presentation information.


## List of Awardees


<!-- vim-markdown-toc GFM -->

<!-- vim-markdown-toc -->

{% assign risingstars = site.risingstars %}
{% for risingstar in risingstars %}

{{ risingstar }}

**Title**: {{ risingstar.talk }}

**Abstract**: {{ risingstar.abstract }}

{% endfor %}
