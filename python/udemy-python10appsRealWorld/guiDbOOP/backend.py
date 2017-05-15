import sqlite3

class Database:
    """
    Classe base de données
    """
    def __init__(self, db):
        """connexion à la bdd"""
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book("
                         "id INTEGER PRIMARY KEY,"
                         "title TEXT,"
                         "author TEXT,"
                         "year INTEGER,"
                         "ISBN INTEGER)")
        self.conn.commit()

    def viewAll(self):
        """Vue de toutes les données"""
        #conn = sqlite3.connect("books.db")
        #cur = conn.cursor()
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def searchEntry(self, title="", author="", year="", isbn=""):
        """Recherche d'une entrée"""
        self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",
                         (title, author, year, isbn))
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows

    def addEntry(self, title, author, year, isbn):
        """Ajouter une entrée"""
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",
                         (title, author, year, isbn))
        self.conn.commit()

    def updateEntry(self, id, title, author, year, isbn):
        """Mets à jour une entrée"""
        self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? "
                         "WHERE id = ?",
                         (title, author, year, isbn, id))
        self.conn.commit()

    def delEntry(self, id):
        """Supprime une entrée"""
        self.cur.execute("DELETE FROM book WHERE id = ?", (id,))
        self.conn.commit()

    def close(self):
        print("close")
        self.conn.close()
        
    def __del__(self):
        self.conn.close()