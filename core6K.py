import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_table_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table')
    table = tables[0]
    rows = table.find_all('tr')
    headers = [th.get_text(strip=True) for th in rows[0].find_all(['th', 'td'])]
    data = []
    for row in rows[1:]:
        cells = row.find_all(['td', 'th'])
        data.append([cell.get_text(strip=True) for cell in cells])
    return pd.DataFrame(data, columns=headers)

def create_grid(df):
    x_coords = df["x-coordinate"]
    y_coords = df["y-coordinate"]
    characters = df["Character"]
    n = int(len(characters)/2)
    grid = [[" " for i in range(n)] for i in range(n)]
    for i, c in enumerate(characters):
        x = int(x_coords[i])
        y = int(y_coords[i])
        grid[x][y] = c
    for row in grid:
        row.reverse()
        print("".join(row))

def show_table_head(url):
    r = requests.get(url)
    # override encoding by real educated guess as provided by chardet
    r.encoding = r.apparent_encoding
    # access the data
    sample_html = r.text
    df = extract_table_from_html(sample_html)
    print(df.head())

def save_to_csv(url, filename):
    r = requests.get(url)
    # override encoding by real educated guess as provided by chardet
    r.encoding = r.apparent_encoding
    # access the data
    sample_html = r.text
    df = extract_table_from_html(sample_html)
    print(df.head())
    df.to_csv(filename)


if __name__ == "__main__":
    #print(sample_html[0:10], sample_html[-10::])
    url = input("Please input a URL:")
    filename = input("Please input a file name with .csv extension:")
    #show_table_head(url)
    save_to_csv(url, filename)

