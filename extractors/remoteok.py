from bs4 import BeautifulSoup
import requests


def extract_remoteok_jobs(keyword):
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    results = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all("tr", class_="job")
        for job in jobs:
            company = job.find("h3", itemprop="name")
            position = job.find("h2", itemprop="title")
            location = job.find("div", class_="location")
            link = job.find("a", itemprop="url").attrs['href'].strip()
            if company:
                company = company.string.strip()
            if position:
                position = position.string.strip()
            if location:
                location = location.string.strip()
            if link:
                link = "https://remoteok.com/" + link
            if company and position and location and link:
                job = {
                    'company': company,
                    'position': position,
                    'location': location,
                    'link': link
                }
                results.append(job)
    else:
        print("Can't get jobs.")
    return results
