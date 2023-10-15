from flask import Flask, request, render_template


from model import model1
app = Flask(__name__)

# MySQL Configuration
# mydb =  mysql.connector.connect(host="localhost", user="root", passwd="nopassword")
# mycursor = mydb.cursor()
# mycursor.execute("USE medihelp")

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/submiter', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        user_name = request.form.get('username')
        password = request.form.get('password')
        
        # Use a parameterized query to avoid SQL injection
        # mycursor.execute("SELECT password FROM authenticator WHERE user_name = %s", (user_name,))
        # data = mycursor.fetchall()
        
        if model1.authentication(user_name,password)==True:
            return render_template('home.html')
        else:
            return render_template('index.html', data="Invalid credentials")

if __name__ == '__main__':
    app.run(debug=True)
