import os 
from twilio.rest import Client

#
# ES NECESARIO REGISTRO EN WEB DE TWILIO
account_sid = 'ACccfed01325e0fe30539ab253e169dfa8' 
auth_token = 'cecbc2d51738c60ee2fd2bed4d458fb6' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='*ALERTA \nShielder*',      
                              to='whatsapp:+56945659268' 
                          ) 
 
print(message.sid)
