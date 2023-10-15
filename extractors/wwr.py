from bs4 import BeautifulSoup
import requests


def extract_wwr_jobs(keyword):
    url = f"https://weworkremotely.com/remote-jobs/search?search_uuid=&term={keyword}&button=&sort=any_time"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    results = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all("li", class_="feature")

        for job in jobs:
            company = job.find("span", class_="company")
            position = job.find("span", class_="title")
            location = job.find("span", class_="region company")
            link = job.find_all("a")[1].attrs['href']
            if company:
                company = company.string.strip()
            if position:
                position = position.string.strip()
            if location:
                location = location.string.strip()
            if link:
                link = "https://weworkremotely.com" + link
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
