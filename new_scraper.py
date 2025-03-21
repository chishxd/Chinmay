import requests
from bs4 import BeautifulSoup

URL = "https://pythonjobs.github.io/"
try:
    # Fetch the webpage
    page = requests.get(URL, timeout=1)
    page.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"An Error Occurred: {e}")
    exit()

# Parse the HTML content
soup = BeautifulSoup(page.content, "html.parser")

# Find the section containing job listings
job_results = soup.find("section", class_="job_list")
job_listings = job_results.find_all("div", class_="job")

# Iterate through each job listing
for job_result in job_listings:
    # Extract the job title
    title_tag = job_result.find("h1")
    title = title_tag.text.strip() if title_tag else "Unable to access Title"

    # Extract job details
    detail_tag = job_result.find("p", class_="detail")
    details = detail_tag.text.strip() if detail_tag else "No Details"

    # Extract the location
    info_span = job_result.find_all("span", class_="info")
    span_texts = [span.text.strip() for span in info_span]  # Extract text from each span

    #Extract Apply Button
    apply = job_result.find("a")["href"] if job_result.find("a")["href"] else "No Application"
    # Print the extracted information
    if "Remote" in span_texts:
        print(f"\nName: {title}")
        print(f"Details: {details}")
        Information = ["Location", "Date", "Tenure", "Company"]
        for i in range(len(span_texts)):
            print(f"{Information[i]} : {span_texts[i]}")
        # print(f"Date: {date.text.strip()}")
        print(f"Read More: https://pythonjobs.github.io{apply}")
        print()
