-- Docs: https://docs.mage.ai/guides/sql-blocks

CREATE OR REPLACE TABLE `airbnb-de-project.airbnb_dw.listings_partitioned`
    PARTITION BY DATE_TRUNC(host_since, MONTH)
    CLUSTER BY city AS
        SELECT * FROM `airbnb-de-project.airbnb_dw.listings`;