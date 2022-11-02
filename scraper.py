import requests
from bs4 import BeautifulSoup

# URL we needed
url = 'https://en.wikipedia.org/wiki/History_of_Mexico'

#  Create function to get citations needed count

def get_citations_needed_count(url):

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    citations = soup.find_all('a', title='Wikipedia:Citation needed')
    count = len(citations)
    print(count) 

#  Create function to get citations needed report
def get_citations_needed_report(url):

    all=[]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    paragraph= soup.find_all('p')
    for paragraph in paragraph:
        if paragraph.find('a', title='Wikipedia:Citation needed'):
            paragraph=paragraph.text.strip().replace('[citation needed]','')
            all.append(paragraph)
    print(all)

# to show the final result

if __name__ == '__main__':
    get_citations_needed_count(url)
    get_citations_needed_report(url)