#! /home/uguen/anaconda/bin/python
from OCC.STEPControl import STEPControl_Reader
from OCC.Display.WebGl import x3dom_renderer_osv
import pdb
import sys
#
# usage stp2html.py filename level
#
filename = sys.argv[1]
level = sys.argv[2]
fileout = filename.replace('.stp','')
step_reader = STEPControl_Reader()
step_reader.ReadFile(filename)
step_reader.TransferRoot()
shape = step_reader.Shape()
my_renderer = x3dom_renderer_osv.X3DomRenderer(path='.',filename=fileout,level=level)
#my_renderer = x3dom_renderer.X3DomRenderer()
my_renderer.DisplayShape(shape)
