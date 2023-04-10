---
layout: page
title: Invited Speakers
description: Details of invited speakers at the conference
nav_order: 2
---

{% include splash.html %}


# TODO for this page:
- Update the speakers

# Confirmed Speakers

Clicking a speaker's photo will jump to their talk information below.

{% include speakers.html %}

# Talk Details

{% assign speakers = site.speakers %}
{% for speaker in speakers %}

### [{{ speaker.name }}]({{ speaker.website }})

{{ speaker.affiliation }}

#### Title: {{ speaker.talk }}

#### Abstract
{{ speaker.abstract}}

{% endfor %}
