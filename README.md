---
layout: default
title: Home
permalink: /
nav_order: 0
---

{% include splash.html %}

{: .highlight}
{: .fs-5}
The Conference on Parsimony and Learning (CPAL) is an annual research
conference focused on addressing the parsimonious, low dimensional structures
that prevail in machine learning, signal processing, optimization, and beyond.
We are interested in theories, algorithms, applications, hardware and systems,
as well as scientific foundations for learning with parsimony. 

<!--
We describe [our]({{ site.baseurl }}/organization_committee) vision for the conference in
more detail [here]({{ site.baseurl }}/vision).
-->

{: .fs-7 .text-center}
**CPAL 2024 will take place from January 3--6 <br> at the University of Hong Kong!**

<div class="youtube-wrapper">
<div class="youtube-video">
<iframe src="https://www.youtube-nocookie.com/embed/pGbjiZOR63I?rel=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>
</div>
<br>


<!--
# Call for Papers

{: .fs-5 .text-center}
[Submit your Work on OpenReview](https://openreview.net/group?id=CPAL.cc/2024/Conference)

We are pleased to invite paper submissions for the first Conference on
Parsimony and Learning. Please see the [**call for papers**]({{ site.baseurl
}}/tracks) for details about the submission and reviewing process, as well as
subject areas of interest and general policies. Stay tuned for further updates.


# Key Dates and Deadlines


*All deadlines are 23:59 [Anywhere-on-Earth (AOE)](https://www.ieee802.org/16/aoe.html)*

- **August 28th, 2023**: Submission Deadline for [Proceedings Track](https://openreview.net/group?id=CPAL.cc/2024/Conference)
- **October 1st, 2023**: [Rising Stars Award]({{ site.baseurl }}/rising_stars)
  Application Deadline
- **October 10th, 2023**: Submission Deadline for [Recent Spotlight Track](https://openreview.net/group?id=CPAL.cc/2024/Recent_Spotlight_Track)
- **November 20th, 2023**: Final Decisions Released (Both Tracks)
- **January 3rd-6th, 2024**: Main Conference (In-Person, HKU Main Campus)

{: .highlight}
See the [deadlines page]({{ site.baseurl }}/deadlines) for a complete list of
key dates.
-->

# Register to Attend CPAL 2024


All CPAL attendees are required to register. **The deadline to register is
December 15th, 2023.**

{: .fs-7 .text-center}
[Registration Link](https://datascience.hku.hk/cpal-registration)

<!-- # Tentative Program -->


# Keynote Speakers

Information on the speakers' planned talks is available [here]({{site.baseurl}}/speakers/#talk-details).

{% include speakers.html %}


# Tentative Program

All times below are in HKT (GMT+8).

{% for calendar in site.calendars %}
{{ calendar }}
{% endfor %}


{% include sponsors.html %}
