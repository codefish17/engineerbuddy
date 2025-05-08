import sqlite3

class Job:

    table_columns = ["id", "name", "description", "requestor", "date_created", "date_due"]

    def __init__(self, id = "", name = "", description ="", requestor = "", date_created = "", date_due = "", is_complete=False, tasks = []):
        self.id = id
        self.name = name
        self.description = description
        self.requestor = requestor
        self.date_created = date_created
        self.date_due = date_due
        self.is_complete = is_complete
        self.tasks = tasks

    def CreateJob(self, connection):
        cur = connection.cursor()
        params = (self.name, self.description, self.requestor, self.date_created, self.date_due)
        sql_str = """INSERT INTO Jobs (name, description, requestor, date_created, date_due) VALUES (?,?,?,?,?)"""
        cur.execute(sql_str, params)
        connection.commit()

    @staticmethod 
    def GetJob(connection, id) -> list:
        cur = connection.cursor()
        res = cur.execute("SELECT * FROM Jobs WHERE id=?", (id,))

        return res.fetchall()
    
    @staticmethod
    def GetJobs(connection) -> list:
        cur = connection.cursor()
        res = cur.execute("SELECT * FROM Jobs")

        return res.fetchall()
    
    @staticmethod
    def UpdateJob(connection, id, column, value):
        pass
        
    @staticmethod
    def DeleteJob(connection, id):
        cur = connection.cursor()
        cur.execute("DELETE FROM Jobs WHERE id=?", (id,))
        connection.commit()

if __name__ == "__main__":
    con = sqlite3.connect('model\\test.db')
    cur = con.cursor()
    
    # con.execute("DROP TABLE Jobs")

    # con.execute("""CREATE TABLE Jobs(
    #             id INTEGER PRIMARY KEY NOT NULL,
    #             name TEXT UNIQUE NOT NULL,
    #             description TEXT,
    #             requestor TEXT,
    #             date_created TEXT,
    #             date_due TEXT)""")
    
    con.commit()
    con.close()


