#! /home/uguen/anaconda/bin/python
from OCC.STEPControl import STEPControl_Reader
from OCC.Display.WebGl import x3dom_renderer
import pdb
import sys
filename = sys.argv[1]
fileout = filename.replace('stp','html')
step_reader = STEPControl_Reader()
step_reader.ReadFile(filename)
step_reader.TransferRoot()
shape = step_reader.Shape()
my_renderer = x3dom_renderer.X3DomRenderer(path='.',filename=fileout)
#my_renderer = x3dom_renderer.X3DomRenderer()
my_renderer.DisplayShape(shape)
