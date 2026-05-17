import pandas as pd

def calculate_customer_metrics(customers, orders):
    orders["revenue"] = orders["quantity"] * orders["price"]

    agg_orders = (
        orders
        .groupby("customer_id")
        .agg(
            total_revenue=("revenue", "sum"),
            total_orders=("order_id", "nunique")
        )
        .reset_index()
    )

    df = customers.merge(agg_orders, on="customer_id", how="left").fillna(0)

    df["signup_date"] = pd.to_datetime(df["signup_date"])

    df["loyalty_months"] = (
        (pd.Timestamp.today() - df["signup_date"]).dt.days // 30
    )

    df["customer_value_score"] = (
        df["total_revenue"] * 0.6 +
        df["total_orders"] * 0.3 +
        df["loyalty_months"] * 0.1
    )

    return df


