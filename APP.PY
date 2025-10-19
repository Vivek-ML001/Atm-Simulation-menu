from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage (you can replace with database later)
atm_data = {
    "pin": None,
    "balance": 1000.0
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_pin', methods=['POST'])
def create_pin():
    pin = request.form['pin']
    if len(pin) == 4 and pin.isdigit():
        atm_data['pin'] = pin
        return render_template('menu.html', message="PIN set successfully!")
    return render_template('index.html', message="Invalid PIN. Try again.")

@app.route('/deposit', methods=['POST'])
def deposit():
    pin = request.form['pin']
    amount = float(request.form['amount'])
    if pin == atm_data['pin']:
        atm_data['balance'] += amount
        msg = f"${amount:.2f} deposited successfully!"
        return render_template('menu.html', message=msg)
    return render_template('menu.html', message="Incorrect PIN!")

@app.route('/withdraw', methods=['POST'])
def withdraw():
    pin = request.form['pin']
    amount = float(request.form['amount'])
    if pin == atm_data['pin']:
        if 0 < amount <= atm_data['balance']:
            atm_data['balance'] -= amount
            msg = f"${amount:.2f} withdrawn successfully!"
        else:
            msg = "Insufficient balance!"
        return render_template('menu.html', message=msg)
    return render_template('menu.html', message="Incorrect PIN!")

@app.route('/check_balance', methods=['POST'])
def check_balance():
    pin = request.form['pin']
    if pin == atm_data['pin']:
        return render_template('menu.html', message=f"Your balance: ${atm_data['balance']:.2f}")
    return render_template('menu.html', message="Incorrect PIN!")

if __name__ == '__main__':
    app.run(debug=True)
