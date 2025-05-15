import sqlite3

class Site:

    def __init__(self, id = 0, tag = "", name = ""):
        self.id = id
        self.tag = tag
        self.name = name

if __name__ == "__main__":
    
    c = sqlite3.connect("model\\test.db")
    c.execute("""CREATE TABLE IF NOT EXISTS sites(
                id INTEGER PRIMARY KEY NOT NULL,
                tag TEXT UNIQUE,
                name TEXT UNIQUE
              )""")
    
    c.commit()
    c.close()