-- Docs: https://docs.mage.ai/guides/sql-blocks

CREATE OR REPLACE TABLE `airbnb-de-project.airbnb_dw.reviews_partitioned`
    PARTITION BY DATE_TRUNC(date, MONTH)
    CLUSTER BY listing_id AS
        SELECT * FROM `airbnb-de-project.airbnb_dw.reviews`;