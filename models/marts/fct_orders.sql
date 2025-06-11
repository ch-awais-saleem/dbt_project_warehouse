SELECT
    o.order_id,
    o.customer_id,
    c.name,
    o.order_date,
    o.total_amount
FROM {{ ref('stg_orders') }} o
JOIN {{ ref('stg_customers') }} c
  ON o.customer_id = c.customer_id
