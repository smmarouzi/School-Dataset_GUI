# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 18:08:15 2018

@author: mm
"""
import sqlite3
import os

os.chdir('F:\RudyProject')

def connect():
    """ Make connection to an SQLite inf file """
    conn = sqlite3.connect("inf.db")
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS StuInfo (id INTEGER PRIMARY KEY, Student_Name TEXT, Hours_bought INTEGER,First_class TEXT,Grade INTEGER, Subject1 TEXT, Subject2 TEXT, Subject3 TEXT, Days_of_attendance INTEGER, Hours_of_attendance INTEGER, Comments TEXT )')
    conn.commit()
    conn.close()
    
    

def insert(Student_Name,Hours_bought,First_class,Grade,Subject1,Subject2,Subject3,Days_of_attendance,Hours_of_attendance,Comments):

    conn = sqlite3.connect("inf.db")
    cur = conn.cursor()
    cur.execute('INSERT INTO StuInfo VALUES (NULL,?,?,?,?,?,?,?,?,?,?)'
                ,(Student_Name,Hours_bought,First_class,Grade,Subject1,Subject2,Subject3,Days_of_attendance,Hours_of_attendance,Comments))
    conn.commit()
    conn.close()
 
def view():
    conn = sqlite3.connect("inf.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM StuInfo')
    rows=cur.fetchall()
    conn.close()
    return rows

def search(Student_Name="",Hours_bought="",First_class="",Grade="",Subject1="",Subject2="",Subject3="",Days_of_attendance="",Hours_of_attendance="",Comments=""):
    conn = sqlite3.connect("inf.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM StuInfo WHERE Student_Name=? OR Hours_bought=? OR First_class=? OR Grade=? OR Subject1=? OR Subject2=? OR Subject3=? OR Days_of_attendance=? OR Hours_of_attendance=? OR Comments=?'
                ,(Student_Name,Hours_bought,First_class,Grade,Subject1,Subject2,Subject3,Days_of_attendance,Hours_of_attendance,Comments))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("inf.db")
    cur = conn.cursor()
    cur.execute('DELETE FROM StuInfo WHERE id=?',(id,))
    conn.commit()
    conn.close()

def update(id,Student_Name,Hours_bought,First_class,Grade,Subject1,Subject2,Subject3,Days_of_attendance,Hours_of_attendance,Comments):
    conn = sqlite3.connect("inf.db")
    cur = conn.cursor()
    cur.execute('UPDATE StuInfo SET Student_Name=?, Hours_bought=?, First_class=?, Grade=?, Subject1=?, Subject2=?, Subject3=?, Days_of_attendance=?, Hours_of_attendance=?, Comments=? WHERE id=?'
                ,(Student_Name,Hours_bought,First_class,Grade,Subject1,Subject2,Subject3,Days_of_attendance,Hours_of_attendance,Comments,id))
    conn.commit()
    conn.close()
    


#connect()
#insert("Sau",2,"ffggg",7,"fdf","ff","efwef",3,4,"efsdf")
#update(6,'Samaneh',22,'Math',5,'Math','Python','English',10,20,'Good Student')
#print(view())












