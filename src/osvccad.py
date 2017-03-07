import ccad.model as cm
import ccad.display as cd
import ccad.entities as ce
import OCC.Display.SimpleGui as SimpleGui
import numpy as np 
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


solid  = cm.from_step('level1/ASM0001_ASM_1_ASM.stp')
entity = ce.entity(solid)
#lshell = t1.subshapes('shell')
#pc = np.array(t1.center())
#t2 = t1.copy()
#t2.translate(-pc)
#
#u = cm.solid(lshell)
#lvertex = lshell[2].subshapes('vertex')
#ledge = lshell[2].subshapes('edge')
#lface = lshell[2].subshapes('face')
for k in entity.G.node:
    data = entity.G.node[k]['entities']
    points3d(data[0,:],data[1,:],data[2,:],resolution=10,mode='sphere',scale_factor=10)
#ax.volume(
s2 = entity.G.node[2]['shape']
lf = s2.subshapes('face')
#g1 = _GProp_GProps()
#lf0 = lf[0]
#_brepgprop_SurfaceProperties(lf0, g1)
