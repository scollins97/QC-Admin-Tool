#all SQL related queries
import sqlite3
import os

#this is where the QC database is located. 
path = "O:\\Common Files\\Inspector Selector\\QC-Inspector-Selector-3000-main\\QC-Inspector-Selector-3000-main\\QCdb.db"

def fetchAllInspectors():
    #create a connection to the database
    conn = sqlite3.connect(f"{path}")
    #create a cursor object. this allows queries to be made
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inspectors")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
def insertNewInspector(id, InspName):
    #should be recieving their employee number and name
    #create a connection to the database
    conn = sqlite3.connect(f"{path}")
    #create a cursor object. this allows queries to be made
    cursor = conn.cursor()
    cursor.execute("INSERT INTO inspectors(id, name, score) VALUES (?, ?, ?)", (id, InspName, 0))
    conn.commit()
    cursor.close()
    conn.close()
def resetScoresToZero() :
    #ceate a connection to the database
    conn = sqlite3.connect(f"{path}")
    #create a cursor object. this allows queries to be made
    cursor = conn.cursor()
    #execute the SQL query
    cursor.execute("UPDATE inspectors SET score = 0")
    #commit changes to database
    conn.commit()
    #close cursor
    cursor.close()
    #close the connection
    conn.close()
def deleteInspector(id):
    #ceate a connection to the database
    conn = sqlite3.connect(f"{path}")
    #create a cursor object. this allows queries to be made
    cursor = conn.cursor()
    #execute the SQL query
    cursor.execute("DELETE FROM inspectors WHERE id = ?", (id,))
    #commit changes to database
    conn.commit()
    #close cursor
    cursor.close()
    #close the connection
    conn.close()