import send_single_emails

#create bulk email send email
def send_bulk_email(email:list, subject:str, body:str=None):
    for to_email in email:
        try:    
            send_single_emails.single_sender(
                to_email=to_email, 
                subject=subject,
                body=body
        )