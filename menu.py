import maya.cmds as cmds
import maya.cmds as cmd

def mat(*args):

    red	    =	[1,0,0]
    aqua	=	[0,1,1]
    blue	=	[0,0,1]
    fuchsia	=	[1,0,1]
    gray	=	[0,502,0,502,0,502]
    green	=	[0,0,502,0]
    lime	=	[0,1,0]
    maroon	=	[0,502,0,0]
    navy	=	[0,0,0,502]
    olive	=	[0,502,0,502,0]
    purple	=	[0,502,0,0,502]
    silver	=	[0,753,0,753,0,753]
    teal	=	[0,0,502,0,502]
    white	=	[1,1,1]
    yellow	=	[1,1,0]

    colori = [red, aqua,blue,fuchsia,gray,green,lime,maroon,navy,olive,purple,silver,teal,white,yellow]
    x = 0
    count = 0

    select_list = cmds.ls(selection = True)


    for selection in select_list:
        cmds.select(selection, visible=True )

        faces = cmds.ls(sl=True)

        # assign shader
        sha = cmds.shadingNode('blinn', asShader=True, name="{}_Material".format(selection))

        r = colori[count][0]
        g = colori[count][1]
        b = colori[count][2]

        cmds.setAttr(sha + ".color", r,g,b)

        count = count + 1

        if count == 15:
            count = 0

        sg = cmds.sets(empty=True, renderable=True, noSurfaceShader=True,  name="{}_{}_sg".format(selection, x))
        cmds.connectAttr( sha+".outColor", sg+".surfaceShader", f=True)
        cmds.sets(faces, e=True, forceElement=sg)





def rename_tool(*args):

    #nomi oggetti
    select_list = cmds.ls(selection = True)

    for selection in select_list:
        cmds.select(selection, visible=True )
        select_v_val = cmd.ls(sl=1)

        sel_ = cmds.listRelatives(select_v_val, shapes=1)

        if (cmds.nodeType(sel_)=='locator'):
            prefix = "LOC_"
        elif (cmds.nodeType(sel_)=='nurbsCurve'):
            prefix = "CRV_"
        if (cmds.nodeType(sel_)=='mesh'):
            prefix = "MSH_"
            result = cmds.promptDialog(
                title=prefix,
                message='Enter Name:',
                button=['OK', 'Cancel'],
                defaultButton='OK',
                cancelButton='Cancel',
                dismissString='Cancel')

            if result == 'OK':
                    text_ = cmds.promptDialog(query=True, text=True)
            cmds.rename(selection, prefix + text_)



def pre_separator_02(*args):
    cmd.separator()
    cmd.separator(style="singleDash")
    cmd.separator()

def try_m(*args):
    if cmd.window('UI_Menu_MP', exists=True):
        cmd.deleteUI('UI_Menu_MP')

try_m()

mainWindow = cmd.window("UI_Menu_MP", menuBar=True, h=100, title='MP_Tool', iconName='MP_Tool', resizeToFitChildren=True)
cmd.columnLayout("main_t", adj=1, cal="center")
cmd.separator(bgc=[1, 0.5, 0.5])
cmds.helpLine(annotation='Help line', bgc=[0.5, 0.5, 0.5])
#######################-------------------------------#######################

###
cmd.columnLayout("main_layout", adj=1, cal="center")

cmd.separator(bgc=[1, 0.5, 0.5])
cmd.text(font='boldLabelFont' ,label=
'AVE O MARIA',  annotation='LEGGERE ATTENTAMENTE IL TESTO!')
cmd.separator(bgc=[1, 0.5, 0.5])

cmd.text(label='Tool Created By Matteo Petracci')
pre_separator_02()
##################################################################################
cmd.button (label = 'PORCO DIO', h=30,w=20, command = rename_tool, enable=True,  annotation='Questo bottone è stato maledetto!')
pre_separator_02()

cmd.showWindow()
