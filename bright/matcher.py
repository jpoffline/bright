from typing import List
from .models import Member, Jobs, Job


def is_compatible(token: str, job: Job) -> bool:
    return (token in job.lower_location) or (token in job.lower_title)


from dataclasses import dataclass


@dataclass
class MatcherParams:
    negate_location: bool = False
    definite_location: bool = False
    relocate_location: bool = False


def matcher_params_from_member(member: Member) -> MatcherParams:
    member_bio = member.lower_bio
    member_bio_tokens = member_bio.split(" ")

    matcher_params = MatcherParams()

    if "outside" in member_bio:
        matcher_params.negate_location = True
    else:
        for token in member_bio_tokens:
            if token == "in":
                matcher_params.definite_location = True
                break

    if "relocate to" in member_bio:
        matcher_params.negate_location = False
        matcher_params.definite_location = False
        matcher_params.relocate_location = True
    return matcher_params


def match_jobs_to_member(member: Member, jobs: Jobs) -> List[Job]:
    member_bio_tokens = member.lower_bio.split(" ")

    matcher_params = matcher_params_from_member(member)

    possible: List[Job] = []
    for job in jobs:
        for token in member_bio_tokens:
            if len(token) < 4:
                continue
            if token == job.lower_location and matcher_params.negate_location:
                continue
            if is_compatible(token, job):
                possible.append(job)
    return possible
