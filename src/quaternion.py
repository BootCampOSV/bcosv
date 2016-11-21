import networkx as nx
import numpy as np 
import numpy.linalg as la
import matplotlib.pyplot as plt 
import imusim.maths.quaternions as q
from itertools import takewhile,permutations
from mpl_toolkits.mplot3d import Axes3D
import pdb 

plt.close('all')
# Np : Number of point per cloud 
Np =  2 
Nc =  15 
G = nx.DiGraph()
for ic in range(Nc):
    c = np.random.rand(Np,3)
    c = c - np.mean(c,axis=0)
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
            un = u/np.sqrt(np.sum(u*u))
            th = 2*np.pi*np.random.rand(1)
            qt = q.Quaternion(0,v[0],v[1],v[2])
            qr = q.Quaternion(np.cos(th/2),np.sin(th/2)*un[0],np.sin(th/2)*un[1],np.sin(th/2)*un[2])
            G.add_edge(n1,n2,qt=qt,qr=qr)

col = ['r','b','g','c','m','k','y'] 

def view(G,Nc=3,Np=2):
    """  view graph 
    """ 
    nodelist = np.random.permutation(G.node.keys())
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    pts = np.zeros((Nc*Np,3))
    for k1,n in enumerate(nodelist):
        pt = G.node[n]['pt'] 
        qpt = q.QuaternionArray(np.hstack((np.zeros(Np)[:,None],pt)))
        if k1==0:
            n0 = n
            #print n0 
            #pts = pt
        else:
            path = nx.shortest_path(nx.Graph(G),n0,n)
            print n,path
            qts = q.Quaternion(0,0,0,0)
            qrs = q.Quaternion(1,0,0,0)
            for k2 in np.arange(len(path)-1):
                ledges = G.edges()
                # handle edge orientation 
                if (path[k2],path[k2+1]) in ledges:
                    qt = G.edge[path[k2]][path[k2+1]]['qt']
                    qr = G.edge[path[k2]][path[k2+1]]['qr']
                else:
                    qt = -G.edge[path[k2+1]][path[k2]]['qt']
                    qr =  G.edge[path[k2+1]][path[k2]]['qr'].conjugate
                print "qt :",qt
                print "qr :",qr
                #qts = qts + qt
                qts = qts
                qrs = qrs*qr
                print "qts : ",qts
                print "qrs : ",qrs
            #print qts
            #print qrs
            qce = qrs*qpt*qrs.conjugate
            pt  = (qce.vector+qts.vector).T
        pts[k1*Np:(k1+1)*Np,:] = pt 
    #return(pts-np.mean(pts,axis=0))
    return(pts)

def is_isomorph(pt1,pt2):
    """ test isomorphism between 2 sets of points

    Examples
    --------

        >>> import numpy as np 
        >>> from pylayers.geomutil import *
        >>> pt1 = np.random(3,10)
        >>> M = MEulerAngle(0.3,0.5,0.9)
        >>> pt2 = np.dot(M,pt1)
        >>> v = np.array([10,20,30])[:,None]
        >>> pt2 = pt2+v
        >>> is_isomorph(pt1,pt2)

    """
    assert(pt1.shape==pt2.shape)
    # N x 3
    pt1c = pt1 - np.sum(pt1,axis=0)/pt1.shape[1]
    pt2c = pt2 - np.sum(pt2,axis=0)/pt2.shape[1]
    A=np.dot(pt1c.T,pt1c)
    B=np.dot(pt1c.T,pt2c)
    M = np.dot(B,la.inv(A))
    err = pt2c.T-np.dot(M,pt1c.T)
    err2 = np.sum(err*err)
    if err2 < 1e-10:
        return(True,err2)
    else:
        return(False,err2)

pts1 = view(G,Nc=Nc,Np=Np)
print('--')
pts2 = view(G,Nc=Nc,Np=Np)
print('--')
pts3 = view(G,Nc=Nc,Np=Np)
#if is_isomorph(pts1,pts2)[0]:
#    print "isomorph"
fig1 = plt.figure()
ax1 = fig1.add_subplot(111,projection='3d')
ax1.scatter(pts1[:,0],pts1[:,1],pts1[:,2],s=20,color='r')
#fig2=plt.figure()
#ax2 = fig2.add_subplot(111,projection='3d')
ax1.scatter(pts2[:,0],pts2[:,1],pts2[:,2],s=20,color='b')
plt.show()

#import numpy as np 
#from pylayers.util.geomutil import *
#pt1 = np.random.rand(3,10)
#M = MEulerAngle(0,0,0)
#pt2 = np.dot(M,pt1)
#v = np.array([0,0,0])[:,None]
#pt2 = pt2+v
#if is_isomorph(pt1,pt2):
#    print "isomorph"
#else:
#    print "not isomorph"
