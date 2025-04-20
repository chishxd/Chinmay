import requests
from bs4 import BeautifulSoup

print("Script started\n")

URL = "https://www.python.org/jobs/"
try:
    response = requests.get(URL, timeout=1)  # Add timeout
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    exit()

soup = BeautifulSoup(response.content, "html.parser")
results = soup.find("div", class_="row")

if not results:
    print("Couldn't Find Any Jobs Now")
    exit()

jobs_list = results.find("ol", class_="list-recent-jobs list-row-container menu").find_all("li")


# usa_jobs = [
#     job_card for job_card in li_list if job_card.find("span", class_="listing-location") and "united states" in job_card.find("span", class_="listing-location").text.strip().lower()]

for job_card in jobs_list:
    title_span = job_card.find("span", class_="listing-company-name").find("a") if job_card.find("span", class_="listing-company-name").find("a") else "Unable to access Title"
    # title = title_span.find("a") if title_span else None
    
    company_span = job_card.find("span", class_="listing-company-name").find("a") if job_card.find("span", class_="listing-company-name").find("a") else "Couldn't find Company"
    # company = company_span.find("a") if company_span else None
    
    location_span = job_card.find("span", class_="listing-location").find("a") if job_card.find("span", class_="listing-location").find("a") else "Unable to show location"
    # location = location_span.find("a") if location_span else None
    
    link_url = title_span["href"] if title_span else None
    
    if not (title_span and company_span and location_span):
        continue
    location_text = location_span.text.strip().lower()

    if "united states" not in location_text:
        continue
    print(title_span.text.strip())
    print(company_span.text.strip())
    print(location_span.text.strip())
    print(f"Apply Here: https://www.python.org{link_url}\n")
