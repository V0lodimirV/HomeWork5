import imdb
# a.
rating = open("data_hw5/ratings.list", 'r')
rating.close()
# b. 
# pip install IMDbPY
import imdb
film = imdb.IMDb()
# Поиск ТОП250 фильмов
search = film.get_top250_movies()
# Извлечение 250 заголовков
for i in range(250):
    print(search[i]['title'])
# c.  Программа создает 3 файла  top250_movies.txt – названия файлов,
# ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
def movies(*args):
    for i in args:
        movies = open(f"data_hw5/{i}", 'w')
        movies.close()
movies('top250_movies.txt', 'ratings.txt', 'years.txt')