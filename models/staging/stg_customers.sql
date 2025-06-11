SELECT
    CUSTOMER_ID,
    NAME,
    EMAIL,
    SIGNUP_DATE
FROM {{ source('raw', 'customers_raw') }}
