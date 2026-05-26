"""Hello World"""

from ngio import create_synthetic_ome_zarr

from fractal_atmc_measurements.atmc_analysis_feature_extraction_task import (
    atmc_analysis_feature_extraction_task,
)

test_data_path = "test_data.zarr"
shape = (1, 1, 64, 64)
axes = "czyx"

create_synthetic_ome_zarr(
    store=test_data_path,
    shape=shape,
    overwrite=True,
    axes_names=axes,
)

atmc_analysis_feature_extraction_task(
    zarr_url=test_data_path,  # Get folder from at least one well, zip to have backup.
    label_image_name="nuclei",
    output_table_name="test_output",
    overwrite=True,
)
