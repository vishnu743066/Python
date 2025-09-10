import logging as lg
import send_single_emails
from app import users_table   # ✅ import users_table from app.py

lg.basicConfig(
    filename="app.log",
    level=lg.DEBUG,
    format="[%(asctime)s - %(levelname)s] - %(message)s"
)

def deposite(user_name: int):
    lg.debug("user in deposit page")
    deposit_amount = int(input("Please enter deposit amount: "))
    if user_name in users_table:
        users_table[user_name][2] += deposit_amount
        new_balance = users_table[user_name][2]
        print(f"{deposit_amount} deposited. Balance: {new_balance}")

        send_single_emails.single_sender(
            to_email=users_table[user_name][1],
            subject="Deposit Successful",
            body=f"Hi {users_table[user_name][0]}, {deposit_amount} credited. "
                 f"New balance: {new_balance}."
        )
    else:
        print("User not found")
