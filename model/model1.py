import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="nopassword")
mycursor = mydb.cursor()
mycursor.execute("USE medihelp")

def authentication(user_name, password):
    mycursor.execute("SELECT password FROM authenticator WHERE user_name = %s", (user_name,))
    data = mycursor.fetchall()
    if data and password == data[0][0]:
        return True
    else:
        return False


