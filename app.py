from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    dob = request.form['dob']
    
    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, dob])
    
    return f"<h3>Thank you {name}, your data has been saved!</h3>"

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
