SELECT
    O.ORDER_ID,
    O.CUSTOMER_ID,
    C.NAME,
    O.ORDER_DATE,
    O.TOTAL_AMOUNT
FROM {{ ref('stg_orders') }} O
JOIN {{ ref('stg_customers') }} C
  ON O.CUSTOMER_ID = C.CUSTOMER_ID