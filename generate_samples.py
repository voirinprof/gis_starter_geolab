import geopandas as gpd
import numpy as np
import pandas as pd
from shapely.geometry import Point
import os

# Paramètres
output_path = "/workspaces/gis_starter_geolab/data/sample.shp"
num_points = 470000  # Nombre de points à générer
crs = "EPSG:4326"  # Système de coordonnées (WGS84)

# Définir l'étendue géographique (bounding box) : [min_lon, min_lat, max_lon, max_lat]
bbox = [-82.5, 42.20, -76.6, 45.43]

# Générer des coordonnées aléatoires
np.random.seed(42)  # Pour la reproductibilité
lons = np.random.uniform(bbox[0], bbox[2], num_points)  # Longitudes
lats = np.random.uniform(bbox[1], bbox[3], num_points)  # Latitudes

# Générer des valeurs aléatoires (par exemple, entiers entre 1 et 100)
values = np.random.randint(1, 101, num_points)

# Créer des géométries Point
geometry = [Point(lon, lat) for lon, lat in zip(lons, lats)]

# Créer un DataFrame avec les coordonnées et les valeurs
data = {
    'value': values,
    'geometry': geometry
}
gdf = gpd.GeoDataFrame(data, crs=crs)

gdf_3348 = gdf.to_crs('epsg:3348')
# Vérifier que le répertoire de sortie existe
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Sauvegarder dans un fichier Shapefile
gdf_3348.to_file(output_path, driver="ESRI Shapefile")

print(f"Shapefile créé avec succès : {output_path}")