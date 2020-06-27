import sqlite3
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS store (id INTEGER PRIMARY KEY, product TEXT, "
                    "seller TEXT, price INTEGER, qty INTEGER, u_id INTEGER)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS users (u_id INTEGER PRIMARY KEY, name TEXT, "
                    "password TEXT)")
        self.conn.commit()

    def insert(self,product, seller, price, qty):
        #the NULL parameter is for the auto-incremented id
        self.cur.execute("INSERT INTO store VALUES(NULL,?,?,?,?)", (product,seller,price,qty))
        self.conn.commit()



    def view(self):
        self.cur.execute("SELECT * FROM store")
        rows = self.cur.fetchall()

        return rows

    def search(self,product="", seller="", price="", qty=""):
        self.cur.execute("SELECT * FROM store WHERE product = ? OR seller = ? OR price = ? "
                    "OR qty = ?", (product, seller, price, qty))
        rows = self.cur.fetchall()
        #conn.close()
        return rows

    def delete(self,id1):
        
        self.cur.execute("DELETE FROM store WHERE product = ?", (id1,))
        self.conn.commit()
        
            
        #conn.close()

    def update(self,id, product, seller, price, qty):
        self.cur.execute("UPDATE store SET product = ?, seller = ?, price = ?, qty = ? WHERE id = ?", (product, seller, price, qty, id))
        self.conn.commit()

    #destructor-->now we close the connection to our database here
    def __del__(self):
        self.conn.close()
