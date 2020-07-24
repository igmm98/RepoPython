import os 
from twilio.rest import Client

#
# ES NECESARIO REGISTRO EN WEB DE TWILIO
account_sid = '#' 
auth_token = '#' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='*ALERTA \nShielder*',      
                              to='whatsapp:+#' 
                          ) 
 
print(message.sid)
