import networkx as nx
import numpy as np 
import numpy.linalg as la
import matplotlib.pyplot as plt 
import imusim.maths.quaternions as q
from itertools import takewhile,permutations
Np =  3 
Nc =  6 
G = nx.DiGraph()
for ic in range(Nc):
    c = np.random.rand(Np,3)
    G.add_node(ic+1,pt=c)

ln = G.node.keys()

while not nx.is_connected(nx.Graph(G)):

    k1 = np.random.randint(Nc)
    k2 = np.random.randint(Nc)

    if (k1!=k2):  
        n1 = ln[k1]
        n2 = ln[k2]
        if (n1,n2) not in G.edges():
            v = 20*(np.random.rand(3)-0.5)
            u = np.random.rand(3)
            un = u/np.sum(u*u)
            th = 2*np.pi*np.random.rand(1)
            qt = q.Quaternion(0,v[0],v[1],v[2])
            qr = q.Quaternion(np.cos(th/2),np.sin(th/2)*un[0],np.sin(th/2)*un[1],np.sin(th/2)*un[2])
            G.add_edge(n1,n2,qt=qt,qr=qr)

col = ['r','b','g','c','m','k','y'] 

def view(G):
    nodelist = np.random.permutation(G.node.keys())
    fig=plt.figure()
    ax = fig.gca(projection='3d')
    for k,n in enumerate(nodelist):
        pt = G.node[n]['pt'] 
        qpt = q.QuaternionArray(np.hstack((np.zeros(Np)[:,None],pt)))
        if k==0:
            n0 = n
            #print n0 
            pts = pt
        else:
            path = nx.shortest_path(nx.Graph(G),n0,n)
            print n,path
            qts = q.Quaternion(0,0,0,0)
            qrs = q.Quaternion(1,0,0,0)
            for k in np.arange(len(path)-1):
                ledges = G.edges()
                # handle edge orientation 
                if (path[k],path[k+1]) in ledges:
                    sign = +1
                    qt = G.edge[path[k]][path[k+1]]['qt']
                    qr = G.edge[path[k]][path[k+1]]['qr']
                else:
                    sign = -1
                    qt = -G.edge[path[k+1]][path[k]]['qt']
                    qr = G.edge[path[k+1]][path[k]]['qr'].conjugate
                qts = qts + qt
                qrs = qrs*qr 
            #print qts
            #print qrs
            qce=qrs*qpt*qrs.conjugate
            pt=(qce.vector+qts.vector).T
            pts = np.vstack((pts,pt))
    return(pts)

def is_isomorph(pt1,pt2):
    assert(pt1.shape==pt2.shape)
    pt1c = pt1 - np.sum(pt1,axis=0)/pt1.shape[0]
    pt2c = pt2 - np.sum(pt2,axis=0)/pt2.shape[0]
    A=np.dot(pt1c,pt1c.T)
    B=np.dot(pt2c,pt1c.T)
    M =np.dot(B,la.inv(A))
    err = pt2c-np.dot(M,pt1c)
    err2 = np.sum(err*err)
    return(err2)

pts1 = view(G)
print('--')
pts2 = view(G)
print('--')
pts3 = view(G)
#        ax.scatter(pt[:,0],pt[:,1],pt[:,2],color=col[n])
is_isomorph(pts1,pts2)
