---
layout: page
title: Poster Presentations
description: Scheduling information for oral presentations at CPAL
parent: Conference Program
nav_order: 3
---

{% include splash.html %}

# Poster Sessions at CPAL 2025

## Presentation Format

All accepted papers at CPAL 2025, from both the Proceedings and Spotlight
tracks, will be presented as posters at the conference. A select number of
Proceedings track papers are also presented as orals, as specified on the [orals
page]({{site.baseurl}}/orals).

See the [full program]({{ site.baseurl }}/program_schedule/) for an aggregated
view of the precise times and locations of each poster and oral session.

## Logistical Information

Posters should be printed in ***A0 size***, with vertical orientation preferred.


<!-- Loop over oral sessions in the calendar. -->
{% assign calendars = site.calendars %}

{% for calendar in calendars %}
{% for day in calendar.calendar %}
{% assign event_day = day.name | replace: '<br>', ' -- ' %}

{% for event in day.events %}

{% if event.class == 'poster' %}

<!-- print information for this session. -->
{% assign event_name = event.name | strip_html %}
{% assign event_time = event.start | strip_html %}
{% assign event_end = event.end | strip_html %}
## {{ event_name }}
#### Time: [{{ event_day }} -- {{ event_time }} to {{ event_end }}]({{ site.baseurl }}/program_schedule/)

<!-- print papers for this session. -->
{% assign session_number = event_name | split: " " | last %}

{% assign spotlight_papers = site.spotlight | where: 'session', session_number %}
{% assign proceedings_papers = site.proceedings | where: 'session', session_number %}
{% assign papers = spotlight_papers | concat: proceedings_papers | sort: 'num' %}

{% for paper in papers %}

### {{ paper.num }}. [{{ paper.title }}]({{ paper.link }})
{{ paper.authors }}

{: .fs-2 }
Keywords: *{{ paper.keywords }}*

{% endfor %}

{% endif %}

{% endfor %}

{% endfor %}
{% endfor %}
