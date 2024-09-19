from bright.data import load_jobs_data, load_members_data
from bright.matcher.matcher import match_jobs_to_member
from bright.matcher.report import report_matches_for_member
import sys
from config import DATA_SOURCE


def run():

    jobs = load_jobs_data(DATA_SOURCE)
    members = load_members_data(DATA_SOURCE)

    for member in members:
        jobs_for_member = match_jobs_to_member(member, jobs)
        report_matches_for_member(sys.stdout, jobs_for_member)


if __name__ == "__main__":
    run()
