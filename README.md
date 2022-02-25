# b_notified
A Django notification service

## API endpoint
``
http://127.0.0.1:8000/webapp/notify/
``
 - x-www-urlencoded
```
{
    type: '',
    message: '',
    recipient: ''
}
```
#### Supported `type`'(s) of notification
 - SMS
 - EMAIL
 - PUSH_NOTIF

 ### Recipient
  - depends on type of notification
  if `type` is EMAIL
     -  ex: example@gmail.com
  - if type is SMS
     -  ex: +250730000000  
  - if type is PUSH_NOTIF:
     -  it sands push notification to devices registered in (firebase cloude essaging) database

## 3rd parties used
 - Twilio for sms messaging
 - FCM(Firebase Cloude Messaging) for push notifications
 ## Not yet implemented (downside)
 - Proper validation
 - proper handling of confidential info