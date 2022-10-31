import imdb
# a.
rating = open('ratings.list','r')
rating.close()
# b.
# Поиск ТОП250 фильмов
ia = imdb.IMDb()
search = ia.get_top250_movies()
# Извлечение 250 заголовков
for i in range(250):
   print(search[i]['title'])
   #print(search[i]['votes'])

#c создаем файл с названиями файлов
top_250_file = open("top250_movies.txt", "w+")
top_250_file.write(str(search).replace(',','\n'))
top_250_file.close()


