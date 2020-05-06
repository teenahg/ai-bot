# Commented out sections contain functionality to be added as future updates
import logging
logger = logging
from flask import session, redirect, url_for, request
from functools import wraps

def check_intention(f):
    @wraps(f)
    def intention(*args, **kwargs):
        sender_number = ''
        msg_body = ''
        try:
            message = dict(kwargs['message'])
            sender_number = str(message['From']).replace('whatsapp:', '')
            msg_body = str(message['Body'])
            
            logger.error(message)
            
        except IndexError as e:
            logger.error(e.args)
            return f(*args, **kwargs)
        
        except Exception as e:
            logger.error(e.args)
            return f(*args, **kwargs)
        
        if 'intention_'+sender_number not in session:
            return f(*args, **kwargs)
        elif session['intention_'+sender_number] == 'login':
            return f(*args,message=message)
        elif session['intention_'+sender_number] == 'registration':
            tag = {'tag': 'registration'}
            message.update(tag)
            return redirect(url_for('home' ,message=message))
            # return f(*args,message=message)
        elif session['intention_'+sender_number] == 'transporter':
            tag = {'tag': 'transporter'}
            message.update(tag)
            return f(*args,message=message)
        elif session['intention_'+sender_number] == 'more':
            tag = {'tag' 'more'}
            message.update(tag)
            return f(*args,message=message)
        elif msg_body.startswith('done'):
            return f(*args, message = message)
        else:
            return f(*args, **kwargs)
        
    return intention