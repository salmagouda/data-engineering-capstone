-- Docs: https://docs.mage.ai/guides/sql-blocks
CREATE OR REPLACE TABLE `airbnb-de-project.airbnb_dw.airbnb_data`
    AS
        SELECT 
            l.*,
            r.review_id,
            r.reviewer_id,
            r.date AS review_date,
            r.listing_review_count 
        FROM `airbnb-de-project.airbnb_dw.listings_partitioned_transformed` l
        JOIN `airbnb-de-project.airbnb_dw.reviews_partitioned_transformed` r
            ON l.listing_id = r.listing_id;