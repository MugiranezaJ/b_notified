from twilio.rest import Client
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.template.loader import render_to_string
from firebase_admin.messaging import Message, Notification
from fcm_django.models import FCMDevice
# Create your views here.

@api_view(["GET", "POST"])
def notify(request):
    try:
        method = request.method
        if method == 'POST':
            notif_type = request.data["type"]
            message = request.data["message"]
            recipient = request.data["recipient"]
            notify = Notify(notif_type, message, recipient) 
            return notify.send_notification()
        else:
            return Response({"messge":"You have to use post on this url"})
    except Exception as e:
        return Response({"error":"[1] internal server error", "stack":str(e)})

class Notify:
    message = ''
    notif_type = ''
    recipient = ''
    # recipient = '+250738913482'
    # recipient = '+250780712835'
    def __init__(self, notif_type, message, recipient):
        self.notif_type = notif_type
        self.message = message
        self.recipient = recipient
    
    def send_notification(self):
        try:
            if self.notif_type == "SMS":
                res = self.send_sms(self.recipient, self.message)
                return Response(res)
            elif self.notif_type == "EMAIL":
                res = self.send_email_notification(self.recipient, self.message)
                return Response(res)
            elif self.notif_type == "PUSH_NOTIF":
                res = self.send_push_notification(self.message)
                return Response(res)
            else:
                return Response({"error":"invalid notification type"})
        except Exception as e:
            return Response({"error":"[2] internal server error", "stack":str(e)})
        
    def send_email_notification(self, recipient, message):
        template = render_to_string("email_template.html", {"message": message})
        res = dict()
        try:
            send_mail(
                'Notification Test',
                template,
                settings.EMAIL_HOST_USER,
                [recipient],
                fail_silently=False
            )
            
            res["message"] = "Email notification sent successfully!"
            return res
        except Exception as e:
            res["error"] = "There was error sending email"
            res["stack"] = str(e)
            print(str(res))
            return res

    def send_sms(self, recipient, message):
        try:
            account_sid = settings.TWILIO_ACCOUNT_SID
            auth_token = settings.TWILIO_AUTH_TOKEN
            client = Client(account_sid, auth_token)
            messageBody = client.messages.create(
                body=message, 
                from_=settings.TWILIO_NUMBER, 
                to=recipient)
            return ({"message":"text message sent successfully", "sid":str(messageBody.sid)})
        except Exception as e:
            return ({"message":"There was error send sms", "stack": str(e)})

    def send_push_notification(self, message):
        print("inside")
        try:
            devices = FCMDevice.objects.all()
            res = devices.send_message(Message(
                notification=Notification(
                    title="BNotified notfication", 
                    body=message, 
                    image="url"),
                    topic="Topic: firebase notifiction service :)",
                )
            )
            print(str(devices))
            recipients = len(devices)
            res_message = "Push notification sent!" if recipients else "Push notification sent!, But it seems like no registered client to receive it"
            return ({
                "message":res_message, 
                "Firebase_response":
                {
                    "registration_ids_sent": res.registration_ids_sent,
                    "deactivated_registration_ids": res.deactivated_registration_ids,
                    "success_count": res.response.success_count,
                    "failure_count": res.response.failure_count,
                    "data": str(res.response.responses)
                }
                })
        except Exception as e:
            return ({"error":"There was error sending push notification", "stack": str(e)})