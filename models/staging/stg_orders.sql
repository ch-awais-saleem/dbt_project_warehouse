SELECT
    ORDER_ID,
    CUSTOMER_ID,
    ORDER_DATE,
    TOTAL_AMOUNT
FROM {{ source('raw', 'orders_raw') }}
