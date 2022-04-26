# aws testing task

## Preparation to work

To install all needed dependencies run such commands as follows:
* `python -m venv venv` - creates a virtualenv for further installations and work
* `pip install -r requirements.txt` - installs all dependencies needed to work with the project.
---
## The Factorial task
The task has been placed in the <b>factorial</b> directory. The code and the tests for it are stored separately. The Factorial class is intended to work not only with user input values but the values that may be given from the tests or other programs during the runtime. The unit tests were written via pytest framework.

To run the "factorial" program run `python3 factorial/factorial.py` and put any number you want!

To run tests simply run `pytest` command from the root directory or use the embedded test runner in your IDE.

---
## The Countdown task
This is a really simple program for the countdown that corresponds to all the explicitly pointed requirements. The task is located in the <b>countdown</b> directory. To start the countdown just run `python3 countdown/countdown.py` command.

---
## The AWS + Robot Framework task
The AWS infrastructure was prepared for testing as described below:
1. The IAM-users were created and added to different groups with specific permissions to s3 access: 
    * the `ADMIN` user with full access to s3;
    * the `READ-ONLY` user with Read-Only access to s3;
    * the `WITHOUT-ROLES` user with denial to access to s3 whatsoever.
2. The test s3 Bucket named `aws-test-task-closed-bucket` with SeverSide encryption was created, and the test file `amazon.txt` was manually uploaded to the `manual/` s3 folder.

The test framework itself resides in the <b>aws</b> directory. The tests are placed in `aws_test_suite.robot`. The variables needed are stored in the `variables.py` file.
The AWS credentials to each IAM-user are stored in the `.env` file and passed as environment variables to the `variables.py` file during the testing.
 The custom python library locates in `s3bucket.py` file.  The output reports, logs, and results are placed in `aws/Results folder`.
 
 To execute tests run the command:

 <b>`robot --outputdir ./aws/Results/ aws/aws_test_suite.robot `</b>

