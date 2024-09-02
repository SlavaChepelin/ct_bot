from bs4 import BeautifulSoup
import csv
import requests

html = requests.get('https://docs.google.com/spreadsheets/d/1dy_i_s5Cn4DEZnl87_j5YdkAL4Yf1Gq9RTe_wVwoHzk/pubhtml').text
soup = BeautifulSoup(html, "lxml")
tables = soup.find_all("table")


with open("ans.csv", "w") as f:
    wr = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    wr.writerows([[td.text for td in row.find_all("td")] for row in tables[0].find_all("tr")])
with open('ans.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))