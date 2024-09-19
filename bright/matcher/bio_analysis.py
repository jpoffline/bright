from ..models import Member
from .models import BioAnalysis


# analyse_bio will return tokens and flags deduced from a Member's
# bio, in order to allow job-matching.
def analyse_bio(member: Member) -> BioAnalysis:
    member_bio = member.lower_bio
    member_bio_tokens = member_bio.split(" ")

    bio_analysis = BioAnalysis()

    if "outside" in member_bio:
        bio_analysis.negate_location = True
    else:
        for token in member_bio_tokens:
            if token == "in":
                bio_analysis.definite_location = True
                break

    if "relocate to" in member_bio:
        bio_analysis.negate_location = False
        bio_analysis.definite_location = False
        bio_analysis.relocate_location = True
    return bio_analysis
