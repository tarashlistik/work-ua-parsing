import requests
from bs4 import BeautifulSoup

url = "https://www.work.ua/jobs-it-data+scientist/?advs=1&experience=1"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('div', class_='card-hover')

for result in results:
    job_title = result.find('h2').text.strip()
    company_name = result.find('div', class_='add-top-xs').span.b.text
    job_location = result.find('div', class_='add-top-xs').text.strip()
    job_posted = result.find('span', class_='text-muted')
    print(job_title)