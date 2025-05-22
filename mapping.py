import geopandas as gpd
import matplotlib.pyplot as plt
from config import MORTALITY_MIN, MORTALITY_MAX

def plot_us_county_borders(shp_file_path):
    """
    Reads a shapefile of US county borders and plots them.

    Args:
        shp_file_path (str): Path to the shapefile (.shp) describing US county borders.
    """
    # Load the shapefile using geopandas
    counties = gpd.read_file(shp_file_path)

    # Plot the county borders
    fig, ax = plt.subplots(figsize=(12,7))
    counties.boundary.plot(ax=ax, linewidth=0.5, color='black')
    ax.set_title("US County Borders")
    ax.set_axis_off()
    # Set axis limits to focus on the continental US
    ax.set_xlim([-125, -66])
    ax.set_ylim([24, 50])
    plt.show()

def plot_county_choropleth(shp_file_path, cancer_df, county_fips_col, cancer_rate_col, cmap="Reds"):
    """
    Plots a choropleth map of US counties colored by cancer rates.

    Args:
        shp_file_path (str): Path to the shapefile (.shp) describing US county borders.
        cancer_df (pd.DataFrame): DataFrame containing cancer rates for each county.
        county_fips_col (str): Column name in cancer_df with county FIPS codes (should match shapefile).
        cancer_rate_col (str): Column name in cancer_df with cancer rates.
        cmap (str): Matplotlib colormap for the choropleth.
    """
    # Load the shapefile using geopandas
    counties = gpd.read_file(shp_file_path)

    # Ensure FIPS codes are strings and zero-padded to 5 digits
    counties["FIPS"] = counties["GEOID"].astype(str).str.zfill(5)
    cancer_df["FIPS"] = cancer_df[county_fips_col].astype(str).str.zfill(5)

    # Merge cancer rates into the counties GeoDataFrame
    merged = counties.merge(cancer_df, on="FIPS", how="left")

    # Plot the choropleth
    fig, ax = plt.subplots(figsize=(12, 7))
    # Plot the choropleth without legend, but capture the collection for colorbar
    collection = merged.plot(
        column=cancer_rate_col,
        cmap=cmap,
        linewidth=0.1,
        ax=ax,
        edgecolor='0.5',
        legend=False,
        missing_kwds={
            "color": "lightgrey",
            "label": "No data"
        }
    )

    # Add a colorbar
    sm = plt.cm.ScalarMappable(
        cmap=cmap,
        norm=plt.Normalize(
            vmin=MORTALITY_MIN,
            vmax=MORTALITY_MAX
        )
    )
    sm._A = []
    cbar = fig.colorbar(sm, ax=ax, fraction=0.03, pad=0.04)
    cbar.set_label(cancer_rate_col)
    ax.set_title("US County Cancer Rates")
    ax.set_axis_off()

    # Set axis limits to focus on the continental US
    ax.set_xlim([-125, -66])
    ax.set_ylim([24, 50])

    plt.show()


# Example usage:
# plot_us_county_borders("C://Users/aronsonms/Downloads/tl_2022_us_county/tl_2022_us_county.shp")
# plot_us_county_borders("maps/tl_2022_us_county.shp")