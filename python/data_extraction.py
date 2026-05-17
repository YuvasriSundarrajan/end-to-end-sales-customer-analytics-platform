import pandas as pd
from db_connection import get_engine

def load_customers():
    query = """
    SELECT customer_id, customer_name, signup_date
    FROM customers
    """
    return pd.read_sql(query, get_engine())

def load_orders():
    query = """
    SELECT 
        o.order_id,
        o.customer_id,
        oi.quantity,
        p.price
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id
    """
    return pd.read_sql(query, get_engine())
