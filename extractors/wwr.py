from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keywords):
    # 요청사이트
    base_url = "https://weworkremotely.com/remote-jobs/search?utf8="

    # 응답받기
    reponse = get(f"{base_url}{keywords}")
    if reponse.status_code != 200:
        print("Can't request website")
    else:  # 응답OK이면
        results = []
        soup = BeautifulSoup(reponse.text, "html.parser")  # 파싱
        jobs = soup.find_all('section', class_="jobs")  # find_all 하면 리스트로 저장
        print(len(jobs))
        for job_section in jobs:
            job_posts = job_section.find_all('li')
            job_posts.pop(-1)
            for post in job_posts:  # 모든 li > a > href > span : company,region 착지
                anchors = post.find_all('a')
                anchors = anchors[1]
                link = anchors['href']  # anchor는 딕셔너리이다
                company, kind, region = anchors.find_all('span', class_="company")
                title = anchors.find('span', class_='title')
                job_data = {
                    'link': f"https://weworkremotely.com{link}",
                    'company': company.string.replace(","," "),
                    'location': region.string.replace(","," "),
                    'position': title.string.replace(","," ")
                }
                results.append(job_data)
        return results
