import io
import os
import pandas as pd
import requests
import zipfile

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://maven-datasets.s3.amazonaws.com/Airbnb/Airbnb+Data.zip'
    response = requests.get(url)

     # Define the dtype and parse_dates parameters
    reviews_dtypes = {
        'listing_id': pd.Int64Dtype(), 
        'review_id': pd.Int64Dtype(), 
        'reviewer_id': pd.Int64Dtype()
    }


    parse_dates = ['date']

    # Write the zipped content to a temporary file
    with open('temp.zip', 'wb') as f:
        f.write(response.content)
    # Extract the CSV file "listings.csv" from the zip file
    with zipfile.ZipFile('temp.zip', 'r') as zip_ref:
        # Get the list of files and folders in the zip file
        file_list = zip_ref.namelist()
        # Check if the nested folder structure exists
        if 'Airbnb Data/Reviews.csv' in file_list:
            # Extract the "listings.csv" file from the nested folders
            zip_ref.extract('Airbnb Data/Reviews.csv')

        df = pd.read_csv('Airbnb Data/Reviews.csv', sep=',', dtype=reviews_dtypes, parse_dates=parse_dates)


        # Here I'll adjust my fictious data date by adding 2 years to the host_since column to make it more relevant for analytics
        df['date'] = df['date'] + pd.DateOffset(years=2)
   
    # Remove the temporary zip file
    os.remove('temp.zip')

    return df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

