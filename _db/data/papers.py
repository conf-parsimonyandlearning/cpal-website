#!/usr/bin/env python
# -*- coding: utf-8 -*-

# imports
import dataclasses
from collections.abc import Callable
from pathlib import Path
from typing import Dict, Literal, Optional, Tuple, cast

import openreview

"""
Functions for getting OpenReview data about accepted papers

Requires openreview-py client
https://docs.openreview.net/getting-started/using-the-api/installing-and-instantiating-the-python-client

TODO: requests.py versioning issues with openreview-py
"""


def get_accepted_papers(venue_str=""):
    # Load credentials
    with open("credentials.txt", "r") as file:
        user = file.readline().strip()
        passwd = file.readline().strip()

    # API V2
    client = openreview.api.OpenReviewClient(
        baseurl="https://api2.openreview.net", username=user, password=passwd
    )
    venue_group = client.get_group(venue_str)
    submission_name = venue_group.content["submission_name"]["value"]
    # submissions = client.get_all_notes(invitation=f'CPAL.cc/2024/Recent_Spotlight_Track/-/{submission_name}')
    submissions = client.get_all_notes(content={"venueid": venue_str})

    # submissions is a list of notes
    # https://openreview-py.readthedocs.io/en/latest/api.html#openreview.api.Note
    return submissions


if __name__ == "__main__":
    papers = get_accepted_papers(venue_str="CPAL.cc/2025/Proceedings_Track")
    print(papers[10].to_json())
    print(papers[10].to_json()['content']['venue']['value'].split(' ')[-1].lower())
