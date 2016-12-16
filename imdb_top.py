import requests
import re
from bs4 import BeautifulSoup 

count = 1

seed = 1

target = open("demo.pl", 'w')

for page in range(1, 11):

    url = "http://www.imdb.com/list/ls006266261/?start={}".format(seed)
    seed += 100
    r= requests.get(url)
    soup = BeautifulSoup(r.content)

    movies = soup.find_all("div", {"class": "info"})

    for movie in movies:
        title = movie.find("b").find("a").text

        title = title.replace(':', '').replace('.', '').replace('-','_').replace('!', '').replace(' ', '_').replace(',', '').replace('\'', '').lower()

        year = movie.find("b").find("span").text
        year = re.findall(r"\d{4}", year)[0]
        rating = movie.find("span", {"class": "value"}).text
        director = movie.find("div", {"class": "secondary"}).find("a").text
        link = "http://www.imdb.com" + movie.find("b").find("a")['href']

        single = requests.get(link)

        soup2 = BeautifulSoup(single.content)
        cat = soup2.find("div", {"class": "subtext"}).findAll(itemprop="genre")

        for genre in cat:
        	result = "movie(" + title + ", " + str(round(float(rating.strip()))) + ", " + year + ", " + genre.text.strip().replace('-', '_').lower() + ", " + director.replace(' ', '_').strip().lower() +")."
        	print("{} : {}".format(count, result))
        	target.write(result)
        	target.write("\n")
        	count += 1

print("\n\n=>Finished Scrape")       
target.close()       
