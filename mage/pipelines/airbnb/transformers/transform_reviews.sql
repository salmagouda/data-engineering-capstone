-- Docs: https://docs.mage.ai/guides/sql-blocks

CREATE OR REPLACE TABLE `airbnb-de-project.airbnb_dw.reviews_partitioned_transformed`
AS
SELECT
    r.*,
    agg.listing_review_count
FROM
    airbnb-de-project.airbnb_dw.reviews_partitioned r
JOIN (
    SELECT
        listing_id,
        COUNT(review_id) AS listing_review_count
    FROM
        airbnb-de-project.airbnb_dw.reviews_partitioned
    GROUP BY
        listing_id
) agg ON r.listing_id = agg.listing_id;


