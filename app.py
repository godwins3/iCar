import os
from flask import Flask, request
from send_sms import send_sms

app = Flask(__name__)

@app.route('/incoming-messages', methods=['POST'])
def incoming_messages():
   data = request.get_json(force=True)
   print(f'Incoming message...\n ${data}')
   return Response(status=200)


@app.route('/delivery-reports', methods=['POST'])
def delivery_reports():
   data = request.get_json(force=True)
   print(f'Delivery report response...\n ${data}')
   return Response(status=200) 

if __name__ == "__main__":
    #TODO: Call send message function
    
    app.run(debug=True, port = os.environ.get("PORT"))
