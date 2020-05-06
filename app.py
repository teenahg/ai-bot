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
    resp = MessagingResponse()
    phone = request.form.get('From')
    sender = phone.replace('whatsapp:','')
    curr_msg = request.form.get('Body')
    greets = ['Hi', 'Hie', 'Hey', 'Good day']

    if curr_msg in greets:
        resp.message(\
            '''
            Hi, my name is Murimi, a *Tobacco Industry & Marketing Board* digital customer care assistant and I am here to serve you. To begin interacting with me, please select an option from the following:\n1. Login as a Tobacco Grower \n2. How can I register a new grower number? \n3. What are the requirements to register as a Tobacco transporter? \n4. Who can I speak to for more information? \n\nYou can type *#done* at any time to close the conversation.\n\n*Tobacco Industry and Marketing Board - Icon of excellence*
            '''
            )
    
    elif curr_msg.startswith('#done'):
        resp.message(\
            '''
            Thank you for your time. I hope I have been of great service to you.\n\nGood bye!
            '''
            )
    
    else:
        if curr_msg.startswith('1'):
            resp.message(\
                '''
                Please enter your registered Grower Number and National ID number to continue.
                '''
                )
        elif curr_msg.startswith('2'):
            resp.message(\
                '''
                In order to register as a Grower, you are required to bring an *offer letter and Agritex letter*, but if you are not the owner of the farm, an *affidavit and ID of the owner* are required. The registration fee is RTGS$100 from November to December, RTGS$200 in January before opening of floors and RTGS$500 when floors are open. When in need of a grower number but in the rural areas, a *letter from the Councillor, Agritex and a copy of your ID* are required.
                '''
                )
        elif curr_msg.startswith('3'):
            resp.message(\
                '''
            Stop Order for a new transporter's permit is RTGS$3750 and for renewal is RTGS$2500. To register as a new individual transporter, you are required to bring copies of your national ID and registration book as well as an agreement of sale for the vehicle to be used. When registering as a company, copies of the following documents are required: *CR14, Certificate of Incorporation and Tax Clearance*.
            '''
            )
        elif curr_msg.startswith('4'):
            resp.message(\
                '''
                For more information, please feel free to call our landline number on *+263772145166-9* or alternatively visit our website on *www.timb.co.zw* to stay updated on current affairs in the Tobacco Industry.
                ''')
            
    return str(resp)

    class msgTemplates:
        def __init__(self):
            self.tmp_main = \
            '''
            Hi, my name is Murimi, a *Tobacco Industry & Marketing Board* digital customer care assistant and I am here to serve you. To begin interacting with me, please select an option from the following:\n1. Login as a Tobacco Grower \n2. How can I register a new grower number? \n3. What are the requirements to register as a Tobacco transporter? \n4. Who can I speak to for more information? \n\nYou can type *#done* at any time to close the conversation.\n\n*Tobacco Industry and Marketing Board - Icon of excellence*
            '''
                

if __name__ == "__main__":
    app.run(debug = True)