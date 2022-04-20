# aws testing task

## Preparation to work

To install all needed dependencies run such commands as follows:
* `python -m venv venv` - creates a virtualenv for further installations and work
* `pip install -r requirements.txt` - installs all dependencies needed to work with the project.

## The Factorial task
The task has been placed in the <b>factorial</b> directory. The code and the tests for it are stored separately. The Factorial class is intended to work not only with user input values but the values that may be given from the tests or other programs during the runtime. The unit tests were written via pytest framework.

To run the "factorial" program run `python3 factorial/factorial.py` and put any number you want!

To run tests simply run `pytest` command from the root directory or use the embedded test runner in your IDE.

## The Countdown task
This is a really simple program for the countdown that corresponds to all the explicitly pointed requirements. The task is located in the <b>countdown</b> directory. To start the countdown just run `python3 countdown/countdown.py` command.