import ccad.model as cm
import ccad.display as cd
import ccad.entities as ce
from numpy.linalg import svd
from quaternions import *
import OCC.Display.SimpleGui as SimpleGui
import os
import pdb 
import numpy as np 
import networkx as nx 
from mayavi.mlab import *
from OCC.GProp import GProp_GProps as _GProp_GProps
from OCC.BRepGProp import (brepgprop_VolumeProperties as _brepgprop_VolumeProperties,
                           brepgprop_LinearProperties as _brepgprop_LinearProperties,
                           brepgprop_SurfaceProperties as _brepgprop_SurfaceProperties)

#s1=cm.sphere(1.0)
#s1.translate(np.array([1,12,3]))
#b1 = cm.box(1,2,5)
#s = s1-b1

def view(model):
    display, start_display, add_menu, add_function_to_menu = SimpleGui.init_display()
    display.DisplayShape(model.shape, update = True)
    start_display()
#
# read a file from the OSV parts
# The goal is to decomposed this object in a graph of simpler objects 
#

# 1) get a solid from step
solid  = cm.from_step('level1/ASM0001_ASM_1_ASM.stp')
#solid  = cm.from_step('level1/MOTORIDUTTORE_ASM.stp')
# 2) construct entity from solid
entity = ce.entity(solid)

#
# An entity is a solid and a graph
#
#lshell = t1.subshapes('shell')
#pc = np.array(t1.center())
#t2 = t1.copy()
#t2.translate(-pc)
#
#u = cm.solid(lshell)
#lvertex = lshell[2].subshapes('vertex')
#ledge = lshell[2].subshapes('edge')
#lface = lshell[2].subshapes('face')
#
# Loop over all entities 
#
for k in entity.G.node:
    data = entity.G.node[k]['pcloud']
    pts = np.vstack((data[0,:],data[1,:],data[2,:])).T
    ptm = np.mean(pts,axis=0)
    ptsm = pts - ptm 
    U,S,V = svd(ptsm)
    
    q = Quaternion()
    q.from_mat(V)
    vec,ang = q.vecang()

    shp = entity.G.node[k]['shape']

    S0 = str(int(np.ceil(S[0])))
    S1 = str(int(np.ceil(S[1])))
    S2 = str(int(np.ceil(S[2])))

    sig = S0+'_'+S1+'_'+S2
    # if signature has not been already encountered, create new file
    filename = sig+'.stp'
    if not os.path.isfile(filename):
       shp.translate(-ptm)
       shp.rotate(np.array([0,0,0]),vec,ang)
       shp.to_step(filename)

    print(sig,ptm,vec,ang)

    entity.G.node[k]['name']=sig
    entity.G.node[k]['R']=V
    entity.G.node[k]['ptm']=ptm
    entity.G.node[k]['q']=q

    # Mayavi vizualisation of point cloud
    #points3d(data[0,:],data[1,:],data[2,:],resolution=10,mode='sphere',scale_factor=10)

#ax.volume(
s2 = entity.G.node[2]['shape']
lf = s2.subshapes('face')
#g1 = _GProp_GProps()
#lf0 = lf[0]
#_brepgprop_SurfaceProperties(lf0, g1)
