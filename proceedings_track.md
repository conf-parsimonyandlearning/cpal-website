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
{% assign session_number = event_name | split: " " | last %}

{% assign papers = site.proceedings | where: 'session', session_number | sort: 'order' %}
{% for paper in papers %}

### {{ paper.order }}. [{{ paper.title }}]({{ paper.link }})
{{ paper.authors }}

{: .fs-2 }
Keywords: *{{ paper.keywords }}*

{% endfor %}

{% endif %}

{% endfor %}

{% endfor %}
{% endfor %}
