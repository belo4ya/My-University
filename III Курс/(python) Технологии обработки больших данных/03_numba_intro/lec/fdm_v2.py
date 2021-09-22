# v.1

import csv


def read_movies(src, skip_header=True, title_column_ind=1):
    '''
    Parameters:
        src (String): имя файла с фильмами
        skip_header (bool, optional): Пропускать ли заголовок?
        title_column_ind (int, optional): Столбец с названиями фильмов
    Returns:
        list: Список названий фильмов из файла (столбец title_column_ind в CSV)
    '''
    with open(src) as fd:
        csv_reader = csv.reader(fd, delimiter=',')
        movies = [row[title_column_ind] for row in csv_reader]
        if skip_header:
            movies = movies[1:]
        return movies


# исправляем очевидное "слабое место" - огромное количество вызовов lower()

def is_duplicate2(needle, haystack):
    for movie in haystack:
        if needle == movie:
            return True
    return False


def find_duplicate_movies2(src='tmdb_5000_credits.csv'):
    movies = [movie.lower() for movie in read_movies(src)]
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate2(movie, movies):
            duplicates.append(movie)
    return duplicates
