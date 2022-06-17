import json
from decorators import singleton
import boto3


@singleton
class S3Proxy:
    def __init__(self, access_key_id, secret_access_key):
        self.s3 = boto3.resource("s3", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
    
    def call(self, bucket, key):
        return json.loads(self.s3.Object(bucket, key).get()["Body"].read().decode("utf-8"))


class ResumeDAO:
    proxy = S3Proxy(access_key_id="AKIAW75GGEL5V4DVDOHE", secret_access_key="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")
    bucket = "dynamicresumes05635-staging"

    @classmethod
    def get_resume(cls, resume_name):
        metadata = cls.proxy.call(cls.bucket, f"{resume_name}")
        data = {}
        data["stylesheet"] = cls.get_stylesheet(metadata["stylesheet_name"])
        data["layout"] = cls.get_layout(metadata["layout_name"])
        
        return data

    @classmethod
    def get_stylesheet(cls, stylesheet_name):
        return cls.proxy.call(cls.bucket, f"stylesheets/{stylesheet_name}")

    @classmethod
    def get_layout(cls, layout_name):
        return cls.proxy.call(cls.bucket, f"layout/{layout_name}")
