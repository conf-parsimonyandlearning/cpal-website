#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

# imports
from dataclasses import dataclass, field
from pathlib import Path

from unidecode import unidecode

# global-type variables
seed = 100101010101


def random_id():
    random.seed(a=seed)
    return random.randrange(10**6)


# Base class, common fields
@dataclass(frozen=True)
class Event:
    name: str
    event_class: str
    day: int
    start: str
    end: str
    location: str = ""
    talk: str = ""
    id: int = field(default_factory=random_id)

    def get_fn(self) -> str:
        name = unidecode(self.name.lower()).split()
        fn = name[0]
        ln = name[-1]
        role = unidecode(self.event_class.lower()).split()
        if len(role) > 1:
            role_str = role[0][0] + role[1][0]
        else:
            role_str = role[0][0:2]
        return ln + "_" + fn + "_" + role_str + "_" + str(self.id)

    def export_jekyll(self, path, subdir=""):
        # This function prints the markdown files Jekyll/just-the-docs use to
        # make the website
        # We won't normally use this for events, though
        p = Path(path)
        org_fn = p / subdir / (self.get_fn() + ".md")

        to_dict = self.__dict__
        with org_fn.open(mode="w", encoding="utf-8") as f:
            f.write("---\n")
            for key in to_dict.keys():
                if key != "id" and key != "email":
                    f.write(key + ": " + to_dict[key] + "\n")
            f.write("---\n")

    def dump_calendar(self):
        # Dump the event content as a string, formatted for calendar
        # (i.e. just-the-class formatting, for a YAML header)
        out_str = ""
        if self.event_class == "keynote":
            out_str += f'name: \'<a href="/speakers/#{self.name.lower().replace(" ", "-").replace("+", "")}">{self.name}</a>\'\n'
        elif self.event_class == "oral":
            out_str += f'name: \'<a href="/orals/#{self.name.lower().replace(" ", "-").replace("+", "")}">{self.name}</a>\'\n'
        elif self.event_class == "poster":
            out_str += f'name: \'<a href="/posters/#{self.name.lower().replace(" ", "-").replace("+", "")}">{self.name}</a>\'\n'
        elif self.event_class == "rising":
            out_str += f'name: \'<a href="/rising_stars_presentations/#{self.name.lower().replace(" ", "-").replace("+", "")}">{self.name}</a>\'\n'
        else:
            out_str += f"name: '{self.name}'\n"
        out_str += f'class: "{self.event_class}"\n'
        out_str += f'start: "{self.start}"\n'
        out_str += f'end: "{self.end}"\n'
        # if self.location == "TBA":
        #     # treat this as a catch-all, we just define the location based on the day
        #     if self.day == 1:
        #         out_str += f'location: <a href="/venue/#day-1-venue-rayson-huang-theatre-hku">Rayson Huang Theatre</a>\n'
        #     else:
        #         out_str += f'location: <a href="/venue/#days-24-venue-lecture-hall-ii-cpd-lg07-10-lg-centennial-campus-hku">Lee Shau Kee Lecture Ctr.</a>\n'
        # else:
        #     out_str += f'location: {self.location}\n'
        out_str += f'location: {self.location}\n'
        # out_str += f'location: "{self.location}"\n'
        if self.event_class == "keynote":
            out_str += f'talk: "{self.talk}"\n'
        return out_str

    def dump_schedule(self):
        # Dump the event content as a string, formatted for plaintext schedule
        # (i.e. our custom formatting, for use with just-the-docs)
        pass
