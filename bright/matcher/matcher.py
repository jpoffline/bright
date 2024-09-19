from ..models import Member, Jobs, Job
from .models import JobSuggestionsForMember
from .bio_analysis import analyse_bio
from .models import BioAnalysis


def is_compatible(member_bio_token: str, job: Job, bio_analysis: BioAnalysis) -> bool:
    if member_bio_token == job.lower_location and bio_analysis.negate_location:
        return False
    return (member_bio_token in job.lower_location) or (
        member_bio_token in job.lower_title
    )


# match_jobs_to_member will create a list of job suggestions for the provided member.
def match_jobs_to_member(member: Member, jobs: Jobs) -> JobSuggestionsForMember:
    # Turn a member bio into tokens; the tokens are lower-case words in the bio.
    member_bio_tokens = member.lower_bio.split(" ")

    bio_analysis = analyse_bio(member)

    possible = JobSuggestionsForMember(member)
    for job in jobs:
        add_job = False
        for token in member_bio_tokens:
            if len(token) < 4:
                continue
            if is_compatible(token, job, bio_analysis):
                add_job = True
        if add_job:
            possible.add_suggestion(job)
    possible.finish()
    return possible
