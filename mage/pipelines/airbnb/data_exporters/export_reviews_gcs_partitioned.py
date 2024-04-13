import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "./keys/my-creds.json"

bucket_name = 'airbnb-data-lake'
project_id = 'airbnb-de-project'

table_name = "airbnb-reviews"

root_path = f"{bucket_name}/{table_name}"

@data_exporter
def export_data(data, *args, **kwargs):
    data['date'] = pd.to_datetime(data['date'])
    data['year'] = data['date'].dt.year  # Extract the year from the date


    table = pa.Table.from_pandas(data)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['year'],
        filesystem=gcs
    )