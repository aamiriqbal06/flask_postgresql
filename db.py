import psycopg2
import psycopg2.extras
db_name="postgres"
db_user="postgres.ykmdauexsqwnylxqzzzn"
db_password="Supabasewhatsapp06"
port="5432", 
db_host="aws-0-ap-south-1.pooler.supabase.com"

def tasklist_db():
    connect = psycopg2.connect(dbname=db_name, user=db_user, password=db_password,  port="5432",  host=db_host)
    cur = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute('SELECT id, task_name, due_date, is_done FROM task_list')
    tasklist=cur.fetchall()
    cur.close()
    connect.close()
    return tasklist

def add_task(task,date):
    connect = psycopg2.connect(dbname=db_name, user=db_user,  port="5432",  password=db_password, host=db_host)
    cur = connect.cursor()
    cur.execute('INSERT INTO task_list (task_name, due_date) VALUES (%s, %s)', (task,date))
    connect.commit()
    cur.close()
    connect.close()

def update_call( utask, udate,uid):
    connect = psycopg2.connect(dbname=db_name, user=db_user,  port="5432",  password=db_password, host=db_host)
    cur= connect.cursor()
    print(utask,udate,uid)
    cur.execute('UPDATE task_list SET task_name=%s, due_date=%s WHERE id=%s ', (utask, udate, uid))
    connect.commit()
    cur.close()
    connect.close()

def delete_call(uid):
    connect=psycopg2.connect(dbname=db_name, user=db_user,  port="5432",  password=db_password, host=db_host)
    cur=connect.cursor()
    cur.execute('DELETE FROM task_list WHERE id=%s', (uid,))
    connect.commit()
    cur.close()
    connect.close()
