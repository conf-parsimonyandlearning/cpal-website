---
layout: page
title: Keynote Speakers
permalink: /speakers/
nav_order: 40
---

# Keynote Speakers

CPAL keynote sessions feature invited perspectives on fundamental and emerging questions in parsimonious learning, spanning theory, algorithms, systems, and applications.

<div class="keynote-grid">
  {% for speaker in site.data.keynote_speakers %}
  <article class="keynote-card">
    <a class="keynote-photo-link" href="{{ speaker.website }}" target="_blank" rel="noopener" aria-label="Visit {{ speaker.name }}'s website">
      <span class="keynote-photo-frame">
        <img src="{{ '/assets/images/keynote/' | append: speaker.photo | relative_url }}" alt="Portrait of {{ speaker.name }}" loading="lazy" decoding="async"
          style="object-position: {{ speaker.photo_position }}; transform: translate({{ speaker.photo_x }}, {{ speaker.photo_y }}) scale({{ speaker.photo_scale }});">
      </span>
    </a>
    <h2 class="keynote-name no_anchor"><a href="{{ speaker.website }}" target="_blank" rel="noopener">{{ speaker.name }}</a></h2>
    <p class="keynote-affiliation">{{ speaker.affiliation | escape }}</p>
  </article>
  {% endfor %}
</div>
