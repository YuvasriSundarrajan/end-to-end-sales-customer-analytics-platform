from db_connection import get_engine

try:
    engine = get_engine()
    conn = engine.connect()
    print("✅ Python connected to MySQL successfully")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)
