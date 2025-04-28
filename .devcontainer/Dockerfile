# Base image Python 3.11
FROM mcr.microsoft.com/devcontainers/python:3.11

# Install OS dependencies for GDAL, Fiona, Rasterio, GeoPandas
RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    libproj-dev \
    proj-data \
    proj-bin \
    libgeos-dev \
    && rm -rf /var/lib/apt/lists/*

# Set GDAL version environment variable (important for pip)
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal
ENV GDAL_VERSION=3.6.2
