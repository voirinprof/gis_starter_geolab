# GIS Starter GeoLab

Welcome to the **GIS Starter GeoLab** repository! This project provides a collection of Python scripts and tools designed for geospatial data processing and analysis, ideal for beginners and intermediate users in the field of Geographic Information Systems (GIS). The repository is configured to run seamlessly in GitHub Codespaces, leveraging a pre-configured environment with essential geospatial libraries.

## Project Overview

The **GIS Starter GeoLab** is a learning and experimentation platform for geospatial data manipulation. It includes scripts for:
- Reading and writing raster data (e.g., GeoTIFF files).
- Processing vector data (e.g., Shapefiles) with operations like reprojection.
- Generating synthetic geospatial datasets, such as random point Shapefiles.


## Repository Structure

```
gis_starter_geolab/
├── .devcontainer/
│   ├── devcontainer.json        # Codespaces configuration
│   ├── Dockerfile              # Custom Docker image for geospatial tools
│   └── requirements.txt        # Python dependencies
├── data/
│   ├── alberta_2011.tiff       # Sample GeoTIFF file
│   └── ...
├── raster/
│   ├── read_geotiff.py         # Script to read GeoTIFF files
│   └── ...                     # scripts for ratser data
├── vector/
│   ├── reproject_vector_with_fiona.py  # Script to reproject Shapefiles
│   └── ...                             # all scripts for vector data
├── analysis/
│   └── ...                             # scripts for converting vector/raster, using rtree, shortest path, ...
├── csv_json_xml/
│   └── ...                             # all scripts for csv, json, xml data
├── web/
│   └── ...                             # all scripts for web data
└── README.md                   # This file
```

## Prerequisites

To use this repository, you need:
- A GitHub account with access to GitHub Codespaces.
- Basic knowledge of Python and GIS concepts.

The repository is pre-configured to run in GitHub Codespaces, which provides a cloud-based development environment with all dependencies installed.

## Getting Started

### Using GitHub Codespaces

1. **Open the Repository in Codespaces**:
   - Navigate to [github.com/voirinprof/gis_starter_geolab](https://github.com/voirinprof/gis_starter_geolab).
   - Click the **Code** button, then select **Create codespace on main**.
   - Wait for the Codespace to initialize (this may take a few minutes as it builds the Docker environment).

2. **Verify the Environment**:
   - Open a terminal in Codespaces and check the installed Python packages:
     ```bash
     pip list
     ```
     Expected key packages:
     - `geopandas==0.14.4`
     - `rasterio==1.3.10`
     - `fiona==1.9.6`
     - `gdal==3.6.2`
     - `numpy==1.26.4`
     - `matplotlib==3.8.4`
     - `shapely==2.0.4`
     - `pyproj==3.6.1`

3. **Run Example Scripts**:
   - **Read a GeoTIFF**:
     ```bash
     python raster/read_geotiff.py
     ```
     This script reads `data/alberta_2011.tiff` and displays its dimensions and georeferencing information.

   - **Reproject a Shapefile**:
     ```bash
     python vector/reproject_vector_with_fiona.py
     ```
     This script reprojects `data/mask_satellite.shp` from its source CRS to EPSG:4326.

   - **Generate Random Points**:
     ```bash
     python vector/create_random_points_reproject.py
     ```
     This script creates `data/sample.shp` (random points in EPSG:4326) and `data/sample_3348.shp` (reprojected to EPSG:3348), along with a visualization plot.

4. **Explore the Data**:
   - Use the following Python code to inspect generated or sample data:
     ```python
     import geopandas as gpd
     gdf = gpd.read_file("data/sample_3348.shp")
     print(gdf.head())
     print("CRS:", gdf.crs)
     gdf.plot()
     import matplotlib.pyplot as plt
     plt.show()
     ```

5. **Save Your Work**:
   - Commit and push changes to the repository:
     ```bash
     git add .
     git commit -m "Added new script or data"
     git push origin main
     ```

### Local Setup (Optional)

If you prefer to run the project locally:
1. Clone the repository:
   ```bash
   git clone https://github.com/voirinprof/gis_starter_geolab.git
   cd gis_starter_geolab
   ```
2. Install dependencies using the provided `requirements.txt`:
   ```bash
   pip install -r .devcontainer/requirements.txt
   ```
3. Ensure you have `libgdal-dev` (version 3.6.2 or compatible) installed on your system. For Ubuntu:
   ```bash
   sudo apt-get update
   sudo apt-get install libgdal-dev
   ```
4. Run the scripts as described above.

Note: Local setup may require additional configuration to match the Codespaces environment, especially for geospatial libraries like GDAL.

## Dependencies

The project relies on the following Python packages (specified in `.devcontainer/requirements.txt`):
- `numpy==1.26.4`
- `rasterio==1.3.10`
- `fiona==1.9.6`
- `beautifulsoup4==4.12.3`
- `gdal==3.6.2`
- `pandas==2.2.2`
- `geopandas==0.14.4`
- `requests==2.31.0`
- `lxml==5.2.1`
- `matplotlib==3.8.4`
- `shapely==2.0.4`
- `pyproj==3.6.1`

The Codespaces environment is built using a custom Dockerfile based on `osgeo/gdal:ubuntu-full-3.6.2`, ensuring compatibility with geospatial tools.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Make your changes and test them in a Codespace or locally.
4. Commit and push your changes:
   ```bash
   git commit -m "Added new feature"
   git push origin feature/your-feature
   ```
5. Open a pull request describing your changes.

Please ensure your code follows Python best practices and includes appropriate comments.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, please open an issue on GitHub or contact the repository owner at [voirinprof](https://github.com/voirinprof).

Happy geospatial coding!