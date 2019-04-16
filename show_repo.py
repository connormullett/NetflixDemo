
from show import Show

shows = []


def create(title, genre, rating):
    new_show = Show(title, genre, rating)
    shows.append(new_show)


def delete(title):
    show_to_delete = shows.index(get_show_by_name(title))
    del shows[show_to_delete]


def update(search_title, title=None, genre=None, rating=None):
    show_to_update = get_show_by_name(search_title)
    if title:
        show_to_update.title = title
    if genre:
        show_to_update.genre = genre
    if rating:
        show_to_update.rating = rating

    index = shows.index(show_to_update)
    shows[index] = show_to_update


def get_all():
    return shows


def get_show_by_name(title):
    for show in shows:
        if show.title == title:
            return show

