import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_country_data():
    url = "https://www.scrapethissite.com/pages/simple/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    countries = []

    for country in soup.find_all("div", class_="country"):
        name = country.find("h3", class_="country-name").text.strip()
        capital = country.find("span", class_="country-capital").text.strip()
        population = country.find("span", class_="country-population").text.strip()
        area = country.find("span", class_="country-area").text.strip()

        countries.append({
            "Name": name,
            "Capital": capital,
            "Population": population,
            "Area": area
        })

    return countries


def save_to_csv(countries):
    df = pd.DataFrame(countries)
    df.to_csv("countries.csv", index=False)
    print("Data saved successfully to countries.csv")


country_data = scrape_country_data()
save_to_csv(country_data)

print(country_data[:5])