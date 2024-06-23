from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Retrieve API key and secret from environment variables
NEXMO_API_KEY = os.getenv('5913e543EY')
NEXMO_API_SECRET = os.getenv('8O90KfQVQ5rwbAWqT')

def store_otp(phone_number, otp_code):
    conn = sqlite3.connect('otps.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO otps (phone_number, otp_code) VALUES (?, ?)", (phone_number, otp_code))
    conn.commit()
    conn.close()

@app.route('/sms', methods=['POST'])
def sms_reply():
    data = request.json
    phone_number = data['msisdn']
    otp_code = data['text']
    
    store_otp(phone_number, otp_code)
    
    return jsonify({'status': 'received'})

if __name__ == '__main__':
    app.run(debug=True)
