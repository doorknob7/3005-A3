import psycopg2

#connects to database
def database():
    #try catch to connect to database with psycopg2
    try:
        c = psycopg2.connect(
            database='a3q1',
            user='postgres',
            password='pass',
            host= 'localhost', 
            port='5432'
        )
        #returns connection to calling fucntion
        return c
    
    #catch for failed connection
    except (Exception, psycopg2.Error) as e:
        print("failure to connect to databse, error:", e)

#gets the students from the database
def getAllStudents():
    #database connection returned
    c = database()
    #try catch depending on if database connected
    try:
        if c:
            #uses cursor to process SQL statements to the database
            cur = c.cursor()

            #cursor creates a query and executes it
            q = "SELECT * FROM students"
            cur.execute(q)

            #fetches the result of query
            data = cur.fetchall()

            #query output:
            print("All student records:\n" + str(data) + "\n")

            #ends cursor connection
            cur.close()
            #ends database connection
            c.close()

    #except catches databse error
    except (Exception, psycopg2.Error) as e:
        print("failure to get all students, error: ", e)

#adds a student  to the database
def addStudent(first_name, last_name, email, enrollment_date):
    #database connection returned
    c = database()
    #try catch depending on if database connected
    try:
        if c:
            #uses cursor to process SQL statements to the database
            cur = c.cursor()

            #creates a query and executes it
            q = """
                INSERT INTO students (first_name, last_name, email, enrollment_date)
                VALUES (%s, %s, %s, %s)
                """
            v = (first_name, last_name, email, enrollment_date)
            cur.execute(q, v)

            #commits the changes made in query
            c.commit()

            #ends cursor connection
            cur.close()
            #ends database connection
            c.close()

    #except catches database error
    except (Exception, psycopg2.Error) as e:
        print("failure adding student, error:", e)

#changes a students email in the database
def updateStudentEmail(student_id, new_email):
    #database connection returned
    c = database()
    #try catch depending on if database connected
    try:
        if c:
            #uses cursor to process SQL statements to the database
            cur = c.cursor()

            #creates a query and executes it
            q = """
                UPDATE students 
                SET email = %s
                WHERE student_id = %s
            """
            v = (new_email, student_id)
            cur.execute(q,v)

            #commits the changes made in query
            c.commit()

            #ends cursor connection
            cur.close()
            #ends database connection
            c.close()

    #except catches database error
    except (Exception, psycopg2.Error) as e:
        print("failure to update student email, error: ", e)

#deletes a student in the database
def deleteStudent(student_id):
    #database connection returned
    c = database()
    #try catch depending on if database connected
    try:
        # checks if the connection was successful
        if c:
            #uses cursor to process SQL statements to the database
            cur = c.cursor()

            #creates a query and executes it
            q= """
                DELETE FROM students 
                WHERE student_id = %s
            """
            v= (student_id,)

            cur.execute(q,v)  

            #commits the changes made in query
            c.commit()

            #ends cursor connection
            cur.close()
            #ends database connection
            c.close()

    #except catches database error
    except (Exception, psycopg2.Error) as e:
        print("failure to delete student, error: ", e)

print("all students before add student:")
getAllStudents()
addStudent('Alex', 'Jonas', 'alexsemail@email.com', '1999-01-01') 
print("all students after add student:")

print("all students before update student email:")
getAllStudents()
updateStudentEmail(3,"flashynewemail@email.com")
print("all students after update student email:")

print("all students before delete student:")
getAllStudents()
deleteStudent(1)
print("all students after delete student:")
getAllStudents()