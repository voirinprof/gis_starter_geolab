# -*- coding: utf-8 -*-
__author__ = 'voirin'

# j'importe OGR
from osgeo import ogr

# je déclare le chemin vers le fichier
# il faut ajuster en fonction de votre répertoire
shpfile = r'/workspaces/gis_starter_geolab/data/world.shp'
# je déclare un Pilote SHP
driver = ogr.GetDriverByName('ESRI Shapefile')
# # j'ouvre le fichier
datasource = driver.Open(shpfile)
# je cherche les couches
layer = datasource.GetLayer()

# définition du masque
maskfile = r'/workspaces/gis_starter_geolab/data/mask.shp'
datasourceMask = driver.Open(maskfile)
layerMask = datasourceMask.GetLayer()
geomMask = None
featureMask = layerMask.GetNextFeature()
geomMask = featureMask.GetGeometryRef()
# géométrie du masque
print(geomMask)

# on parcourt les entités de world
feature = layer.GetNextFeature()

while feature:
    # on récupère la géométrie
    geography = feature.GetGeometryRef()
    # on récupère la valeur de l'attribut NAME
    name = feature.GetField('NAME')
    # si le masque se superpose au pays
    # alors je l'affiche
    if geomMask.Overlaps(geography):
        print(name)

    feature = layer.GetNextFeature()
