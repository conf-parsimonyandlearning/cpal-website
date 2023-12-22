---
layout: page
title: Organization Committee
parent: Organizers
nav_order: 0
---

# Organization Committee

## General Chairs

<div style="clear: both; display: flex; flex-wrap: wrap; justify-content:
  flex-start;">

  {% assign gcs = site.organizers | where: 'role', 'General Chair' %}
  {% for organizer in gcs %}
  {{ organizer }}
  {% endfor %}

</div>

## Program Chairs

<div style="clear: both; display: flex; flex-wrap: wrap; justify-content:
  flex-start;">

  {% assign pcs = site.organizers | where: 'role', 'Program Chair' %}
  {% for organizer in pcs %}
  {{ organizer }}
  {% endfor %}

</div>


## Local Chairs

<div style="clear: both; display: flex; flex-wrap: wrap; justify-content:
  flex-start;">

  {% assign lcs = site.organizers | where: 'role', 'Local Chair' %}
  {% for organizer in lcs %}
  {{ organizer }}
  {% endfor %}

</div>

## Publication Chairs

<div style="clear: both; display: flex; flex-wrap: wrap; justify-content:
  flex-start;">

  {% assign pubcs = site.organizers | where: 'role', 'Publication Chair' %}
  {% for organizer in pubcs %}
  {{ organizer }}
  {% endfor %}

</div>

## Industry Liaison Chairs

<div style="clear: both; display: flex; flex-wrap: wrap; justify-content:
  flex-start;">

  {% assign spcs = site.organizers | where: 'role', 'Industry Liaison Chair' %}
  {% for organizer in spcs %}
  {{ organizer }}
  {% endfor %}

</div>



## Panel Chairs

<div style="clear: both; display: flex; flex-wrap: wrap; justify-content:
  flex-start;">

  {% assign pancs = site.organizers | where: 'role', 'Panel Chair' %}
  {% for organizer in pancs %}
  {{ organizer }}
  {% endfor %}

</div>


## Tutorial Chairs

<div style="clear: both; display: flex; flex-wrap: wrap; justify-content:
  flex-start;">

  {% assign tutcs = site.organizers | where: 'role', 'Tutorial Chair' %}
  {% for organizer in tutcs %}
  {{ organizer }}
  {% endfor %}

</div>


## Publicity Chairs

<div style="clear: both; display: flex; flex-wrap: wrap; justify-content:
  flex-start;">

  {% assign publiccs = site.organizers | where: 'role', 'Publicity Chair' %}
  {% for organizer in publiccs %}
  {{ organizer }}
  {% endfor %}

</div>


## Rising Stars Award Chairs

<div style="clear: both; display: flex; flex-wrap: wrap; justify-content:
  flex-start;">

  {% assign rsacs = site.organizers | where: 'role', 'Rising Stars Award Chair' %}
  {% for organizer in rsacs %}
  {{ organizer }}
  {% endfor %}

</div>

## Web Chairs

<div style="clear: both; display: flex; flex-wrap: wrap; justify-content:
  flex-start;">

  {% assign wcs = site.organizers | where: 'role', 'Web Chair' %}
  {% for organizer in wcs %}
  {{ organizer }}
  {% endfor %}

</div>


{: .fs-1 .text-grey-dk-000}
\* Ordered alphabetically
