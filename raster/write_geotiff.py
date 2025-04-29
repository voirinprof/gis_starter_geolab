# -*- coding: utf-8 -*-
__author__ = 'voirin'

import numpy as np
import sys
from osgeo import gdal
from osgeo.gdalconst import *

# Activer l'enregistrement des pilotes GDAL
gdal.AllRegister()

# Définir le driver GeoTIFF
driver = gdal.GetDriverByName("GTiff")
if driver is None:
    print("Driver GeoTIFF non disponible")
    sys.exit(1)

# Paramètres de l'image
rows = 50
cols = 50
output_path = "/workspaces/gis_starter_geolab/data/test.tif"

# Créer une image GeoTIFF (1 bande, type Int32)
image = driver.Create(output_path, cols, rows, 1, GDT_Int32)
if image is None:
    print(f"Impossible de créer {output_path}")
    sys.exit(1)

# Définir une géotransformation simple (exemple : coin supérieur gauche à (0,0), résolution 1x1)
geotransform = (0.0, 1.0, 0.0, 0.0, 0.0, -1.0)  # (originX, pixelWidth, 0, originY, 0, pixelHeight)
image.SetGeoTransform(geotransform)

# Définir un CRS (exemple : EPSG:4326)
image.SetProjection('EPSG:4326')

# Récupérer la bande 1
band = image.GetRasterBand(1)

# Créer une matrice numpy de zéros (type int32 pour correspondre à GDT_Int32)
data = np.zeros((rows, cols), dtype=np.int32)

try:
    # Écrire la matrice dans la bande
    band.WriteArray(data, 0, 0)
except Exception as e:
    print(f"Erreur lors de l'écriture avec WriteArray: {e}")
    # Alternative : écrire les données manuellement
    try:
        for i in range(rows):
            band.WriteRaster(0, i, cols, 1, data[i, :].tobytes(), cols, 1, GDT_Int32)
        print("Données écrites via WriteRaster")
    except Exception as e:
        print(f"Erreur lors de l'écriture via WriteRaster: {e}")
        image = None
        sys.exit(1)

# Vider le cache et définir la valeur NoData
band.FlushCache()
band.SetNoDataValue(-99)

# Fermer le fichier
image = None
print(f"Fichier {output_path} créé avec succès")