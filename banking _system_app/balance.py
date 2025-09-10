import logging as lg

lg.basicConfig(
    filename="app.log",
    level=lg.DEBUG,
    format = "[%(asctime)s - %(levelname)s] - %(message)s"
)

#user tables 
users_table= {
    12345: ["Vishnu Vardhan","VV743066@gmail.com",2500],
    123456: ["vardhan","viralvishnu@gmail.com",1000]
}

# balance function
def balance(user_name):
    lg.info("User in balance page")
    if user_name in users_table:
        amount = users_table[user_name][2]
        lg.info(f"{user_name} user current balance is{amount}")
        print(f"{user_name} user current balance is {amount}")
    else:
        lg.warning("User not found")
        print("User not found")