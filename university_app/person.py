import logging as lg
lg.basicConfig(
    filename="University.log",
    level=lg.DEBUG,
    format = "[%(asctime)s - %(levelname)s] - %(message)s"
)

class Person:
    # person take name
    def __init__(self, name):
        self.name = name

    def display(self):
        # display name
        lg.info("Person details displayed")
        print(f"Name: {self.name}")