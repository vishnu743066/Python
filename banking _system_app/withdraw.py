import logging as lg
import send_single_emails

lg.basicConfig(
    filename="app.log",
    level=lg.DEBUG,
    format="[%(asctime)s - %(levelname)s] - %(message)s"
)

users_table = {
    12345: ["name1","email1@gmail.com",2500],
    123456: ["name2","email2@gmail.com",1000]
}

def withdraw(user_name):
    lg.debug("User in withdraw page")
    amount = users_table[user_name][2]
    withdraw_amount = int(input("Please enter withdraw amount: "))
    if amount >= withdraw_amount:
        users_table[user_name][2] -= withdraw_amount
        new_balance = users_table[user_name][2]
        lg.info(f"{withdraw_amount} withdrawn. Balance: {new_balance}")
        print(f"{withdraw_amount} withdrawn. Balance: {new_balance}")

        # ✉ send email
        send_single_emails.single_sender(
            to_email=users_table[user_name][1],
            subject="Withdrawal Successful",
            body=f"Hi {users_table[user_name][0]}, {withdraw_amount} debited. "
                 f"New balance: {new_balance}."
        )
    else:
        lg.warning("insufficient amount")
        print("Insufficient amount")

