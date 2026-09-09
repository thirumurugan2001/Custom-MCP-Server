from helper.dbconnection import dbconnection as conn


# Function to update an existing task in the database
def update_task(task_id,task_name,task_description=None,task_deadline=None,task_status="pending",task_comment=None,task_assign=None):
    connection = None
    try:
        connection = conn()
        cur = connection.cursor()
        cur.execute("""
            UPDATE taskdetails
            SET
                task_name = %s,
                task_description = %s,
                task_deadline = %s,
                task_status = %s,
                task_comment = %s,
                task_assign = %s,
                task_updated_at = CURRENT_TIMESTAMP
            WHERE task_id = %s
            AND is_active = TRUE """, (task_name,task_description,task_deadline,task_status,task_comment,task_assign,task_id))

        connection.commit()
        rows_updated = cur.rowcount
        cur.close()
        connection.close()
        if rows_updated == 0:
            return {
                "status": "error",
                "message": "Task not found or inactive"
            }
        return {
            "status": "updated",
            "task_id": task_id
        }
    except Exception as e:
        if connection:
            connection.rollback()
        print(f"Error: Unable to update task in the database. {e}")
        return {
            "status": "error",
            "message": str(e)
        }
    finally:
        if connection:
            connection.close()