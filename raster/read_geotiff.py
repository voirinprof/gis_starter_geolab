# -*- coding: utf-8 -*-
__author__ = 'voirin'

from osgeo import gdal
import sys
import numpy as np
from osgeo.gdalconst import *

# Activer l'enregistrement des pilotes GDAL
gdal.AllRegister()

# Fichier à lire
filename = r"/workspaces/gis_starter_geolab/data/alberta_2011.tiff"

# Ouvrir le fichier en mode lecture seule
ds = gdal.Open(filename, GA_ReadOnly)

if ds is None:
    print(f"Could not open {filename}")
    sys.exit(1)

# Lire les dimensions : colonnes, lignes, bandes
cols = ds.RasterXSize
rows = ds.RasterYSize
bands = ds.RasterCount
print(f"Dimensions: cols={cols}, rows={rows}, bands={bands}")

# Récupérer la géoréférence de l'image
geotransform = ds.GetGeoTransform()
originX = geotransform[0]
originY = geotransform[3]
pixelWidth = geotransform[1]
pixelHeight = geotransform[5]
print(f"Geotransform: {geotransform}")

# Récupérer la bande 1
band = ds.GetRasterBand(1)

try:
    # Lire la matrice de la bande 1 comme un array numpy
    data = band.ReadAsArray(0, 0, cols, rows)
    if data is None:
        print("Erreur lors de la lecture des données de la bande")
        sys.exit(1)
    print("Données de la bande 1 (premières lignes) :")
    print(data[:5, :5])  # Afficher un sous-ensemble pour éviter une sortie massive
except Exception as e:
    print(f"Erreur lors de la lecture de la bande: {e}")
    # Alternative : lire les données manuellement si ReadAsArray échoue
    try:
        data = np.zeros((rows, cols), dtype=np.float32)  # Ajuster le type selon les données
        for i in range(rows):
            data[i, :] = band.ReadRaster(0, i, cols, 1, cols, 1, band.DataType)
        print("Données lues via ReadRaster (premières lignes) :")
        print(data[:5, :5])
    except Exception as e:
        print(f"Erreur lors de la lecture via ReadRaster: {e}")
        sys.exit(1)

# Fermer le fichier
ds = None