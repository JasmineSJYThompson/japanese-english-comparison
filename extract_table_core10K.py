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

def show_head(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    sample_html = r.text
    df = extract_table_from_html(sample_html)
    print(df.head())

def save_to_csv(url, csv_name):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    sample_html = r.text
    df = extract_table_from_html(sample_html)
    df.to_csv(csv_name)

if __name__ == "__main__":
    #print(sample_html[0:10], sample_html[-10::])
    url = input("Please input a URL: ")
    csv_name = input("Please input a CSV name: ")
    save_to_csv(url, csv_name)
