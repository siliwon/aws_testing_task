import boto3
import boto3.session


class Bucket:
    def __init__(self, session_creds: tuple, bucket_name: str):
        session = boto3.session.Session(
            aws_access_key_id=session_creds[0],
            aws_secret_access_key=session_creds[1]
        )
        self.session = session.client("s3")
        self.bucket_name = bucket_name
        self.bucket_content = {}
        self.encryption = {}
    
    def list_objects(self) -> dict:
        list_objects = self.session.list_objects(Bucket=self.bucket_name)
        for content in list_objects["Contents"]:
            self.bucket_content[content["Key"]] = content
        return self.bucket_content
    
    def check_object_presented_in_bucket(self, object_name):
        try:
            return self.list_objects()[object_name]["Key"]
        except(KeyError):
            return "Not found!"
    
    def check_bucket_encryption(self):
        encryption_response = self.session.get_bucket_encryption(Bucket=self.bucket_name)
        encryption_config = encryption_response["ServerSideEncryptionConfiguration"]["Rules"][0]
        self.encryption["Rules"] = encryption_config["ApplyServerSideEncryptionByDefault"]
        self.encryption["SSEAlgorithm"] = self.encryption["Rules"]["SSEAlgorithm"]
        self.encryption["KMSMasterKeyID"] = self.encryption["Rules"]["KMSMasterKeyID"]
        self.encryption["BucketKeyEnabled"] = encryption_config["BucketKeyEnabled"]
        return self.encryption
    
    def check_bucket_encryption_deleting(self):
        self.session.delete_bucket_encryption(Bucket=self.bucket_name)        


# Functions called by Robot Framework as keywords
def check_encryption(session_creds, bucket_name):
    s3_bucket = Bucket(session_creds,bucket_name)
    encryption = s3_bucket.check_bucket_encryption()
    return encryption["BucketKeyEnabled"]
          
def check_encryption_deleting(session_creds, bucket_name):
    s3_bucket = Bucket(session_creds, bucket_name)
    return s3_bucket.check_bucket_encryption_deleting()

def check_file_presented(session_creds, bucket_name, file_name):
    s3_bucket = Bucket(session_creds, bucket_name)
    return s3_bucket.check_object_presented_in_bucket(file_name)
