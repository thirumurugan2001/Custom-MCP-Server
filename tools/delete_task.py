from helper.dbconnection import dbconnection as conn

# Function to delete a task from the database
def delete_task(task_id):
    connection = None
    try:
        connection = conn()
        cur = connection.cursor()
        cur.execute("""UPDATE taskdetails SET is_active = FALSE, task_updated_at = CURRENT_TIMESTAMP WHERE task_id = %s AND is_active = TRUE """, (task_id,))
        connection.commit()
        rows_updated = cur.rowcount
        cur.close()
        connection.close()
        if rows_updated == 0:
            return {
                "status": "error",
                "message": "Task not found or already deleted"
            }
        return {
            "status": "deleted",
            "task_id": task_id
        }
    except Exception as e:
        if connection:
            connection.rollback()
        print(f"Error: Unable to delete task from the database. {e}")
        return {
            "status": "error",
            "message": str(e)
        }
    finally:
        if connection:
            connection.close()
