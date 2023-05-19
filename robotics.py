from biography import Biography
import textwrap

LINELENGTH = 100

class Robot:
    def __init__(self, name, options):
        self.name = name
        self.options = options
        self.current_selection = None

    # give user name of bot
    def say_hello(self):
        print("Hello, my name is " + self.name)

    # give overview of app functionality
    def describe_purpose(self):
        print("I'm here to introduce you to some of humanity's most famous scientists.")
        print(textwrap.fill("I will provide you with a list of names from which you can select and "
                            "then provide you with the birthdate, date of death, age, and a brief overview of their life.", LINELENGTH))

    # give options from which user can select
    def give_options(self):
        print("Please enter the number corresponding to the person about whom you would like to learn or '0' to exit:")
        for i in range(len(self.options)):
            print(str(i + 1) + ": " + self.options[i])

    # gracefully exit app
    def say_goodbye(self):
        print("Goodbye - thanks for using", self.name, "!")
        exit()

    # receive user selection and generate bio class instance
    def handle_input(self):
        selection = None

        try:
            selection = int(input())

            # user has requested exit
            if selection == 0:
                self.say_goodbye()
            # selection is outside of range
            elif selection > len(self.options) or selection < 0:
                print("The number you have selected is not an option. Please select a number between 1 and", len(self.options),".")
                self.handle_input()
        # char other than int entered
        except ValueError:
            print("Oops! That wasn't a number - please try again.")
            self.handle_input()
        self.current_selection = Biography(self.options[selection-1])
        self.provide_data()

    # displays data for current_selection and then returns to awaiting user input
    def provide_data(self):
        print("\n\n")
        print("You have selected", self.current_selection.name, ".")
        print("According to Wikipedia, they were born on ", self.current_selection.bday, "and died on ",
              self.current_selection.death, "at", self.current_selection.age, "years of age.")
        print(textwrap.fill(self.current_selection.summary, LINELENGTH))
        print("\n\n")
        self.give_options()
        self.handle_input()



