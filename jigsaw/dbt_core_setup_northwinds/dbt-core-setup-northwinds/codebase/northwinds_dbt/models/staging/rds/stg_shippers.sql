WITH source AS (
    SELECT 
      shipper_id,
      company_name
    FROM shippers
)
SELECT * FROM source