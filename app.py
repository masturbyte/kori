from flask import Flask, render_template, request, redirect
import sqlite3


falcon = Flask(__name__)

@falcon.route("/")
def homepage():
    return render_template("index.html" , pagetitle=("Falcon"))

@falcon.route("/about")
def about():
    return render_template("about.html" , pagetitle=("About US"))

@falcon.route("/contact")
def contact():
    return render_template("contact.html" , pagetitle=("Contact"))


@falcon.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        firstName = request.form.get('firstName', '')
        lastName = request.form.get('lastName', '')
        email = request.form.get('email', '')
        number = request.form.get('number', '')
        message = request.form.get('message', '')



        
        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO contacts (firstName, lastName, number, email, message) VALUES (?, ?, ?, ?, ?)',
                           (firstName, lastName, number, email, message))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Failed to insert into database: {e}")
            return "Error processing request.", 400
        
        return redirect('/')
    else:
        return "Method not allowed", 405  

@falcon.route("/info")
def info():
    return render_template("info.html" , pagetitle=("MORE CAR"))

@falcon.route("/booking")
def booking():
    return render_template("booking.html" , pagetitle=("Booking"))

@falcon.route('/pay', methods=['POST'] )
def pay():
    name = request.form.get('namecard') 
    message = f"{name}"
    return render_template('thanks.html', message=message, pagetitle="THANK YOU!")


if __name__ == "__main__":
    falcon.run(debug=True,port=1)