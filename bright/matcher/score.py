from bright.utils import count_same_tokens
from ..models import Member, Job


def calc_score(job: Job, member: Member) -> int:
    return count_same_tokens(job.title + " " + job.location, member.bio)
