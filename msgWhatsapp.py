from twilio.rest import Client 
import datetime

localDate = datetime.datetime.now()
dateNow = localDate.strftime("%c")
 
account_sid = '' 
auth_token = '' 
client = Client(account_sid, auth_token) 
 
def SendAlert(mediaPic):
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='*Alerta de desconocido* {}'.format(dateNow),      
                              media_url=''.format(mediaPic),
                              to='whatsapp:+' 
                          ) 
 
    print(message.sid)
