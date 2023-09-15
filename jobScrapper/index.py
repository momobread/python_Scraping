from extractors.indeed import extract_indeed_job
from extractors.wwr import extract_wwr_jobs

keyword = input("무슨 직업을 검색하고 싶나요?")


#둘다 리스트를 반환한다

indeed = extract_indeed_job(keyword)
# wwr = extract_wwr_jobs(keyword)
#jobs = extract_indeed_job(keyword)
# jobs = indeed+wwr


file = open(f"{keyword}.csv","w",encoding="utf-8")
file.write("Position,Company,Location,URL\n")


# for job in jobs:
for job in indeed:
    file.write(f"{job['link'],{job['company']},{job['location']},{job['position']}}\n")


file.close()







