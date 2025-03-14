import requests
from bs4 import BeautifulSoup

print("Script started")

URL = "https://realpython.github.io/fake-jobs/"
response = requests.get(URL, timeout=1)  # Add timeout

soup = BeautifulSoup(response.content, "html.parser")
results = soup.find(id = "ResultsContainer")

job_cards = results.find_all("div", class_= "card-content")

python_jobs = results.find_all("h2", string = lambda text: "python" in text.lower())

python_job_cards = [h2_elements.parent.parent.parent for h2_elements in python_jobs]

for job_card in python_job_cards:
    title = job_card.find("h2", class_= "title")
    company = job_card.find("h3", class_ = "company")
    location = job_card.find("p", class_ = "location")
    link_url = job_card.find_all('a')[1]["href"]
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print(f"Apply Here: {link_url}\n")
    print()