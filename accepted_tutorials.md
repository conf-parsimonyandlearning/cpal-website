---
layout: page
title: Accepted Tutorials
description: Information about tutorials at CPAL 2026
parent: Tutorials
nav_order: 1
---

{% include splash.html %}

# Tutorials

The first day of the conference features six tutorial presentations, arranged
into two parallel tracks across three sessions throughout the day.
Each tutorial consists of 2.5 hours of lectures from leading experts,
with topics ranging from theory to practice and presentations in an
accessible format.

See the [program schedule]({{ site.baseurl }}/program_schedule/) for the
precise times and locations of each tutorial.

# List of Tutorials

{% assign track1 = site.tutorials | where: 'track', '1' | sort: 'order' %}
{% assign track2 = site.tutorials | where: 'track', '2' | sort: 'order' %}

{% assign t1_tutorials = track1 | map: 'tutorial' | uniq %}
{% assign t2_tutorials = track2 | map: 'tutorial' | uniq %}

## Track 1

{% for title in t1_tutorials %}

### {{ title }}

#### Presenters: {% assign presenters = track1 | where: 'tutorial', title %}{% for p in presenters %}{{ p.name }} ({{ p.affiliation }}){% unless forloop.last %}, {% endunless %}{% endfor %}

{% assign abstract_presenter = presenters | where_exp: 'p', 'p.abstract != ""' | first %}
{% if abstract_presenter %}
#### Abstract
{{ abstract_presenter.abstract }}
{% endif %}

{% endfor %}

## Track 2

{% for title in t2_tutorials %}

### {{ title }}

#### Presenters: {% assign presenters = track2 | where: 'tutorial', title %}{% for p in presenters %}{{ p.name }} ({{ p.affiliation }}){% unless forloop.last %}, {% endunless %}{% endfor %}

{% assign abstract_presenter = presenters | where_exp: 'p', 'p.abstract != ""' | first %}
{% if abstract_presenter %}
#### Abstract
{{ abstract_presenter.abstract }}
{% endif %}

{% endfor %}
