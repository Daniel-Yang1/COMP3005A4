Link to demo: https://youtu.be/Q4mQEwp-nss

The database I used was a previously used database called postgres with 
username postgres and password admin, though it was created locally.
Prior to running the script you will need to create a database with 
the same details as above. Or you must change the connection settings used
in the line 
conn = psycopg2.connect("dbname=postgres user=postgres password=admin")


The table was setup with the following command in psql

CREATE TABLE students (
student_id serial PRIMARY KEY,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
email TEXT UNIQUE NOT NULL,
enrollment_date DATE);

The table was filled with the following command in psql:

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

The application can be run by running the following command in a terminal

py COMP3005A4Q1.py

Assuming you have setup python properly. 


Application Functions:

getAllStudents(): Retrieves and displays all records from the students table.
addStudent(first_name, last_name, email, enrollment_date): Inserts a new student record into the students table.
updateStudentEmail(student_id, new_email): Updates the email address for a student with the specified student_id.
deleteStudent(student_id): Deletes the record of the student with the specified student_id.
