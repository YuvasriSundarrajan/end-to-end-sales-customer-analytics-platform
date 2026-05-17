CREATE OR REPLACE VIEW vw_customer_risk AS
SELECT
    customer_id,
    customer_name,
    total_revenue,
    total_orders,
    loyalty_months,
    customer_value_score,
    risk_level
FROM customer_value_python;

CREATE OR REPLACE VIEW vw_sales_detailed AS
SELECT
    c.customer_id,
    c.customer_name,
    c.city,
    c.signup_date,
    o.order_id,
    o.order_date,
    p.product_id,
    p.product_name,
    p.category,
    p.price,
    p.cost,
    oi.quantity,
    (oi.quantity * p.price) AS revenue,
    (oi.quantity * (p.price - p.cost)) AS profit,
    pay.payment_method,
    pay.payment_status,
    vr.loyalty_months,
    vr.customer_value_score,
    vr.risk_level
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
LEFT JOIN payments pay ON o.order_id = pay.order_id
LEFT JOIN vw_customer_risk vr ON c.customer_id = vr.customer_id;