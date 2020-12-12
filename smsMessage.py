from twilio.rest import Client 
 
account_sid = '' 
auth_token = '' 
client = Client(account_sid, auth_token) 
 
def sendSMS():
    message = client.messages.create( 
                              from_='+14752672676',  
                              body='Rostro desconocido detectado',      
                              to='+' 
                          ) 
 
    print(message.sid)
