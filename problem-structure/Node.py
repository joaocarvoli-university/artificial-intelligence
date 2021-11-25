from Relationship import Relationship


class Node:
    def __init__(self, name, weight, related):
        self.name = name
        self.relation = Relationship(weight, related)

    def getName(self):
        return self.name

    def getRelation(self):
        return self.relation.getRelated()

    def setRelated(self, weight, related):
        return self.relation.setRelation(weight, related)
