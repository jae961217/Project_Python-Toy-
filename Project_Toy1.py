import json
from pprint import pprint

def movie_info(movie):
    need = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    res = dict()
    for i in movie:
        if i in need:
            res[i] = movie[i]
    return res
    # 여기에 코드를 작성합니다.


def movie_info_genre(movie, genres):
    need = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    res = dict()
    for i in movie:
        if i in need:
            res[i] = movie[i]

    res['genre_name'] = []
    for i in res['genre_ids']:
        for j in genres:
            if i == j['id']:
                res['genre_name'].append(j['name'])
    del [res['genre_ids']]

    return res


def movie_info_genre2(movies, genres):
    def info(movie):
        need = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
        value = dict()
        for i in movie:
            if i in need:
                value[i] = movie[i]

        value['genre_name'] = []
        for i in value['genre_ids']:
            for j in genres:
                if i == j['id']:
                    value['genre_name'].append(j['name'])
        del [value['genre_ids']]

        return value

    res = []
    for i in movies:
        res.append(info(i))

    return res


def max_revenue(movies):
    res = ''
    revenue = 0
    for i in movies:
        file_name = 'data/movies/' + str(i['id']) + '.json'
        movie_detail = json.load(open(file_name, encoding='UTF8'))
        if revenue < movie_detail['revenue']:
            revenue = movie_detail['revenue']
            res = movie_detail['title']

    return res


def dec_movies(movies):
    res = []
    for i in movies:
        file_name = 'data/movies/' + str(i['id']) + '.json'
        movie_detail = json.load(open(file_name, encoding='UTF8'))
        if movie_detail['release_date'][5:7] == '12':
            res.append(movie_detail['title'])

    return res



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie))

    pprint(movie_info_genre(movie, genres_list))

    pprint(movie_info_genre2(movies, genres_list))

    print(max_revenue(movies))

    print(dec_movies(movies))