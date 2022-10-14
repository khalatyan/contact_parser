import requests
from bs4 import BeautifulSoup


def get_contacts(inn):
    url = f"https://e-ecolog.ru/entity/{int(inn)}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    emails_res = []
    tels_res = []
    sites_res = []

    for email in soup.find_all('span', itemprop='email'):
        emails_res.append(email.get_text())

    for tel in soup.find_all('span', itemprop='telephone'):
        tels_res.append(tel.get_text())

    for site in soup.find_all('span', itemprop='website'):
        sites_res.append(site.get_text())

    return ";".join(emails_res), ";".join(tels_res), ";".join(sites_res)

