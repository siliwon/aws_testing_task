import os

# Access to s3 with admin roles
ADMIN_ACCESS_KEY_ID = os.environ.get("ADMIN_ACCESS_KEY_ID")
ADMIN_SECRET_ACCESS_KEY = os.environ.get("ADMIN_SECRET_ACCESS_KEY")
ADMIN_CREDS = (ADMIN_ACCESS_KEY_ID, ADMIN_SECRET_ACCESS_KEY)

# Access to s3 with read-only roles                                       
READ_ONLY_ACCESS_KEY_ID = os.environ.get("READ_ONLY_ACCESS_KEY_ID")
READ_ONLY_SECRET_ACCESS_KEY = os.environ.get("READ_ONLY_SECRET_ACCESS_KEY")
READ_ONLY_CREDS = (READ_ONLY_ACCESS_KEY_ID, READ_ONLY_SECRET_ACCESS_KEY)

# Access to s3 without roles
WITHOUT_ROLES_ACCESS_KEY_ID = os.environ.get("WITHOUT_ROLES_ACCESS_KEY_ID")
WITHOUT_ROLES_SECRET_ACCESS_KEY = os.environ.get("WITHOUT_ROLES_SECRET_ACCESS_KEY")
WITHOUT_ROLES_CREDS = (WITHOUT_ROLES_ACCESS_KEY_ID, WITHOUT_ROLES_SECRET_ACCESS_KEY)

# Check the default content of s3
BUCKET = "aws-test-task-closed-bucket"
FILE = "manual/amazon.txt"
