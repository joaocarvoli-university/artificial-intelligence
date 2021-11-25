class Relationship:
    def __init__(self, weight, related):
        relation = [[weight, related]]
        self.related = relation

    def getRelated(self):
        return self.related

    def setRelation(self, weight, related):
        self.related.append([weight, related])

