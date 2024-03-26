#List of NBA champions

import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://en.wikipedia.org/wiki/List_of_NBA_champions"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    tables = soup.find_all("table", class_="wikitable")

    for i, table in enumerate(tables):
        df = pd.read_html(str(table))[0]  # Use [0] to get the first table        
        print(f"Table {i + 1}:")
        print(df)
        print("\n")
else:
    print("Failed to retrieve the page.")
