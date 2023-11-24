#!/usr/bin/env python
# coding: utf-8

# In[22]:


import psycopg2
import datetime


# In[77]:


#COMP 3005 A4 Q1
#Daniel Yang 101194970

#getAllStudents(): Retrieves and displays all records from the students table.
def getAllStudents():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
   
#addStudent(first_name, last_name, email, enrollment_date): Inserts a new student record into the students table.     
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO students(first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (first_name, last_name, email, enrollment_date))
        print(cursor.statusmessage)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()

#updateStudentEmail(student_id, new_email): Updates the email address for a student with the specified student_id
def updateStudentEmail(student_id, new_email):
    try:
        cursor = conn.cursor()
        sql = "UPDATE students SET email = (%s) WHERE student_id = (%s)"
        cursor.execute(sql, (new_email, student_id))
        print(cursor.statusmessage)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
        
#deleteStudent(student_id): Deletes the record of the student with the specified student_id.
def deleteStudent(student_id):
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM students WHERE student_id = (%s)"
        cursor.execute(sql, (student_id,))
        print(cursor.statusmessage)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()


# In[ ]:


if __name__ == '__main__':
    conn = psycopg2.connect("dbname=postgres user=postgres password=admin")
    while(1):
        print("Database Application")
        print("There are 5 options: ")
        print("1: Get all students")
        print("2: Add a student")
        print("3: Update a student email")
        print("4: Delete a student")
        print("5: Exit")
        
        choice = input("Please make a selection: ")
        
        if choice == '1':
            getAllStudents()
        elif choice == '2':
            firstName = input("Please enter a first name: ")
            print("")
            lastName = input("please enter a last name: ")
            print("")
            email = input("Please enter an email: ")
            print("")
            enrollmentDate = input("Please enter a date in YYYY-MM-DD format: ")
            print("")
            addStudent(firstName, lastName, email, enrollmentDate)
        elif choice == '3':
            studentId = input("Please enter a student id: ")
            print("")
            email = input("Please enter an email: ")
            print("")
            updateStudentEmail(studentId, email)
        elif choice == '4':
            studentId = input("Please enter a student id: ")
            deleteStudent(studentId)
        elif choice == '5':
            conn.close()
            break
        else:
            print("Please enter a valid choice")

            
        
        
        


# In[ ]:




