import requests
from bs4 import BeautifulSoup

print("Script started")

URL = "https://www.python.org/jobs/"
response = requests.get(URL, timeout=1)  # Add timeout

soup = BeautifulSoup(response.content, "html.parser")
results = soup.find("div", class_="row")

ol_list = results.find("ol", class_="list-recent-jobs list-row-container menu")
li_list = ol_list.find_all("li")

usa_jobs = [
    job_card for job_card in li_list if job_card.find("span", class_="listing-location") and "united states" in job_card.find("span", class_="listing-location").text.strip().lower()]

for job_card in usa_jobs:
    title_span = job_card.find("span", class_="listing-company-name")
    title = title_span.find("a") if title_span else None
    
    company_span = job_card.find("span", class_="listing-company-name")
    company = company_span.find("a") if company_span else None
    
    location_span = job_card.find("span", class_="listing-location")
    location = location_span.find("a") if location_span else None
    
    link_url = title["href"] if title else None
    
    if title and company and location:
        print(title.text.strip())
        print(company.text.strip())
        print(location.text.strip())
        print(f"Apply Here: {link_url}\n")