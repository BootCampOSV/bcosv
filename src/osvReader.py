from OCC.STEPControl import STEPControl_Reader
from OCC.IFSelect import IFSelect_RetDone, IFSelect_ItemsByEntity
from OCC.Display.SimpleGui import init_display
import sys

step_reader = STEPControl_Reader()
status = step_reader.ReadFile('../stp/TABBY_EVO_step_asm.stp')
#status = step_reader.ReadFile('../stp/single.stp')
#status = step_reader.ReadFile('../stp/both.stp')
#status = step_reader.ReadFile('../stp/part123.stp')
#status  =  step_reader.ReadFile('../stp/wheel.stp')
#status = step_reader.ReadFile('../stp/tab2clean.stp')
#status = step_reader.ReadFile('../stp/reconstructed.stp')
#status = step_reader.ReadFile('../asm0001_asm.stp')
#status = step_reader.ReadFile('../stp/example.stp')
#status = step_reader.ReadFile('../stp/TabbyEvo_4.stp')
#status = step_reader.ReadFile('../stp/cylinder_block.stp')

if status == IFSelect_RetDone:  # check status
    failsonly = False
    step_reader.PrintCheckLoad(failsonly, IFSelect_ItemsByEntity)
    step_reader.PrintCheckTransfer(failsonly, IFSelect_ItemsByEntity)

    ok = step_reader.TransferRoot(1)
    _nbs = step_reader.NbShapes()
    aResShape = step_reader.Shape(1)
else:
    print("Error: can't read file.")
    sys.exit(0)

display, start_display, add_menu, add_function_to_menu = init_display()
display.DisplayShape(aResShape, update=True)

f = display.View.View().GetObject()


def export_to_PDF(event=None):
    f.Export('torus_export.pdf', Graphic3d_EF_PDF)


def export_to_SVG(event=None):
    f.Export('torus_export.svg', Graphic3d_EF_SVG)


def export_to_PS(event=None):
    f.Export('torus_export.ps', Graphic3d_EF_PostScript)


def export_to_EnhPS(event=None):
    f.Export('torus_export_enh.ps', Graphic3d_EF_EnhPostScript)


def export_to_TEX(event=None):
    f.Export('torus_export.tex', Graphic3d_EF_TEX)


#if __name__ == '__main__':
#    add_menu('screencapture')
#    add_function_to_menu('screencapture', export_to_PDF)
#    add_function_to_menu('screencapture', export_to_SVG)
#    add_function_to_menu('screencapture', export_to_PS)
#    add_function_to_menu('screencapture', export_to_EnhPS)
#    add_function_to_menu('screencapture', export_to_TEX)
#    start_display()
