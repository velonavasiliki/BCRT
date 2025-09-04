import igraph
from igraph import *
import random


print('Give parameter q<=1/2')
q = float(input())
print('Give the number of time steps')
n = int(input())

def flipCoin():
    f = random.uniform(0,1)
    return True if f>q else False

g = Graph()
g.add_vertices(2)
g.vs[0]["type"] = "R"
g.vs[1]["type"] = "B"
g.add_edges([(0,1)])

for i in range(1,n+1):
    g.add_vertices(1)
    g.vs[2*i]["type"] = "R"
    m1 = flipCoin()
    if m1 == True:    #no flip
         g.add_edges([(2*i,2*random.randint(1,i)-2)]) 
    else: g.add_edges([(2*i,2*random.randint(1,i)-1)])
    g.add_vertices(1)
    g.vs[2*i+1]["type"] = "B
    m2 = flipCoin()
    if m2 == False:     #flip
         g.add_edges([(2*i+1,2*random.randint(1,i)-2)]) 
    else: g.add_edges([(2*i+1,2*random.randint(1,i)-1)])


print(g)




