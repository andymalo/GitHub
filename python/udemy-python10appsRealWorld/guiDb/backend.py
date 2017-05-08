import sqlite3

def connect():
    """connexion à la bdd"""
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book("
                "id INTEGER PRIMARY KEY,"
                "title TEXT,"
                "author TEXT,"
                "year INTEGER,"
                "ISBN INTEGER)")
    conn.commit()
    conn.close()

def viewAll():
    """Vue de toutes les données"""
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def searchEntry(title="", author="", year="", isbn=""):
    """Recherche d'une entrée"""
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",
                (title, author, year, isbn))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def addEntry(title, author, year, isbn):
    """Ajouter une entrée"""
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",
                (title, author, year, isbn))
    conn.commit()
    conn.close()

def updateEntry(id, title, author, year, isbn):
    """Mets à jour une entrée"""
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? "
                "WHERE id = ?",
                (title, author, year, isbn, id))
    conn.commit()
    conn.close()

def delEntry(id):
    """Supprime une entrée"""
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def close():
    print("close")

connect()
addEntry("The Sun", "John Smith", 1918, 913123132)
#delEntry(6)
updateEntry(8,"TEST","TEST",2017,0000)
print(viewAll())
#print(searchEntry(author="John Smith"))