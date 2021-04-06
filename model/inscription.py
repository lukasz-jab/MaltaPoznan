class Inscription():
    def __init__(self, id=None, title=None, comments=None):
        self.id = id
        self.title = title
        self.comments = comments

    def __repr__(self):
        return '%s, %s, %s' % (self.comments, self.title, self.id)

    def __eq__(self, other):
        return self.title == other.title
