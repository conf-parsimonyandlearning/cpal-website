#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import random
import textwrap

# imports
from dataclasses import dataclass, field, replace
from pathlib import Path

from unidecode import unidecode

from event import Event

# global-type variables
seed = 100101010101
days_of_week = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def random_id():
    random.seed(a=seed)
    return random.randrange(10**6)


# Base class, common fields
# Limitations of this calendar class: very lazy (hard-coded) date support only
@dataclass(frozen=True)
class Calendar:
    name: str
    start_day: int  # corresponds to day 1 (numeric day of month)
    start_day_of_week: str  # corresponds to day 1
    start_month: str  # used for formatting; doesn't support month-crossing...
    early_time: str  # earliest time to show on the schedule (see event.py formatting)
    late_time: str  # latest time to show on the schedule events: list = field(default_factory=list)
    events: list = field(default_factory=list)
    _calendar: dict = field(default_factory=dict)
    id: int = field(default_factory=random_id)

    # value checking
    def __post_init__(self):
        assert self.start_day_of_week.lower() in [s.lower() for s in days_of_week]

    # Add an event to the calendar
    def add_event(self, event: Event):
        self.events.append(event)

    # Helper to convert a time string (just-the-class format) to datetime
    def __convert_time(self, str):
        return datetime.datetime.strptime(str, "%I:%M %p")

    # We populate the calendar dict and validate it (used for exporting too)
    def validate_calendar(self):
        # > The calendar dict is a dict of dicts
        # > Top-level keys are indexed by event day
        # > Next level keys are indexed by event start time
        # A calendar is invalid if two events overlap in duration.
        # (we don't support concurrent events, at this resolution)
        self._calendar.clear()
        # Loop over events
        for event in self.events:
            day = event.day
            if day not in self._calendar:
                self._calendar[day] = {}

            # check for a key conflict
            if event.start in self._calendar[day]:
                raise ValueError(
                    f"Cannot add event {event.name}: time conflict with"
                    + f"{self._calendar[day][event.start].name}"
                )
            # add the new event
            start_time = event.start
            self._calendar[day][start_time] = replace(event)
            # check that we don't run into the start time of the next event
            end_time = event.end
            day_keys = self._calendar[day].keys()
            # the logged events starting before this one ends
            earlier_events = [
                self.__convert_time(time) < self.__convert_time(end_time)
                for time in day_keys
            ]
            # the logged events starting after this one starts
            later_events = [
                self.__convert_time(time) > self.__convert_time(start_time)
                for time in day_keys
            ]
            invalid_events = list(map(lambda x, y: x & y, earlier_events, later_events))
            for index, value in enumerate(invalid_events):
                if value != 0:
                    raise ValueError(
                        f"Cannot add event {event.name}: time conflict with"
                        + f"{self._calendar[day][day_keys[index]].name} ("
                        + f"{event.name} ends at {end_time} on day {day} "
                        + f"but {self._calendar[day][day_keys[index]].name} "
                        + f"starts at {self._calendar[day][day_keys[index]].start})"
                    )
            # If we didn't trigger any errors, we added this event successfully!

    def get_fn(self) -> str:
        name = unidecode(self.name.lower()).split()
        fn = name[0]
        return fn

    def export_jekyll(self, path, subdir=""):
        # This function prints the YAML file Jekyll/just-the-docs use to
        # make the website
        p = Path(path)
        org_fn = p / subdir / (self.get_fn() + ".md")

        to_dict = self.__dict__
        with org_fn.open(mode="w", encoding="utf-8") as f:
            f.write("---\n")
            for key in to_dict.keys():
                if key != "id" and key != "email":
                    f.write(key + ": " + to_dict[key] + "\n")
            f.write("---\n")

    def export_calendar(self, path, subdir="_calendars"):
        # This function prints the YAML file Jekyll/just-the-class use to
        # make the calendar for the website
        p = Path(path)
        org_fn = p / subdir / (self.get_fn() + ".md")

        # First prelim: create time discretization to print at the start
        start_time = self.__convert_time(self.early_time)
        stop_time = self.__convert_time(self.late_time)
        interval = datetime.timedelta(minutes=30)
        discretized_times = []
        current_time = start_time
        while current_time <= stop_time:
            discretized_times.append(current_time.strftime("%I:%M %p"))
            current_time += interval

        # Second prelim: convert the start date to an offset index
        scrubbed_start_dow = self.start_day_of_week.lower().replace(" ", "")
        day_index = len(days_of_week)
        for index, string in enumerate(days_of_week):
            if scrubbed_start_dow == string.lower():
                day_index = index

        # Write out file
        with org_fn.open(mode="w", encoding="utf-8") as f:
            f.write("---\n")
            # timeline
            f.write("timeline:\n")
            for string in discretized_times:
                f.write("  - " + string + "\n")
            # Dump events
            f.write("calendar:\n")
            # loop over days
            day_keys = sorted(self._calendar.keys())
            for day in day_keys:
                day_dict = self._calendar[day]
                f.write(
                    "  - "
                    + f"name: Day {day} "
                    + f"({self.start_month} {self.start_day + day - 1})<br>"
                    + f"{days_of_week[(day_index + day - 1) % 7]}\n"
                )
                f.write("    events:\n")
                # NOTE: subsequent needs 6 space indent + 2 for each line
                # Sort the events based on time of occurrence
                # (we don't need it here, as jekyll will parse this for us...
                #  but we need it for the plaintext dump, so just do it here)
                event_keys = sorted(day_dict.keys(), key=self.__convert_time)
                for event_key in event_keys:
                    # sorted event dump
                    event = day_dict[event_key]
                    event_str = event.dump_calendar()
                    event_str_wrap = textwrap.indent(event_str, "  ")
                    event_str_wrap = "-" + event_str_wrap[1:]
                    event_str_indent = textwrap.indent(event_str_wrap, "      ")
                    f.write(event_str_indent)
            f.write("---\n")
