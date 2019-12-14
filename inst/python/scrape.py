from urllib import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import sys

year = raw_input("Enter desired year to scrape data:\n ")

try:
    year = int(year)
except ValueError:
    year = 2019
    print("Input error: Defaulting to 2019...")

urls = {
  'pergame': "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html",
  'per36': "https://www.basketball-reference.com/leagues/NBA_{}_per_minute.html",
  'per100': "https://www.basketball-reference.com/leagues/NBA_{}_per_poss.html",
  'totals' : "https://www.basketball-reference.com/leagues/NBA_{}_totals.html",
  'advanced': "https://www.basketball-reference.com/leagues/NBA_{}_advanced.html"
}

url = urls['advanced'].format(year)
html = urlopen(url)
soup = BeautifulSoup(html, features='lxml')

headers = [th.getText() for th in soup.findAll('tr', limit=2)]
headers = headers[0].split("\n")
headers = headers[2:-1]

rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
                        for i in range(len(rows))]

stats = pd.DataFrame(player_stats, columns = headers)
print(stats.head(10))

# TODO:
# WRITE UP A PANDAS INDEXING TUTORIAL FOR GRABBING NBA DATA
# Help you (re)learn pandas and would be nice to learn markdown/tutorial making
print("\n\nData is now imported as a pandas DataFrame object \
      named \'stats\', happy hunting!")
print("\nIndexing: \
      https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html")
print("API reference: \
      https://pandas.pydata.org/pandas-docs/stable/reference/index.html")
print("To see column names, run: \'stats.columns\'")
print(stats.columns)
print("E.g. If you wanted the first 10 players block numbers, \
      run \'stats[['Player', 'BLK']][1:10]\'")
print(stats[['Player', 'BLK']][1:10])

# Gets Lou Williams numbers for 2019
player = 'Lou Williams'
print(stats[stats['Player'] == player])


# TODO: Scrape tool to dump x-year to a .csv or .Rds file
def dump_to_csv(df, file = 'nba-data.csv'):
  df.to_csv(file, encoding = "utf-8")

file = "nba-{}-data.csv".format(year)  
dump_to_csv(stats, file)


