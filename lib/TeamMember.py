class TeamMember:
    def __init__(self, name, rating, bkiller):
        self.name = name
        self.rating = rating
        self.bkiller = bkiller


    def to_string(self):
        return "%s,%s,%s" % (self.name, self.rating, self.bkiller)

