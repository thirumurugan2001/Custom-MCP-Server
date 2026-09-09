from helper.dbconnection import dbconnection as conn
from psycopg2.extras import RealDictCursor

# Function to read all active tasks from the database
def read_tasks():
    connection = None
    try:
        connection = conn()
        cur = connection.cursor(cursor_factory=RealDictCursor)
        cur.execute("""
            SELECT
                task_id,
                task_name,
                task_description,
                task_deadline,
                task_status,
                task_comment,
                task_assign,
                task_created_at,
                task_updated_at,
                is_active
            FROM taskdetails WHERE is_active = TRUE ORDER BY task_created_at DESC """)
        rows = cur.fetchall()
        cur.close()
        connection.close()
        return rows
    except Exception as e:
        print(f"Error: Unable to read tasks from the database. {e}")
        return []
    finally:
        if connection:
            connection.close()