---
layout: page
title: Key Dates
nav_order: 6
---
<script src="//code.jquery.com/jquery.js"></script>
<script src="{{ site.baseurl }}/assets/js/jquery.countdown.min.js"></script>
<script src="{{ site.baseurl }}/assets/js/luxon.min.js"></script>

{% include splash.html %}

# Key Dates and Deadlines

*Unless specified otherwise, all deadlines are 23:59 [Anywhere-on-Earth (AOE)](https://www.ieee802.org/16/aoe.html)*

## Main Conference

| Event                           | Date                            | Countdown                    |
|:--------------------------------|:--------------------------------|:-----------------------------|
| [Hotel Registration Deadline]({{ site.baseurl }}/hotels/)    | February 16th, 2026             |<span id="conf-hotel"></span><script type="text/javascript">var date = luxon.DateTime.fromObject({year: 2026, month: 2, day: 16, hour: 23, minute: 59, second: 59}, {zone: 'UTC-12',});$('#conf-hotel').countdown(date.toJSDate(), function(event) { $(this).html(event.strftime('%D days %H:%M:%S')); });</script>|
| Conference Program                        | March 23rd - March 26th, 2026   |<span id="conf-program"></span><script type="text/javascript">var date = luxon.DateTime.fromObject({year: 2026, month: 3, day: 23, hour: 0, minute: 0, second: 0}, {zone: 'UTC-12',});$('#conf-program').countdown(date.toJSDate(), function(event) { $(this).html(event.strftime('%D days %H:%M:%S')); });</script>|


## Conference Submission ([Proceedings Track]({{ site.baseurl }}/tracks/#proceedings-track--archival))

| Event                                                   | Date                           | Countdown                    |
|:--------------------------------------------------------|:-------------------------------|:-----------------------------|
| Submission Deadline                                     | December 12th, 2025              |<span id="proc-sub"></span><script type="text/javascript">var date = luxon.DateTime.fromObject({year: 2025, month: 12, day: 12, hour: 23, minute: 59, second: 59}, {zone: 'UTC-12',});$('#proc-sub').countdown(date.toJSDate(), function(event) { $(this).html(event.strftime('%D days %H:%M:%S')); });</script>|
| Review Deadline                                         | January 5th, 2026             |<span id="proc-review"></span><script type="text/javascript">var date = luxon.DateTime.fromObject({year: 2026, month: 1, day: 5, hour: 23, minute: 59, second: 59}, {zone: 'UTC-12',});$('#proc-review').countdown(date.toJSDate(), function(event) { $(this).html(event.strftime('%D days %H:%M:%S')); });</script>|
| Rebuttal Period                                         | January 8th–14th, 2026            |<span id="proc-rebuttal"></span><script type="text/javascript">var date = luxon.DateTime.fromObject({year: 2026, month: 1, day: 14, hour: 23, minute: 59, second: 59}, {zone: 'UTC-12',});$('#proc-rebuttal').countdown(date.toJSDate(), function(event) { $(this).html(event.strftime('%D days %H:%M:%S')); });</script>|
| Final Decisions Released                                | January 20th, 2026            |<span id="proc-decision"></span><script type="text/javascript">var date = luxon.DateTime.fromObject({year: 2026, month: 1, day: 20, hour: 23, minute: 59, second: 59}, {zone: 'UTC-12',});$('#proc-decision').countdown(date.toJSDate(), function(event) { $(this).html(event.strftime('%D days %H:%M:%S')); });</script>|


## Conference Submission ([Recent Spotlight Track]({{ site.baseurl }}/tracks/#recent-spotlight-track-non-archival))

| Event                     | Date                           | Countdown                    |
|:--------------------------|:-------------------------------|:-----------------------------|
| Submission Deadline       | January 15th, 2026             |<span id="wksp-sub"></span><script type="text/javascript">var date = luxon.DateTime.fromObject({year: 2026, month: 1, day: 15, hour: 23, minute: 59, second: 59}, {zone: 'UTC-12',});$('#wksp-sub').countdown(date.toJSDate(), function(event) { $(this).html(event.strftime('%D days %H:%M:%S')); });</script>|
| Final Decisions Released  | January 20th, 2026            |<span id="wksp-decision"></span><script type="text/javascript">var date = luxon.DateTime.fromObject({year: 2026, month: 1, day: 20, hour: 23, minute: 59, second: 59}, {zone: 'UTC-12',});$('#wksp-decision').countdown(date.toJSDate(), function(event) { $(this).html(event.strftime('%D days %H:%M:%S')); });</script>|

## [Tutorial Proposals]({{ site.baseurl }}/call_for_tutorials)

| Event                     | Date                           | Countdown                    |
|:--------------------------|:-------------------------------|:-----------------------------|
| Application Deadline      | December 10th, 2025              |<span id="tut-sub"></span><script type="text/javascript">var date = luxon.DateTime.fromObject({year: 2025, month: 12, day: 10, hour: 23, minute: 59, second: 59}, {zone: 'UTC-12',});$('#tut-sub').countdown(date.toJSDate(), function(event) { $(this).html(event.strftime('%D days %H:%M:%S')); });</script>|
| Decisions Released        | January 14th, 2026             |<span id="tut-decision"></span><script type="text/javascript">var date = luxon.DateTime.fromObject({year: 2026, month: 1, day: 14, hour: 23, minute: 59, second: 59}, {zone: 'UTC-12',});$('#tut-decision').countdown(date.toJSDate(), function(event) { $(this).html(event.strftime('%D days %H:%M:%S')); });</script>|


## [Rising Stars Award]({{ site.baseurl }}/rising_stars_guidelines)

| Event                     | Date                           | Countdown                    |
|:--------------------------|:-------------------------------|:-----------------------------|
| Application Deadline      | December 15th, 2025              |<span id="stars-sub"></span><script type="text/javascript">var date = luxon.DateTime.fromObject({year: 2025, month: 12, day: 15, hour: 23, minute: 59, second: 59}, {zone: 'UTC-12',});$('#stars-sub').countdown(date.toJSDate(), function(event) { $(this).html(event.strftime('%D days %H:%M:%S')); });</script>|
| Decisions Released        | January 21st, 2026             |<span id="stars-decision"></span><script type="text/javascript">var date = luxon.DateTime.fromObject({year: 2026, month: 1, day: 21, hour: 23, minute: 59, second: 59}, {zone: 'UTC-12',});$('#stars-decision').countdown(date.toJSDate(), function(event) { $(this).html(event.strftime('%D days %H:%M:%S')); });</script>|




