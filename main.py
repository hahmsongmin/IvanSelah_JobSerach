import os
import requests
from bs4 import BeautifulSoup


# user_input = input("검색키워드를 입력해주세요 : ")
job_url = "https://m.jobkorea.co.kr/Search/?ts_search=python&ord=ExactDesc&tabType=recruit&page_no=1"
jobKorea = requests.get(job_url)
soup = BeautifulSoup(jobKorea.content, 'html.parser')
pagination = soup.select_one("div.tplPagination ul")

pages = pagination.find_all('a')
pages_list = list()

for page in pages:
    pages_list.append(int(page.get_text()))

max_page = pages_list[-1]
