
from bs4 import BeautifulSoup
import requests
import re

URL = "http://www.footballlocks.com/nfl_point_spreads.shtml"


def nfl_spreads():
    html_content = requests.get(URL).text
    soup = BeautifulSoup(html_content, "lxml")
    table = soup.find("table", attrs={"cols": "4"})
    data = table.find_all("tr")
    headings = []
    for td in data[1].find_all("td"):
        headings.append(td)
    print(re.sub("<td>|</td>", "",
                 "Favorite is {}, Underdog is {}, Spread is {}".format(
                     headings[1],
                     headings[3],
                     headings[2])))


if __name__ == '__main__':
    nfl_spreads()
