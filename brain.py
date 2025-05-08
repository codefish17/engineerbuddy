import sqlite3
from model import job
from model import task

class Brain:

    def __init__(self):
        self.db_connection = sqlite3.connect("model\\test.db")

if __name__ == "__main__":
    my_brain = Brain()

    # j = job.Job()
    # j.name = "testrow2"
    # j.CreateJob(my_brain.db_connection)

    cur = my_brain.db_connection.cursor()

    res = cur.execute("PRAGMA table_xinfo(Jobs)")

    print(res.fetchall())

    my_brain.db_connection.close()

    


