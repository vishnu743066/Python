import logging as lg
import balance
import withdraw
import deposite
import history
import transfer
import exit_fun

lg.basicConfig(
    filename="app.log",
    level=lg.DEBUG,
    format = "[%(asctime)s - %(levelname)s] - %(message)s"
)


# total Operations
operations = (
    "1. Balance\n",
    "2. withdraw\n",
    "3. deposite\n",
    "4. Transfer\n",
    "5. History\n",
    "6.exit\n"
)


# account table 
account_table = {
    12345:6789,
    123456:6789
    }


#user tables 
# enter your mails to send an emails to send message
# enter your names also 
users_table= {
    12345: ["name1","your mail @gmail.com",2500],
    123456: ["name2","your another @gmail.com",1000]
    }

#transcation table


# Checking valid user
def valid_user(user_name:int, password:int):
    lg.debug("User in login page")
    if user_name in account_table:
        if account_table[user_name] == password:
            lg.info("User successfully logined")
            print("User successfully logined")
            return True
        else:
            lg.warning("Please check your login credentials")
            print("Please check your login credentials")
            return False
    else:
        lg.warning("Please check check your login credentials")
        print("Please check check your login credentials")
        return False




# chose_operation function
def chose_operation(account_no, choice):
    lg.info(f"selected operation is {operations[choice-1]}")
    val = False
    if choice == 1:
        balance.balance(user_name=account_no)
    elif choice == 2:
        withdraw.withdraw(user_name= account_no)
    elif choice == 3:
        deposite.deposite(user_name= account_no)
    elif choice == 4:
        transfer.transfer(user_name= account_no)
    elif choice == 5:
        history.history(user_name= account_no)
    elif choice == 6:
        val = exit_fun.exit_fun()
    else:
        print("Please selct between 1-6")
    if val:
        return val


if __name__ == "__main__":
    print("Welcome to the online codegnan Banking")
    lg.info("Welcome to the online codegnan Banking")
    account_no = int(input("Please, enter account number: "))
    pin =int(input("Please enter pin number: "))
    lg.info(f"User credenctials are {account_no} and {pin}")
    while True:
        if valid_user(user_name=account_no,password=pin):
            print(*operations)
            lg.info(operations)
            choice = int(input("Please select operation (1-6): "))
            exit_fun_val = chose_operation(account_no=account_no, choice=choice)
            if exit_fun_val:
                break
        else:
            lg.warning("User not found, please check with your login credentials")
            print("User not found, please check with your login credentials")

            break
