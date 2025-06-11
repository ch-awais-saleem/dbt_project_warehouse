SELECT
    customer_id,
    name,
    email,
    signup_date
FROM {{ source('raw', 'customers_raw') }}
