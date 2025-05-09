import sqlite3
from model.job import Job
from model.task import Task

class Brain:

    def __init__(self):
        self.db_connection = sqlite3.connect("model\\test.db")


#CODE 

if __name__ == "__main__":
    my_brain = Brain()
    my_brain.db_connection.close()

    