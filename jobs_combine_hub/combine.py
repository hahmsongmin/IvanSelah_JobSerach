from jobs_get.jobKorea import extract_jobKorea_jobs
from jobs_get.incruit import extract_incruit_jobs
from jobs_save.save import save_to_file

def get_jobs(keyword, pages):
    user_input = keyword
    search_pages = pages

    jobKorea_jobs = extract_jobKorea_jobs(user_input, search_pages)
    incruit_jobs = extract_incruit_jobs(user_input, search_pages)

    jobs = jobKorea_jobs + incruit_jobs
    return jobs

# save_to_file(jobs)