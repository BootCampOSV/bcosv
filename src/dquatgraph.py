import networkx as nx
import numpy as np 
import numpy.linalg as la
import matplotlib.pyplot as plt 
from quaternions import *
import scipy.spatial.distance as di
from itertools import takewhile,permutations
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import pdb 

plt.close('all')
np.random.seed(10)
# Np : Number of point per cloud 
Np =  2 
Nc =  3
G = nx.DiGraph()
for ic in range(Nc):
    #v = np.random.rand(3)
    v  = np.array([0,0,1])
    vn = v/np.sqrt(np.sum(v*v))
    c = vn[None,:]*np.linspace(1,2,Np)[:,None]
    cc = c - np.mean(c,axis=0)
    G.add_node(ic+1,pt=cc)

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
            #print un
            th = 2*np.pi*np.random.rand(1)
            qt = Quaternion(v[0]*1j,v[1]+v[2]*1j)
            qr = Quaternion(np.cos(th/2.)+1j*np.sin(th/2.)*un[0],np.sin(th/2.)*un[1]+1j*np.sin(th/2.)*un[2])
            dis = Displacement(qt=qt,qr=qr)
            G.add_edge(n1,n2,dis=dis)

col = ['r','b','g','c','m','k','y'] 

def view(G,Nc=3,Np=2):
    """  view graph 
    """ 
    # pick a random permutation of graph nodes
    nodelist = np.random.permutation(G.node.keys())
    # loop over nodes of the graph 
    qptf = Quaternion(np.zeros((Nc*Np,1)),np.zeros((Nc*Np,1)))
    dqpt = {}
    for k1,n in enumerate(nodelist):
        # get set of points from node n
        pt  = G.node[n]['pt'] 
        # build the array of quaternions 
        #if k1==0:
        qpt  = DQPoint(pt)
        #else:
        #    qpt = q.QuaternionArray(np.vstack((qpt.array,pte)))
        if k1==0:
            # cluster n0 forces the origin
            n0 = n
            #print n0 
            #pts = pt
        else:
            # find shortest path from node n to node n0
            path = nx.shortest_path(nx.Graph(G),n,n0)
            print n,path
            dqs = Displacement() 
            # chaining of dual quaternions along the path 
            for k2 in np.arange(len(path)-1):
                ledges = G.edges()
                # handle edge orientation 
                if (path[k2],path[k2+1]) in ledges:
                    dis = G.edge[path[k2]][path[k2+1]]['dis']
                else:
                    dis = G.edge[path[k2+1]][path[k2]]['dis'].conj1()
                dqs = dqs*dis
            qpt = dqs*qpt*dqs.conj1()
        dqpt[n] = qpt
        #pts[k1*Np:(k1+1)*Np,:] = pt 
    #return(pts-np.mean(pts,axis=0))
    for k in range(1,len(nodelist)+1):
        qptf[(k-1)*Np:k*Np] = dqpt[k].qd 
    return(dqpt,qptf)
    #return(dqpt)

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
    A = np.dot(pt1c.T,pt1c)
    B = np.dot(pt1c.T,pt2c)
    M = np.dot(B,la.inv(A))
    err = pt2c.T-np.dot(M,pt1c.T)
    err2 = np.sum(err*err)
    if err2 < 1e-10:
        return(True,err2)
    else:
        return(False,err2)

dq1,qpts1 = view(G,Nc=Nc,Np=Np)
print('--')
dq2,qpts2 = view(G,Nc=Nc,Np=Np)
print('--')
dq3,qpts3 = view(G,Nc=Nc,Np=Np)
pts1 = qpts1.vect().T
pts2 = qpts2.vect().T
pts3 = qpts3.vect().T
##if is_isomorph(pts1,pts2)[0]:
##    print "isomorph"
##pts1 = pts1-np.mean(pts1,axis=0)
##pts2 = pts2-np.mean(pts2,axis=0)
##pts3 = pts3-np.mean(pts3,axis=0)
D1 = di.cdist(pts1,pts1)
D2 = di.cdist(pts2,pts2)
D3 = di.cdist(pts3,pts3)
plt.subplot(131)
plt.imshow(D1,cmap=cm.jet)
plt.colorbar()
plt.subplot(132)
plt.imshow(D2,cmap=cm.jet)
plt.colorbar()
plt.subplot(133)
plt.imshow(D3,cmap=cm.jet)
plt.colorbar()
fig1 = plt.figure()
ax1 = fig1.add_subplot(111,projection='3d')
##ax2 = fig2.add_subplot(111,projection='3d')
ax1.scatter(pts1[:,0],pts1[:,1],pts1[:,2],s=20,color='r')
ax1.scatter(pts2[:,0],pts2[:,1],pts2[:,2],s=20,color='b')
ax1.scatter(pts3[:,0],pts3[:,1],pts3[:,2],s=20,color='g')
plt.show()
#
##import numpy as np 
##from pylayers.util.geomutil import *
##pt1 = np.random.rand(3,10)
##M = MEulerAngle(0,0,0)
##pt2 = np.dot(M,pt1)
##v = np.array([0,0,0])[:,None]
##pt2 = pt2+v
##if is_isomorph(pt1,pt2):
##    print "isomorph"
##else:
##    print "not isomorph"
