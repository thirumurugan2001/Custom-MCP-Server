from helper.dbconnection import dbconnection as conn
from psycopg2.extras import RealDictCursor

# Function to get the schema of the taskdetails table
def get_task_table_schema():
    connection = None
    try:
        connection = conn()
        cur = connection.cursor(cursor_factory=RealDictCursor)
        cur.execute("""
            SELECT
                column_name,
                data_type,
                is_nullable,
                column_default
            FROM information_schema.columns
            WHERE table_schema = 'public'
              AND table_name = 'taskdetails'
            ORDER BY ordinal_position
        """)
        schema = cur.fetchall()
        cur.close()
        connection.close()
        return schema
    except Exception as e:
        print(f"Error: Unable to get task table schema. {e}")
        return []
    finally:
        if connection:
            connection.close()
