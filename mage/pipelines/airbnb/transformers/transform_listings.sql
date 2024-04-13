-- Docs: https://docs.mage.ai/guides/sql-blocks

CREATE OR REPLACE TABLE `airbnb-de-project.airbnb_dw.listings_partitioned_transformed`
    AS
        SELECT
        -- removing noninteresting columns
         listing_id, 
         --name, 
         host_id, 
         host_since, 
         --host_location,
         --host_response_time, 
         host_response_rate, 
         --host_acceptance_rate,
         host_is_superhost, 
         host_total_listings_count,
         host_has_profile_pic, 
         host_identity_verified, 
         neighbourhood,
         district, 
         city, 
         latitude, 
         longitude, 
         property_type,
         room_type, 
         accommodates, 
         bedrooms, 
         --amenities, 
         price,
         --minimum_nights, 
         --maximum_nights, 
         review_scores_rating,
         review_scores_accuracy, 
         review_scores_cleanliness,
         review_scores_checkin, 
         review_scores_communication,
         review_scores_location, 
         review_scores_value, 
         --instant_bookable

        FROM airbnb-de-project.airbnb_dw.listings_partitioned
        -- filtereing out listings where price is 0
        WHERE price > 0
