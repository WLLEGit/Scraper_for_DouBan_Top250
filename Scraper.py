import csv

import requests
from bs4 import BeautifulSoup


def connect_and_cook_soup(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"}
    req = requests.get(url, headers=headers)
    return BeautifulSoup(req.content, "html.parser")


def result_rows(soup):
    lis = soup.find_all(class_="grid_view")[0].find_all("li")
    rows = []
    for li in lis:
        title = li.find_all(class_="hd")[0].find_all(class_="title")
        other = li.find_all(class_="hd")[0].find_all(class_="other")
        rating = li.find_all(class_="bd")[0].find_all(class_="rating_num")
        quote = li.find_all(class_="bd")[0].find_all(class_="inq")
        title_str = ""
        for t in title:
            title_str += t.get_text().replace('\xa0', ' ')

        other_str = ""
        for o in other:
            other_str += o.get_text().replace('\xa0', ' ')
        other_str = other_str[3:]

        rating_str = rating[0].get_text().replace('\xa0', ' ')

        quote_str = ""
        for q in quote:
            quote_str+= q.get_text()

        rows.append({"title": title_str,
                     "other_name": other_str,
                     "rating": rating_str,
                     "quote":quote_str})
    return rows


def write_csv(rows):
    with open("Top250.csv", "w", encoding="utf-8-sig", newline="") as csvfile:
        fieldnames = ["title", "other_name", "rating", "quote"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)


def run_once(url):
    soup = connect_and_cook_soup(url)
    rows = result_rows(soup)
    return rows


if __name__ == "__main__":
    rows = []
    for i in range(0, 10):
        url = "https://movie.douban.com/top250?start=" + str(i * 25)
        rows.extend(run_once(url))
    write_csv(rows)
