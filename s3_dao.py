import json
from decorators import singleton
import boto3


@singleton
class S3Proxy:
    """S3 proxy.

    Connect to S3. Only allows a single connection.
    """

    def __init__(self, access_key_id, secret_access_key):
        """Constructor for S3Proxy class."""
        self.s3 = boto3.resource(
            "s3", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

    def call(self, bucket, key):
        """Makes calls to S3."""
        return json.loads(self.s3.Object(bucket, key).get()["Body"].read().decode("utf-8"))


class ResumeDAO:
    """Resume data access object layer.

    Used to access database.
    """
    proxy = S3Proxy(access_key_id="AKIAW75GGEL5V4DVDOHE",
                    secret_access_key="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")
    bucket = "dynamicresumes05635-staging"

    @classmethod
    def get_resume(cls, resume_name):
        """Gets resume data."""
        metadata = cls.proxy.call(cls.bucket, f"{resume_name}")
        data = {}
        data["stylesheet"] = cls.get_stylesheet(metadata["stylesheet_name"])
        data["layout"] = cls.get_layout(metadata["layout_name"])

        return data

    @classmethod
    def get_stylesheet(cls, stylesheet_name):
        """Gets resume stylesheet data."""
        return cls.proxy.call(cls.bucket, f"stylesheets/{stylesheet_name}")

    @classmethod
    def get_layout(cls, layout_name):
        """Gets resume layout data."""
        return cls.proxy.call(cls.bucket, f"layout/{layout_name}")
