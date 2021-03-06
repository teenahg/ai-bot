from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from misc import check_intention

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/sms", methods = ['POST'])
@check_intention
def sms_reply():
    # capture user input
    resp = MessagingResponse()
    phone = request.form.get('From')
    sender = phone.replace('whatsapp:','')
    current_message = request.form.get('Body')
    greeting_messages = ['Hi', 'hi', 'hie', 'Hie', 'Hello', 'hello', 'Greetings', 'greetings', 'Good day']

    if current_message in greeting_messages:
        resp.message(\
'''
Hi, I'm *Pat*, a digital career guidance chatbot. Please choose one of the following to interact with me:\n
1. Register \n
2. Login \n
3. Get help choosing a career \n
4. About me\n\n
You can type *#done* at any time to close the conversation.\n\n
*Pat*
'''
            )
    
    elif current_message.startswith('#done'):
        resp.message(\
            '''
            Thank you for your time. I hope I have been of great service to you.\n\nGood bye!
            '''
            )
    
    else:
        if current_message.startswith('1'):
            resp.message(\
                '''
                Please enter a valid email and phone number to register.
                '''
                )
        elif current_message.startswith('2'):
            resp.message(\
                '''
                Enter your registered email and phone number to log in.
                '''
                )
        elif current_message.startswith('3'):
            resp.message(\
                '''
            To get started, please enter the subject combinations you prefer.
            '''
            )
        elif current_message.startswith('4'):
            resp.message(\
                '''
                I am Pat, a digital career guidance chatbot built under ScarLab AI by AxionTech.
                ''')
        else:
            resp.message(\
                '''
                Sorry, I did not get that. Please come again!
                '''
                )
            
    return str(resp)

    class msgTemplates:
        def __init__(self):
            self.tmp_main = \
            '''
            Hi, my name is Murimi, a *Tobacco Industry & Marketing Board* digital customer care assistant and I am here to serve you. To begin interacting with me, please select an option from the following:\n1. Login as a Tobacco Grower \n2. How can I register a new grower number? \n3. What are the requirements to register as a Tobacco transporter? \n4. Who can I speak to for more information? \n\nYou can type *#done* at any time to close the conversation.\n\n*Tobacco Industry and Marketing Board - Icon of excellence*
            '''
                

if __name__ == "__main__":
    app.run(debug = True)