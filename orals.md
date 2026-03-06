---
layout: page
title: Oral Presentations
description: Scheduling information for oral presentations at CPAL
parent: Conference Program
nav_order: 2
---

{% include splash.html %}

# Oral Sessions at CPAL 2026
{: .no_toc}

A select number of papers from the CPAL 2026 Proceedings Track will be presented
as oral presentations at the conference. The oral presentations are listed
below, in their corresponding oral sessions.

## Quick Links
{: .no_toc}
1. TOC
{:toc}

<!-- Loop over oral sessions in the calendar. -->
{% assign calendars = site.calendars %}

{% for calendar in calendars %}
{% for day in calendar.calendar %}
{% assign event_day = day.name | replace: '<br>', ' -- ' %}

{% for event in day.events %}

{% if event.class == 'oral' %}

<!-- print information for this session. -->
{% assign event_name = event.name | strip_html %}
{% assign event_time = event.start | strip_html %}
{% assign event_end = event.end | strip_html %}
## {{ event_name }}
#### Time: [{{ event_day }} -- {{ event_time }} to {{ event_end }}]({{ site.baseurl }}/program_schedule/)

<!-- print papers for this session. -->
{% assign session_roman = event_name | split: " " | last %}
{% if session_roman == "I" %}{% assign session_number = "1" %}{% elsif session_roman == "II" %}{% assign session_number = "2" %}{% elsif session_roman == "III" %}{% assign session_number = "3" %}{% endif %}

{% assign papers = site.proceedings | where: 'oral_session', session_number | where: 'type', 'oral' | sort: 'oral_order' %}
{% for paper in papers %}

### [{{ paper.title }}]({{ paper.link }})
{: .no_toc}
{{ paper.authors }}

{: .fs-2 }
Keywords: *{{ paper.keywords }}*

{% endfor %}

{% endif %}

{% endfor %}

{% endfor %}
{% endfor %}
