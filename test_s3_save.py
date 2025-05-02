from datetime import datetime
import boto3
import os
from dotenv import load_dotenv

load_dotenv(override=True)

s3 = boto3.client(
    "s3",
    region_name=os.getenv("AWS_DEFAULT_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

# Sample content
filename = f"chat_history_test_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.txt"
content = "USER [test time]:\nHello!\n\nASSISTANT [test time]:\nHi there! 👋"

# Upload to S3
s3.put_object(
    Bucket=os.getenv("S3_BUCKET_NAME"),
    Key=filename,
    Body=content.encode("utf-8"),
    ContentType="text/plain"
)

print(f"✅ Uploaded {filename} to S3.")
