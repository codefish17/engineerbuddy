import sqlite3

class Task:
    
    def __init__(self, id="", description="", date_created="", date_due="", parent_Task = "", parent_task = "", is_complete=False):
        self.id = id
        self.description = description
        self.date_created = date_created
        self.date_due = date_due
        self.is_complete = is_complete

    def CreateTask(self, connection):
        cur = connection.cursor()
        params = (self.name, self.description, self.requestor, self.date_created, self.date_due)
        sql_str = """INSERT INTO Tasks (name, description, requestor, date_created, date_due) VALUES (?,?,?,?,?)"""
        cur.execute(sql_str, params)
        connection.commit()

    @staticmethod 
    def GetTask(connection, id) -> list:
        cur = connection.cursor()
        res = cur.execute("SELECT * FROM Tasks WHERE id=?", (id,))

        return res.fetchall()
    
    @staticmethod
    def GetTasks(connection) -> list:
        cur = connection.cursor()
        res = cur.execute("SELECT * FROM Tasks")

        return res.fetchall()
    
    @staticmethod
    def UpdateTask(connection, id, column, value) -> bool:
        cur = connection.cursor()

        for row in cur.execute("PRAGMA table_xinfo(Tasks)"):
            if column == row[1]:
                cur.execute(f"UPDATE Tasks SET {column} = ? WHERE id=?", (value, id))
                return True
        
        return False

    @staticmethod
    def DeleteTask(connection, id):
        cur = connection.cursor()
        cur.execute("DELETE FROM Tasks WHERE id=?", (id,))
        connection.commit()

if __name__ == "__main__":
    con = sqlite3.connect('model\\test.db')
    cur = con.cursor()
    
    # con.execute("DROP TABLE Tasks")

    # con.execute("""CREATE TABLE Tasks(
    #             id INTEGER PRIMARY KEY NOT NULL,
    #             description TEXT UNIQUE NOT NULL,
    #             date_created_TEXT,
    #             date_due TEXT,
    #             parent_Task INTEGER NOT NULL,
    #             parent_task INTEGER,
    #             is_complete INTEGER NOT NULL,
    #             FOREIGN KEY (parent_Task) REFERENCES Tasks(id),
    #             FOREIGN KEY (parent_task) REFERENCES Tasks(id)
    #             )""")
    
    con.commit()
    con.close()