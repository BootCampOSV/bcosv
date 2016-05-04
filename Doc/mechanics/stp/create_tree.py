import os
import path
import networkx as nx
import matplotlib.pyplot as plt
import pdb

fd = open('../ListProduct.txt',"r")
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
    G.add_node(name,l=l)
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

d = {}
for n in G.nodes_iter():
    if G.node[n]['l']==1:
        d[n]={}

for n1 in d:
    ln2 = nx.neighbors(G,n1)
    print n1
    os.mkdir(n1)
    for n2 in ln2:
        if G.node[n2]['l']==2:
            d[n1][n2]={}
            os.mkdir(n1+'/'+n2)
            ln3 = nx.neighbors(G,n2)
            print '\t',n2
            for n3 in ln3:
                if G.node[n3]['l']==3:
                    d[n1][n2][n3]={}
                    os.mkdir(n1+'/'+n2+'/'+n3)
                    ln4 = nx.neighbors(G,n3)
                    print '\t\t',n3
                    for n4 in ln4:
                        ln5 = nx.neighbors(G,n4)
                        print '\t\t\t',n4
                        if G.node[n4]['l']==4:
                            d[n1][n2][n3][n4]={}
                            os.mkdir(n1+'/'+n2+'/'+n3+'/'+n4)
                            for n5 in ln5:
                                if G.node[n5]['l']==5:
                                    d[n1][n2][n3][n4][n5]={}
                                    os.mkdir(n1+'/'+n2+'/'+n3+'/'+n4+'/'+n5)
                                    print '\t\t\t\t',n5

