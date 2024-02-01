WITH source AS (
    SELECT *
    FROM suppliers
),
renamed AS (
    SELECT
      supplier_id,
      company_name,
      split_part(contact_name, ' ', 1) AS first_name,
      split_part(contact_name, ' ', 2) AS last_name,
      contact_title,
      address,
      city,
      region,
      postal_code,
      country,
      phone,
      fax,
      homepage
    FROM source
)
SELECT * FROM renamed