import os
import path
import networkx as nx
import matplotlib.pyplot as plt
import pdb

fd = open('ListProduct.txt',"r")
lis = fd.readlines()
G = nx.Graph()
lprev = 1
d = {}
for li in lis:
    ch1  = li.split("PRODUCT,")
    start = ch1[0]
    if start[0]!=' ':
        l = 0
    elif start[4]!=' ':
        l = 1
    elif start[8]!=' ':
        l = 2
    elif start[12]!=' ':
        l = 3
    elif start[16]!=' ':
        l = 4
    else:
        l =5

    name = ch1[1].split(',')[0].replace('"','').replace('\'','')
    G.add_node(name)
    if l!=lprev:
        d[l]=name
    if l>0:
        G.add_edge(name,d[l-1])
    lprev = l

from networkx.drawing.nx_pydot import graphviz_layout
pos=graphviz_layout(G,prog='twopi',args='')
#pos=nx.spring_layout(G)
fig = plt.figure(figsize=(20,20))
nx.draw(G,pos,node_size=20,alpha=0.5,node_color='blue',with_labels=True,fig=fig)
plt.savefig('tabbyGraph.png')
