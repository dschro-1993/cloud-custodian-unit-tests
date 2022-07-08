import boto3
from unittest.mock import patch
from moto import mock_s3
from test_runner import CustodianPolicyTest

class S3MarkUnencryptedBucketsPolicyTest(CustodianPolicyTest):
    @patch("c7n.policy.Policy._write_file")
    @patch("c7n.utils.dumps")
    @mock_s3
    def test_s3_mark_unencrypted_buckets(self, dumps, wf):
        conn = boto3.client("s3")

        bucket_name_unencrypted = "bucket_unencrypted"
        bucket_name_encrypted   = "bucket_encrypted"

        conn.create_bucket(Bucket=bucket_name_unencrypted)
        conn.create_bucket(Bucket=bucket_name_encrypted)

        conn.put_bucket_encryption(
            Bucket=bucket_name_encrypted,
            ServerSideEncryptionConfiguration={
                "Rules": [
                    {
                        "ApplyServerSideEncryptionByDefault": {
                            "SSEAlgorithm": "AES256",
                        },
                    },
                ],
            },
        )

        elements, metadata = self.execute_policy("s3_mark_unencrypted_buckets.yml", dumps)
        # print(elements)
        # print(metadata)

        self.assertEqual(len(elements), 1)

        bucket_tagging = conn.get_bucket_tagging(Bucket=bucket_name_unencrypted)
        tag_set = bucket_tagging["TagSet"]
        tag = tag_set[0]

        self.assertEqual(tag["Key"],   "unencrypted")
        self.assertEqual(tag["Value"], "yes")

        # ...
