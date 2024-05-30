import psycopg2
from psycopg2 import sql
from contextlib import contextmanager

@contextmanager
def get_connection():
    conn = psycopg2.connect(
        name='name_db',
        user='user_db',
        password='password_db',
        host='host_db',
        port='port_db'
    )
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS notes (
                    id SERIAL PRIMARY KEY,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()

def add_note(content):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('INSERT INTO notes (content) VALUES (%s)', (content,))
            conn.commit()

def get_notes():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT id, content, created_at FROM notes ORDER BY created_at DESC')
            notes = cursor.fetchall()
            return notes

def update_note(note_id, new_content):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('UPDATE notes SET content = %s WHERE id = %s', (new_content, note_id))
            conn.commit()

def delete_note(note_id):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('DELETE FROM notes WHERE id = %s', (note_id,))
            conn.commit()
