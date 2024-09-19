from .models import JobSuggestionsForMember


def report_matches_for_member(tgt, suggestions: JobSuggestionsForMember):
    tgt.write("Member: " + suggestions.member.name + "\n")
    tgt.write("Bio: " + suggestions.member.bio + "\n")
    tgt.write("Suggestions: \n")
    for i, js in enumerate(suggestions.job_suggestions):
        if i == 0:
            tgt.write("*")
        tgt.write(
            "  ("
            + str(js.score)
            + ") "
            + js.job.title
            + " in "
            + js.job.location
            + "\n"
        )
    tgt.write("\n")
