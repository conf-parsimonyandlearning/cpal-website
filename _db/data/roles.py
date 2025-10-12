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
class Individual:
    name: str
    role: str
    affiliation: str
    website: str = ""
    email: str = ""
    photo: str = ""
    id: int = field(default_factory=random_id)

    def get_fn(self) -> str:
        name = unidecode(self.name.lower()).split()
        fn = name[0]
        ln = name[-1]
        role = unidecode(self.role.lower()).split()
        if len(role) > 1:
            role_str = role[0][0] + role[1][0]
        else:
            role_str = role[0][0:2]
        return ln + "_" + fn + "_" + role_str + "_" + str(self.id)

    def export_jekyll(self, path, subdir=""):
        # This function prints the markdown files Jekyll/just-the-docs use to
        # make the website
        p = Path(path)
        org_fn = p / subdir / (self.get_fn() + ".md")

        to_dict = self.__dict__
        with org_fn.open(mode="w", encoding="utf-8") as f:
            f.write("---\n")
            for key in to_dict.keys():
                if key != "id" and key != "email":  # and key != 'day':
                    f.write(key + ": " + '"' + str(to_dict[key]) + '"' + "\n")
            f.write("---\n")


@dataclass(frozen=True)
class Organizer(Individual):
    def export_jekyll(self, path):
        super().export_jekyll(path=path, subdir="_organizers")


@dataclass(frozen=True)
class Speaker(Individual):
    # Talk parameters
    talk: str = ""
    abstract: str = ""
    bio: str = ""
    # Schedule parameters
    day: int = 0
    start: str = ""
    end: str = ""
    location: str = ""

    def export_jekyll(self, path):
        super().export_jekyll(path=path, subdir="_speakers")


@dataclass(frozen=True)
class RisingStar(Individual):
    talk: str = ""
    abstract: str = ""
    session: int = 1
    order: int = 1

    def export_jekyll(self, path):
        super().export_jekyll(path=path, subdir="_risingstars")


@dataclass(frozen=True)
class Tutorial(Individual):
    order: int = 1
    track: int = 1
    tutorial: str = ""
    abstract: str = ""

    def get_fn(self) -> str:
        name = unidecode(self.name.lower()).split()
        fn = name[0]
        ln = name[-1]
        return str(self.order) + "_" + ln + "_" + fn + "_" + str(self.id)

    def export_jekyll(self, path):
        super().export_jekyll(path=path, subdir="_tutorials")


if __name__ == "__main__":
    sam = Organizer(
        name="Sam Buchanan",
        role="Web Chair",
        email="sam@ttic.edu",
        website="https://sdbuchanan.com",
        affiliation="TTIC",
        photo="sdb.jpg",
    )
    print(sam.get_fn())
