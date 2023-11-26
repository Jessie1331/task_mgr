from app.database import get_db

def output_formatter(results):
    out = []
    for result in results:
        res = {
            "id":result[0],
            "summary": result[1],
            "description":result[2],
            "is_done": result[3]

        }
        out.append(res)
        return out

def scan():
    cann = get_db()
    cursor = cann.execute("SELECT * FROM task WHERE is_done=0," ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def select_by_id(task_id):
    cann = get_db()
    task_tuple = (
        task_data.get("summary")
        task_data.get("description")

    )
    statement = """
       INSERT INTO task(
        summary,
        description

       )VALUES (?,?)
       """
       cann.execute(statement,task_tuple)
       cann.commit()

def update_by_id(task_data, task_id):
    cann = get_db()
    task_tuple = (
        task_data.get("summary"),
        task_data.get("description"),
        task_data.get("is_done"),
        task_id
    )
    statement = """
        UPDATE task SET 
           summary = ?,
           description = ?,
           is_done = ?,
        WHERE id = ?
    """
    cann.execute(statment, task_tuple)
    cann.commit()

def delete_by_id(task_id):
    cann = get_db()
    cann.execute("DELETE FROM task WHERE id=?", (task_id))
    cann.commit()