-- Docs: https://docs.mage.ai/guides/sql-blocks
-- Create a new table with the additional price_usd column
CREATE OR REPLACE TABLE airbnb_dw.listings_partitioned_transformed AS
SELECT
  *,
  CASE
    WHEN city = 'Paris' THEN price * 1.07
    WHEN city = 'New York' THEN price * 1
    WHEN city = 'Bangkok' THEN price * 0.027
    WHEN city = 'Rio de Janeiro' THEN price * 0.20
    WHEN city = 'Sydney' THEN price * 0.65
    WHEN city = 'Istanbul' THEN price * 0.031
    WHEN city = 'Rome' THEN price * 1.07
    WHEN city = 'Hong Kong' THEN price * 0.13
    WHEN city = 'Mexico City' THEN price * 0.060
    WHEN city = 'Cape Town' THEN price * 0.053
    ELSE price  -- Use original price if city is not in the conversion list
  END AS price_usd
FROM airbnb_dw.listings_partitioned_transformed;