import logging as lg

lg.basicConfig(
    filename="app.log",
    level=lg.DEBUG,
    format = "[%(asctime)s - %(levelname)s] - %(message)s"
)

#user tables 
users_table= {
    12345: ["name 1","mail1@gmail.com",2500],
    123456: ["name 2","mail2@gmail.com",1000]
}


# exit function
def exit_fun():
    lg.info("User in exit page")
    print("Sucessfully excuted, Thank you using codegnan online bank services ")
    return True

