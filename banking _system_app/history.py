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


# history function
def history(user_name):
    lg.info("User in history page")
    print("History function under developement process.....")