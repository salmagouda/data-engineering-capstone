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
    listings_dtypes = {
        'listing_id': pd.Int64Dtype(), 
        'name': str, 
        'host_id': pd.Int64Dtype(), 
        'host_location': str,
        'host_response_time': str, 
        'host_response_rate': float, 
        'host_acceptance_rate': float,
        'host_is_superhost': str, 
        'host_total_listings_count': pd.Int64Dtype(),
        'host_has_profile_pic': str, 
        'host_identity_verified': str, 
        'neighbourhood': str,
        'district': str, 
        'city': str, 
        'latitude': float, 
        'longitude': float, 
        'property_type': str,
        'room_type': str, 
        'accommodates': pd.Int64Dtype(), 
        'bedrooms': pd.Int64Dtype(), 
        'amenities': str, 
        'price': pd.Int64Dtype(),
        'minimum_nights': pd.Int64Dtype(), 
        'maximum_nights': pd.Int64Dtype(), 
        'review_scores_rating': pd.Int64Dtype(),
        'review_scores_accuracy': pd.Int64Dtype(), 
        'review_scores_cleanliness': pd.Int64Dtype(),
        'review_scores_checkin': pd.Int64Dtype(), 
        'review_scores_communication': pd.Int64Dtype(),
        'review_scores_location': pd.Int64Dtype(), 
        'review_scores_value': pd.Int64Dtype(), 
        'instant_bookable': str
    }


    parse_dates = ['host_since']

    # Write the zipped content to a temporary file
    with open('temp.zip', 'wb') as f:
        f.write(response.content)
    # Extract the CSV file "listings.csv" from the zip file
    with zipfile.ZipFile('temp.zip', 'r') as zip_ref:
        # Get the list of files and folders in the zip file
        file_list = zip_ref.namelist()
        # Check if the nested folder structure exists
        if 'Airbnb Data/Listings.csv' in file_list:
            # Extract the "listings.csv" file from the nested folders
            zip_ref.extract('Airbnb Data/Listings.csv')

        df = pd.read_csv('Airbnb Data/Listings.csv', encoding='ISO-8859-1', sep=',', dtype=listings_dtypes, parse_dates=parse_dates)


        # Here I'll adjust my fictious data date by adding 2 years to the host_since column to make it more relevant for analytics
        df['host_since'] = df['host_since'] + pd.DateOffset(years=2)
   
    # Remove the temporary zip file
    os.remove('temp.zip')

    return df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
