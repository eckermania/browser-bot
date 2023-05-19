from robotics import Robot

SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]

robot = Robot("Quandrinaut", SCIENTISTS)


def introduce_yourself():
    robot.say_hello()

def introduce_functionality():
    robot.describe_purpose()

def give_selection_options():
    robot.give_options()

def handle_input():
    robot.handle_input()

def main():
    introduce_yourself()
    introduce_functionality()
    give_selection_options()
    # loop awaiting user selection until user requests to exit
    handle_input()

if __name__ == "__main__":
    main()
