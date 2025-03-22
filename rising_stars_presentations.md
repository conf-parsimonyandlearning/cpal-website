---
layout: page
title: Rising Stars Presentations
description: Scheduling information for Rising Stars presentations
parent: Conference Program
nav_order: 4
---

{% include splash.html %}

# CPAL Rising Stars Presentation Sessions
{: .no_toc}

## Presentation Format
{: .no_toc}

Each awarded [CPAL Rising Star]({{ site.baseurl }}/rising_stars_awardees/)
will give a talk about their research in one of three sessions during the
conference.

Presentations are ten minutes in duration, with two minutes for Q&A.

The ordering of session numbers matches their chronological ordering, and
presentations will be delivered in the order they are listed.
See the [full program]({{ site.baseurl }}/program_schedule/) for the precise
time and location of each CPAL Rising Stars session.

## Quick Links
{: .no_toc}
1. TOC
{:toc}


{% assign calendars = site.calendars %}

{% for calendar in calendars %}
{% for day in calendar.calendar %}
{% assign event_day = day.name | replace: '<br>', ' -- ' %}

{% for event in day.events %}

{% if event.class == 'rising' %}

<!-- print information for this session. -->
{% assign event_name = event.name | strip_html %}
{% assign event_time = event.start | strip_html %}
{% assign event_end = event.end | strip_html %}
## {{ event_name }}
#### Time: [{{ event_day }} -- {{ event_time }} to {{ event_end }}]({{ site.baseurl }}/program_schedule/) 

<!-- print papers for this session. -->
{% assign session_number = event_name | split: " " | last %}

{% assign risingstars = site.risingstars | where: 'session', session_number
| sort: order %}
{% for risingstar in risingstars %}

{{ risingstar }}

**Title**: {{ risingstar.talk }}

**Abstract**: {{ risingstar.abstract }}

{% endfor %}

{% endif %}

{% endfor %}

{% endfor %}
{% endfor %}
