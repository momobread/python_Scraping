from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_page_count(keyword):
    # 요청부분
    options = Options()
    print(options)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options)
    browser.get(f"https://kr.indeed.com/jobs?q={keyword}&limit=50")

    soup = BeautifulSoup(browser.page_source,"html.parser")
    pagination = soup.find('ul',class_="css-zu9cdh eu4oa1w0")
    if pagination == None: #ul이없다 다음페이지가 없다(>버튼)
        return 1
    #ul 안의 li의 갯수 / recursive=False를 쓰면 해당 태그만 가져온다
    pages = pagination.find_all('li',recursive=False)
    count = len(pages)
    if count >=5: #페이지가 5개 이상이다 = >버튼이 있다
        return 5
    else:
        return count



def extract_indeed_job(keyword):
    #keyword의 페이지 갯수를 구한다
    pages = get_page_count(keyword)
    results = []
    count =0
    #page의 갯수만큼 반복문을 돌린다
    for page in range(pages):
        count +=page
        #요청부분
        options = Options()
        print(options)
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        browser = webdriver.Chrome(options=options)
        a=browser.get(f"https://kr.indeed.com/jobs?q={keyword}&start={page*10}&limit=50")
        print(a)
        print("//////")
        #html파싱
        soup = BeautifulSoup(browser.page_source, "html.parser")

        job_list = soup.find("ul",class_="css-zu9cdh eu4oa1w0")
        jobs = job_list.find_all('li',recursive=False)

        for job in jobs:
            zone = job.find("div",class_="mosaic-zone")
            print(zone)
            if zone == None:
                h2 = job.find("h2",class_="jobTitle")
                anchor = job.select_one("h2 a") #이렇게하면 리스트의 a가 아니라 a만 가져오게 된다
                title = anchor['aria-label']
                link = anchor['href']
                print(title,link)
                company = job.find('span',class_="companyName")
                location = job.find('div',class_="companyLocation")
                job_data = {
                    'link' :f"https://kr.indeed.com{link}",
                    'company': company.string,
                    'location' : location.string,
                    'position' : title
                }
                results.append(job_data)
        print(count,"page 입니다")
        print("////////")
    return results


# jobs = extract_indeed_job('python')
# print(jobs)


# while (True):
#     pass




