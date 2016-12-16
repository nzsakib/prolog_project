import requests
import re
from bs4 import BeautifulSoup 

seedYear = 2004

count = 1

for i in range(1):
    seedYear += 1
    for page in range(1, 5):

        url = "http://www.imdb.com/search/title?release_date={}&page={}".format(seedYear, page)

        r= requests.get(url)
        soup = BeautifulSoup(r.content)

        movies = soup.find_all("div", {"class": "lister-item-content"})

        for movie in movies:
            title = movie.find("h3").find("a").text
            
            year = movie.find("h3").find("span", {"class": "lister-item-year"}).text

            categories = movie.find("span", {"class": "genre"}).text

            rating = movie.find("div", {"class": "ratings-imdb-rating"}).text


            year = year.strip()
            year = re.findall(r"\d{4}", year)[0]
            #title year rating categories-loop
            categories = categories.strip()
            categories = categories.split(',')
            #length = len(categories)
            title = title.replace(':', '').replace('.', '').replace('-','_').replace('!', '').replace(' ', '_').replace(',', '').replace('\'', '').lower()
            for genre in categories:
                result = "movie(" + title + ", " + str(round(float(rating.strip()))) + ", " + year + ", " + genre.strip().replace('-', '_').lower() + ")."
            

            print("{} : {}".format(count, result))
            # print("Title: {}".format(title.strip()))
            # try:
            #     print("Year: {}".format(year.strip()))
            # except:
            #     pass
            # print("Genre: {}".format(categories.strip()))

            # print("Rate: {}".format(rating.strip()))
            count += 1
