import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / 'data' / 'students.db'

class Database:
    def __init__(self, path=DB_PATH):
        self.path = str(path); self.initialize()

    def connect(self):
        con = sqlite3.connect(self.path); con.row_factory = sqlite3.Row; return con

    def initialize(self):
        with self.connect() as con:
            con.execute('''CREATE TABLE IF NOT EXISTS students (
                reg_no INTEGER PRIMARY KEY, name TEXT NOT NULL, subject1 INTEGER NOT NULL,
                subject2 INTEGER NOT NULL, subject3 INTEGER NOT NULL)''')

    def add(self, reg_no, name, marks):
        with self.connect() as con:
            con.execute('INSERT INTO students VALUES (?,?,?,?,?)', (reg_no,name,*marks))

    def update(self, reg_no, name, marks):
        with self.connect() as con:
            con.execute('UPDATE students SET name=?,subject1=?,subject2=?,subject3=? WHERE reg_no=?', (name,*marks,reg_no))

    def delete(self, reg_no):
        with self.connect() as con: con.execute('DELETE FROM students WHERE reg_no=?',(reg_no,))

    def get(self, reg_no):
        with self.connect() as con: return con.execute('SELECT * FROM students WHERE reg_no=?',(reg_no,)).fetchone()

    def all(self):
        with self.connect() as con: return con.execute('SELECT * FROM students ORDER BY reg_no').fetchall()
