import os, re
import requests
from bs4 import BeautifulSoup

def extract_job(result):

    company_work = result.find("div", class_="company").get_text()
    company = company_work.strip()

    title_work = result.select_one("div.text h3").get_text()
    title = re.sub('[0-9]', '', title_work).replace(".", "").strip()

    location= result.select_one("ul.list-border > li").string

    job_link = result["href"]
    return {'회사': company, '채용': title, '지역': location, "링크": f"https://m.jobkorea.co.kr{job_link}"}


def extract_jobKorea_jobs(keyword, pagesNum):
    jobs = list()
    URL = f"https://m.jobkorea.co.kr/Search/?ts_search={keyword}&ord=ExactDesc&tabType=recruit"
    count = 0
    for page in range(pagesNum):
        count += 1
        result = requests.get(f"{URL}&page_no={page + 1}")
        soup = BeautifulSoup(result.content, 'html.parser')
        results = soup.find_all("a", {"class": "clearfix"})
        if results:
            for result in results:
                job = extract_job(result)
                jobs.append(job)
        else:
            print("검색할 페이지가 없습니다.")
    print(f"✅JobKorea Scrapping 🚀 {count} page")
    return jobs


