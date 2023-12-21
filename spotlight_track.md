---
layout: page
title: Spotlight Track
description: Accepted papers for CPAL 2024 Spotlight Track
parent: Accepted Papers
---

{% include splash.html %}

# Spotlight Track: Accepted Papers

## Presentation Format

Accepted papers will be presented in one of two spotlight poster sessions
during the conference.

The ordering of session numbers matches their chronological ordering.
See the [full program]({{ site.baseurl }}/program_schedule/) for the precise
time and location of each spotlight presentation session.

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

{% assign papers = site.spotlight | where: 'session', session_number | sort: 'order' %}
{% for paper in papers %}

### [{{ paper.title }}]({{ paper.link }})
{{ paper.authors }}

{: .fs-2 }
Keywords: *{{ paper.keywords }}*

{% endfor %}

{% endif %}

{% endfor %}

{% endfor %}
{% endfor %}
