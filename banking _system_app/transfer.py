import logging as lg
import send_single_emails   # added

lg.basicConfig(
    filename="app.log",
    level=lg.DEBUG,
    format="[%(asctime)s - %(levelname)s] - %(message)s"
)

users_table = {
    12345: ["Vishnu Vardhan","VV743066@gmail.com",2500],
    123456: ["vardhan","viralvishnu@gmail.com",1000]
}

def transfer(user_name):
    lg.debug("user in transfer page")
    receiver_account = int(input("Enter receiver account number: "))
    amount = int(input("Please enter the amount: "))
    lg.info(f"receiver={receiver_account}, amount={amount}")

    current_amount = users_table[user_name][2]
    if receiver_account in users_table:
        if current_amount >= amount:
            # update balances
            users_table[user_name][2] -= amount
            users_table[receiver_account][2] += amount
            new_balance = users_table[user_name][2]

            lg.info(f"{amount} transferred. Balance: {new_balance}")
            print(f"{amount} transferred successfully. Balance: {new_balance}")

            # ✉ email sender
            send_single_emails.single_sender(
                to_email=users_table[user_name][1],
                subject="Transfer Successful",
                body=f"Hi {users_table[user_name][0]}, {amount} debited. "
                     f"New balance: {new_balance}."
            )

            # ✉ email receiver
            send_single_emails.single_sender(
                to_email=users_table[receiver_account][1],
                subject="Money Received",
                body=f"Hi {users_table[receiver_account][0]}, {amount} credited from "
                     f"{users_table[user_name][0]}. "
                     f"Your new balance: {users_table[receiver_account][2]}."
            )
        else:
            lg.warning("insufficient funds")
            print("Insufficient funds")
    else:
        lg.warning(f"{receiver_account} not found")
        print(f"{receiver_account} not found")
