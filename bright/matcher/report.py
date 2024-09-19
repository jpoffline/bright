from .models import JobSuggestionsForMember
from typing import Protocol


class Writer(Protocol):
    def write(self, message): ...


# report_matches_for_member will provide a report written to the target Writer.
def report_matches_for_member(writer: Writer, suggestions: JobSuggestionsForMember):
    writer.write("Member: " + suggestions.member.name + "\n")
    writer.write("Bio: " + suggestions.member.bio + "\n")
    writer.write("Suggestions: \n")
    for i, js in enumerate(suggestions.job_suggestions):
        if i == 0:
            writer.write("*")
        writer.write(
            "  ("
            + str(js.score)
            + ") "
            + js.job.title
            + " in "
            + js.job.location
            + "\n"
        )
    writer.write("\n")
