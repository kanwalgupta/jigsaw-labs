WITH source AS (
    SELECT *
    FROM {{source('hubspot','northwinds_hubspot')}}
),
companies AS (
    SELECT *
    FROM {{ref('stg_hubspot_companies')}}
),
renamed AS (
    SELECT 
      CONCAT('hubspot-', hubspot_id) AS contact_id,
      first_name,
      last_name,
      REPLACE(TRANSLATE(phone, '(,),-,.', ''), ' ', '') as updated_phone,
      business_name
    FROM source
),
final AS (
    SELECT 
      contact_id AS customer_id,
      first_name,
      last_name,
      CASE WHEN LENGTH(updated_phone) = 10 THEN
       '(' || SUBSTRING(updated_phone, 1, 3) || ') ' || 
       SUBSTRING(updated_phone, 4, 3) || '-' ||
       SUBSTRING(updated_phone, 7, 4) 
       END as phone,
       companies.company_id
    FROM renamed
    INNER JOIN companies 
      ON renamed.business_name = companies.name
)
SELECT * 
FROM final