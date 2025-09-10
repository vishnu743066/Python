import bank_app.send_single_emails as send_single_emails
import bank_app.send_bulk_email as send_bulk_email

#main start
if __name__ == "__main__":
    print("select type emails send\n 1.send email \n 2.but email send")
    choice = int(input("please select your type of email send: "))
    subject_email= input("Enter subject of email: ")
    body = input("Enter body of an email: ")
    if choice ==1:
        receiver_email= input("Enter receiver emails: ")
    # send single main function call
        send_single_emails.single_sender(
            to_email=receiver_email, 
            subject=subject_email, 
            body=body
        )
    elif choice==2:
        receiver_email_lists= list(input("Enter receiver emails: ").split(","))
        send_single_emails.single_sender(
            to_email=receiver_email_lists, 
            subject=subject_email, 
            body=body
        )