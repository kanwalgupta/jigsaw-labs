WITH source AS (
    SELECT business_name
    FROM {{source('hubspot','northwinds_hubspot')}}
),
renamed AS (
    SELECT 
      --CONCAT('hubspot-',LOWER(REPLACE(business_name,' ','-'))) AS company_id,
      CONCAT('hubspot-',LOWER(REPLACE(TRANSLATE(business_name,',',''),' ','-'))) AS company_id,
      business_name AS name
    FROM source
    GROUP BY name
)
SELECT *
FROM renamed