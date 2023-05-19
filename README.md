# Robotic Researcher
Welcome to Quandri's technical assignment. This assignment is meant to simulate the work
you would do working at Quandri building software robots. 

## Your task
The purpose of this software robot is to find key information about important scientists
and display it to the user.

When this robot is run, it should:

1. Introduce itself and explain the steps it's about to take.
2. Navigate to the wikipedia page of the scientists found in the list SCIENTISTS.
3. Retrieve the dates the scientists were born and died and calculate their age. Also, 
    retrieve the first paragraph of their wikipedia page.
4. Display all of this information to the user in an easily understood manner. 

## A few things to keep in mind
- This should be written as production level code. i.e. You would expect this code to
    pass a PR to get merged into main.
- As this is a software robot, it should not make use of any wikipedia API but it should 
    instead open a browser and navigate to wikipedia in the same manner a human would.
- The provided code can be added to, removed and changed as you see fit.
- Please use rpaframework to complete this task. Documentation for the provided 
    library can be found [here](https://rpaframework.org/#)

## Bonus
What other nifty features can you add to your robot? This is not required but is an
opportunity for you to have fun with your code and show your creativity.


## Submission
When you've completed the task, please email your project in a zip folder to 
jamieson@quandri.io with the subject line: `Robotic Researcher - Quandri Backend Python 
Interview`



## Assumptions
* The application's UI is the console.
* Users will be fluent in English.
* All values contained in the SCIENTISTS constant will be correctly formed names of scientists that have pages on wikipedia.
* All scientists included in the list will have a date of death.

## Running
From the terminal in the root of the project, run `pip install -r requirements.txt`.
The command `python main.py` will start the application.

## Testing
A testing suite has been provided using the unittest library. To run the tests enter `python tests.py`.