from dataclasses import dataclass, field
from ..models import Member, Job
from typing import List


from .score import calc_score


@dataclass
class BioAnalysis:
    negate_location: bool = False
    definite_location: bool = False
    relocate_location: bool = False


@dataclass
class JobSuggestion:
    job: Job
    score: int


@dataclass
class JobSuggestionsForMember:
    member: Member
    job_suggestions: List[JobSuggestion] = field(default_factory=list)

    def add_suggestion(self, job: Job):
        suggestion = JobSuggestion(job=job, score=calc_score(job, self.member))
        self.job_suggestions.append(suggestion)

    def finish(self):
        self.job_suggestions.sort(key=lambda x: x.score, reverse=True)
