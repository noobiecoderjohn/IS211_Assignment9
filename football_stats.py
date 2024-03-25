#List of NBA champions

import requests
from bs4 import BeautifulSoup

def nba_champions():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find("table", class_="wikitable")
    nba_list = []
    headers = [header.text.strip() for header in table.find_all('th')]
    rows = table.find_all('tr')
    
    for row in rows:
        columns = row.find_all('td')
        if columns:
            columns = [column.text.strip() for column in columns]
            nba_list.append(columns)

    df = pd.DataFrame(nba_list, columns=headers)
    df = df.replace(r'\[\d+\]', '', regex=True)
    
    return df

if __name__ == "__main__":
    URL = 'https://en.wikipedia.org/wiki/List_of_NBA_champions'
    df_nba = nba_champions(URL)
    print(df_nba.head())
