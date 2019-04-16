
class Show(object):

    def __init__(self, title, genre, rating=1):
        self.title = title
        self.genre = genre
        self.rating = rating

    def __repr__(self):
        return f'{self.title}, {self.rating}'

