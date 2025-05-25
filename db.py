import psycopg2
import psycopg2.extras
db_name="tasklist_db"
db_user="task_list_user"
db_password="abc123"
db_host="localhost"

def tasklist_db():
    connect = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host)
    cur = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute('SELECT task_name, due_date, is_done FROM task_list')
    tasklist=cur.fetchall()
    cur.close()
    connect.close()
    return tasklist

def add_task(task,date):
    connect = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host)
    cur = connect.cursor()
    cur.execute('INSERT INTO task_list (task_name, due_date) VALUES (%s, %s)', (task,date))
    connect.commit()
    cur.close()
    connect.close() 