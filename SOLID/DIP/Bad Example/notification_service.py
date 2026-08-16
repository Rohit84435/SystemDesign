from email_service import EmailService
from sms_service import SMSservice

class NotificationService:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SMSservice()

    
    def notifyByEmail(self, message):
        self.email_service.send_email(message)
    
    def notifyBySMS(self, message):
        self.sms_service.send_sms(message)


ns = NotificationService()
ns.notifyByEmail("Good morning")
ns.notifyBySMS("Hello g")