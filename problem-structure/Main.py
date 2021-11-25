from Node import Node

g = Node('Fortaleza', 5, 'Quixada')
g.setRelated(7, 'Mombaça')
print(g.getName(), "-> ", g.getRelation())
