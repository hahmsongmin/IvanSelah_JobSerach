from jobKorea import extract_jobKorea_jobs
from incruit import extract_incruit_jobs

user_input = input("검색키워드를 입력해주세요 : ")
search_pages = int(input("검색할페이지수를 입력해주세요 : "))

jobKorea_jobs = extract_jobKorea_jobs(user_input, search_pages)
incruit_jobs = extract_incruit_jobs(user_input, search_pages)

jobs = jobKorea_jobs + incruit_jobs
print(jobs)