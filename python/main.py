from data_extraction import load_customers, load_orders
from feature_engineering import calculate_customer_metrics
from revenue_risk_model import assign_risk
from export_to_mysql import export_customer_metrics

def main():
    try:
        customers = load_customers()
        orders = load_orders()

        metrics = calculate_customer_metrics(customers, orders)

        metrics["risk_level"] = metrics["customer_value_score"].apply(assign_risk)

        export_customer_metrics(metrics)

        print("✅ Data pipeline executed successfully.")

    except Exception as e:
        print("❌ Pipeline failed:", e)

if __name__ == "__main__":
    main()
