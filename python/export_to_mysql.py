from db_connection import get_engine

def export_customer_metrics(df):
    engine = get_engine()

    df_to_save = df[
        [
            "customer_id",
            "customer_name",
            "total_revenue",
            "total_orders",
            "loyalty_months",
            "customer_value_score",
            "risk_level"
        ]
    ]

    df_to_save.to_sql(
        "customer_value_python",
        engine,
        if_exists="replace",
        index=False
    )

    print("Customer analytics exported to MySQL successfully.")
