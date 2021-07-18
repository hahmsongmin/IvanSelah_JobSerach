import os, re
import requests
from bs4 import BeautifulSoup

def extract_job(result):

    if result.select_one("h3 > a") is None:
        company = result.select_one("h3").get_text().replace("관심기업등록", "")
    else:
        company = result.select_one("h3 > a").get_text()

    title = result.find("span", {"class": "rcrtTitle"}).get_text()

    location_work = result.select_one("p.etc span").get_text().split("|")[1]
    location = location_work.replace(">", " ").strip()

    job_link_work = result.select_one("span.rcrtTitle > a")["href"]
    job_link = re.sub('[^0-9]', "", job_link_work)

    return {'회사': company, '채용': title, '지역': location, "링크": f"https://job.incruit.com/jobdb_info/jobpost.asp?job={job_link}"}


def extract_incruit_jobs(keyword, pagesNum):
    jobs = list()
    URL = f"https://search.incruit.com/list/search.asp?col=job&il=y&kw={keyword}"
    count = 0
    for page in range(pagesNum):
        count += 1
        if page == 0:
            result = requests.get(f"{URL}")
        else:
            result = requests.get(f"{URL}&startno={page*20}")
        soup = BeautifulSoup(result.content, 'html.parser')
        results = soup.select("ul.litype01 li")
        if results:
            for result in results:
                job = extract_job(result)
                jobs.append(job)
        else:
            print("검색할 페이지가 없습니다.")
    print(f"✅InCruit Scrapping 🚀 {count} page")
    return jobs
