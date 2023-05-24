import africastalking
import random
username='campaignSms'
api_key='f889296043073085e9038f75dc7bc46cdd65f9c473fc49ae555103a532f971a6'

africastalking.initialize(username, api_key)
def get_me():
    message_dict= [
        "Hooray you have reached level" + "of the game. You are now a pro" +"Did you know that Kisumu is the cleanest city in Kenya",
        "Please wear a mask to avoid being infected with covid-19",
        "Thank you for your cooperation"
    ]
    m = random.choice(message_dict)
    return m

class send_sms():

    sms = africastalking.SMS
    def sending(self):
        # Set the numbers in international format
        recipients = ["+254742079321"]
        # Set your message
        message = get_me()
        # Set your shortCode or senderId
        #sender = "iCar Ltd"
        try:
            response = self.sms.send(message, recipients)
            print (response)
        except Exception as e:
            print (f'Houston, we have a problem: {e}')

send_sms().sending()