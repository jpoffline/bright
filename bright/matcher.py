from typing import List
from .models import Member, Jobs, Job


def is_compatible(token: str, job: Job) -> bool:
    return (token in job.lower_location) or (token in job.lower_title)


def match_jobs_to_member(member: Member, jobs: Jobs) -> List[Job]:
    member_bio = member.lower_bio
    member_bio_tokens = member_bio.split(" ")

    negate_location = False
    if "outside" in member_bio:
        negate_location = True

    definite_location = False
    for token in member_bio_tokens:
        if token == "in":
            definite_location = True
            break
    print(definite_location)
    possible: List[Job] = []
    for job in jobs:
        for token in member_bio_tokens:
            if len(token) < 4:
                continue
            if token == job.lower_location and negate_location:
                continue
            if is_compatible(token, job):
                possible.append(job)
    return possible
