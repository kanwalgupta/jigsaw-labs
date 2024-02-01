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
      --phone,
      fax,
      homepage
    FROM source
),
phone_digits AS (
    SELECT 
      supplier_id,
      REGEXP_REPLACE(phone, '[^0-9]', '', 'g')  AS phone_digits,
      LENGTH(REGEXP_REPLACE(phone, '[^0-9]', '', 'g')) AS phone_length
    FROM source  
),
valid_phone AS (
    SELECT
      supplier_id, 
      CONCAT(
        '(',
        SUBSTR(phone_digits,1,3),
        ')',
        ' ',
        SUBSTR(phone_digits,4,3),
        '-',
        SUBSTR(phone_digits,6,4)
      ) AS phone
    FROM phone_digits
    WHERE phone_length = 10
)
SELECT renamed.*, valid_phone.phone
FROM renamed
  INNER JOIN valid_phone 
  ON renamed.supplier_id = valid_phone.supplier_id
