import requests
import pprint
from bs4 import BeautifulSoup
import json

def view():
    print('_'*44)
#################################
URL = "https://www.bayt.com/en/jordan/jobs/python-jobs/"
res = requests.get(URL)
soup = BeautifulSoup(res.content, 'html.parser')
#################################
results_div = soup.find('div', id = 'results_inner_card')
results_ul = results_div.find('ul', class_='media-list')
# pprint.pprint(results_div)
jobs_list = results_ul.find_all('li')



all_job_obj = []
for job in jobs_list :
    job_dict = {'title' : '', 'company_name' : ''}
    title_before_strip = job.find('h2')
    company_before_strip = job.find('b', class_='p10r')
    if title_before_strip :
        title = title_before_strip.get_text().strip()
        job_dict['title'] = title 
        company_name = company_before_strip.get_text().strip()
        job_dict['company_name'] = company_name 
        all_job_obj.append(job_dict)

if __name__ == "__main__" :
    view()
    print(res)
    view()
# Print Title For 1 Job :
    print(jobs_list[1].find('h2').get_text())
    view()
    print(type(soup))
    view()
    print(results_ul)
    view()
    print(len(jobs_list))
    view()
    print('a')




    view()
    print(all_job_obj)
    view()

with open('all_jobs.json', 'w') as f :
    content = json.dumps(all_job_obj)
    f.write(content)


