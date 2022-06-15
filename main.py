import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
responce = requests.get(URL)
html_text = responce.text

soup = BeautifulSoup(html_text, 'html.parser')

movies_tag = soup.find_all(name='h3', class_='title')
movies = [movie.getText() for movie in movies_tag]
print(movies)

for movie in movies[::-1]:
    with open('100movies.txt', 'a') as file:
        file.write(f'{movie}\n')



