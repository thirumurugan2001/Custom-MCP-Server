from helper.dbconnection import dbconnection as conn

# Function to insert a new task into the database
def insert_task(task_name,task_description=None,task_deadline=None,task_status="pending",task_comment=None,task_assign=None):
    connection = None
    try:
        connection = conn()
        cur = connection.cursor()
        cur.execute("""
            INSERT INTO taskdetails (
                task_name,
                task_description,
                task_deadline,
                task_status,
                task_comment,
                task_assign
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING task_id """, (task_name,task_description,task_deadline,task_status,task_comment,task_assign))

        task_id = cur.fetchone()[0]
        connection.commit()
        cur.close()
        connection.close()
        return {
            "status": "inserted",
            "task_id": str(task_id)
        }
    except Exception as e:
        if connection:
            connection.rollback()
        print(f"Error: Unable to insert task into the database. {e}")
        return {
            "status": "error",
            "message": str(e)
        }
    finally:
        if connection:
            connection.close()

