import maya.cmds as cmds

'''
for o in pm.ls(selection=True):
for shp in pm.listRelatives(o, children=True, sh=True):
if pm.nodeType(shp, q=True)=='mesh':
'''

#seleziono una cosa alla volta

for shp in pm.listRelatives(o, children=True, sh=True):
if pm.nodeType(shp, q=True)=='mesh':
