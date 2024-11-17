import ee
import os

# Authenticate and initialize Google Earth Engine
ee.Authenticate()
ee.Initialize(project='geotiff09')


def download_forest_cover_tiff(longitude_min, latitude_min, longitude_max, latitude_max, output_directory):
    """
    Downloads a GeoTIFF image showing the percentage of forest cover in the specified bounding box using Google Earth Engine.

    Args:
        longitude_min (float): Minimum longitude of the bounding box.
        latitude_min (float): Minimum latitude of the bounding box.
        longitude_max (float): Maximum longitude of the bounding box.
        latitude_max (float): Maximum latitude of the bounding box.
        output_directory (str): Directory to save the downloaded TIFF file.
    """
    try:
        # Define the area of interest (AOI)
        aoi = ee.Geometry.Rectangle([longitude_min, latitude_min, longitude_max, latitude_max])

        # Load MODIS Vegetation Continuous Fields dataset for tree cover percentage
        modis_vcf = ee.ImageCollection('MODIS/006/MOD44B') \
            .filterDate('2020-01-01', '2020-12-31') \
            .first()

        # Select the 'Percent_Tree_Cover' band, which shows the percentage of tree cover
        tree_cover = modis_vcf.select('Percent_Tree_Cover').clip(aoi)

        # Set a threshold for forest cover, e.g., areas with >20% tree cover
        forest_cover = tree_cover.gt(20).selfMask()

        # Configure export parameters
        scale = 500  # 500-meter resolution
        task = ee.batch.Export.image.toDrive(
            image=forest_cover,
            description='Europe_Forest_Cover',
            folder='EarthEngine',
            fileNamePrefix='europe_forest_cover',
            scale=scale,
            region=aoi.getInfo()['coordinates'],
            crs='EPSG:4326'
        )
        task.start()

        print("Export task started. Check your Google Drive for the downloaded image.")
    except Exception as e:
        print(f"Error: {e}")


# Define parameters for Europe
longitude_min = -10.0
latitude_min = 35.0
longitude_max = 40.0
latitude_max = 70.0
output_directory = '/Users/rishinpandit/Desktop/InternetApplied/Project/EcoGuard-Backend/env_monitoring_project/ai_models'

# Create output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Run the script
download_forest_cover_tiff(longitude_min, latitude_min, longitude_max, latitude_max, output_directory)
