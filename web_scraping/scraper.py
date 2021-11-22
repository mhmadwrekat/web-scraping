import requests
import pprint
from bs4 import BeautifulSoup

def view():
    print('\n|------------------------------------------|')
#################################
URL = "https://www.bayt.com/en/jordan/jobs/python-jobs/"
res = requests.get(URL)
soup = BeautifulSoup(res.content, 'html.parser')
#################################
results_div = soup.find('div', id = 'results_inner_card')

pprint.pprint(results_div)

if __name__ == "__main__" :
    view()

    print(res)

    view()
    view()
#    print(soup)

    view()