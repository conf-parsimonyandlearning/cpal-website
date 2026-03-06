---
layout: page
title: Rising Stars Awardees
description: Awardees of the CPAL 2026 Rising Stars Award
parent: Rising Stars Award
nav_order: 2
---

{% include splash.html %}

# CPAL 2026 Rising Stars Awardees

{% assign risingstars = site.risingstars | sort: 'order' %}

{% for risingstar in risingstars %}

{{ risingstar }}

{% endfor %}
