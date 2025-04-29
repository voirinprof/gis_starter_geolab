import fiona
import pyproj
from shapely.geometry import shape, mapping
from shapely.ops import transform
from fiona.crs import from_epsg

# Afficher la version de Fiona
print(fiona.__version__)

# Chemins des fichiers d'entrée et de sortie
source_shapefile_path = r'/workspaces/gis_starter_geolab/data/mask_satellite.shp'
target_shapefile_path = r'/workspaces/gis_starter_geolab/data/mask_satellite_4326.shp'

# Spécifier la projection cible
target_crs = from_epsg(4326)  # WGS 84 (EPSG:4326)

# Ouvrir le fichier source en mode lecture
with fiona.open(source_shapefile_path, 'r') as src:
    # Vérifier le CRS source
    if not src.crs:
        raise ValueError("Le fichier source n'a pas de CRS défini. Spécifiez un CRS source.")
    src_crs = src.crs

    # Créer le schéma pour le fichier de sortie (copie du schéma source)
    schema = src.schema

    # Ouvrir le fichier cible en mode écriture
    with fiona.open(target_shapefile_path, 'w', driver='ESRI Shapefile', crs=target_crs, schema=schema) as dst:
        # Créer un transformateur pour la reprojection
        project = pyproj.Transformer.from_crs(src_crs, target_crs, always_xy=True).transform

        # Parcourir les features
        for feature in src:
            try:
                # Extraire la géométrie
                geom = shape(feature['geometry'])
                
                # Vérifier la validité de la géométrie
                if not geom.is_valid:
                    print(f"Géométrie invalide pour feature {feature.get('id', 'unknown')}, sautée")
                    continue
                
                # Reprojeter la géométrie
                reprojected_geom = transform(project, geom)
                
                # Créer une nouvelle feature pour éviter la modification directe
                new_feature = {
                    'geometry': mapping(reprojected_geom),  # Pas de shape() ici
                    'properties': feature['properties']
                }
                
                # Écrire la nouvelle feature
                dst.write(new_feature)
            except Exception as e:
                print(f"Erreur pour feature {feature.get('id', 'unknown')}: {e}")
                continue