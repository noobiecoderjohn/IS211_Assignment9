#List of Nobel Memorial Prize laureates in Economic Sciences
import requests
from bs4 import BeautifulSoup

def scrape_nobel_laureates():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find("table", class_="wikitable")
    laureates_list = []
    headers = [header.text.strip() for header in table.find_all('th')]
    rows = table.find_all('tr')
    
    for row in rows:
        columns = row.find_all('td')
        if columns:
            columns = [column.text.strip() for column in columns]
            laureates_list.append(columns)

    df = pd.DataFrame(laureates_list, columns=headers)
    df = df.replace(r'\[\d+\]', '', regex=True)
    
    return df

if __name__ == "__main__":
    URL = 'https://en.wikipedia.org/wiki/List_of_Nobel_Memorial_Prize_laureates_in_Economic_Sciences'
    df_laureates = scrape_nobel_economics_laureates(URL)
    print(df_laureates.head())
