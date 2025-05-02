import os
from datetime import datetime
import boto3
from dotenv import load_dotenv

# Load .env with override to ensure correct values from environment
load_dotenv(override=True)

# Environment variables
BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
AWS_REGION = os.getenv("AWS_DEFAULT_REGION")
ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

# Create S3 client
s3 = boto3.client(
    "s3",
    region_name=AWS_REGION,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

# Optional: test connection
try:
    bucket_list = [b["Name"] for b in s3.list_buckets()["Buckets"]]
    if BUCKET_NAME not in bucket_list:
        raise Exception(f"Bucket '{BUCKET_NAME}' not found in your account.")
    print("✅ Connected to AWS S3. Bucket available.")
except Exception as e:
    print("❌ AWS connection failed:", e)

def save_chat_history(chat_log, prefix="chat_history"):
    """
    Saves chat history to an S3 bucket as a timestamped .txt file.
    Includes serial number in filename based on existing files.
    """
    # Determine next serial number based on existing chat files
    existing = list_chat_files()
    next_id = 1
    if existing:
        numbers = []
        for name in existing:
            try:
                num = int(name.split("_")[2])  # Format: chat_history_5_YYYY...
                numbers.append(num)
            except:
                continue
        if numbers:
            next_id = max(numbers) + 1

    # Format filename with serial number and timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{prefix}_{next_id}_{timestamp}.txt"

    content = []
    for entry in chat_log:
        role = getattr(entry, "type", None) or entry.get("role", "unknown")
        msg = getattr(entry, "content", "") or entry.get("content", "")
        time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content.append(f"{role.upper()} [{time_str}]:\n{msg}\n")

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=filename,
        Body="\n".join(content).encode("utf-8"),
        ContentType="text/plain"
    )

    print(f"✅ Chat saved to S3 as: {filename}")


def list_chat_files():
    """
    Lists chat history files stored in the S3 bucket.
    """
    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix="chat_history")
        if "Contents" not in response:
            return []
        return sorted([obj["Key"] for obj in response["Contents"]], reverse=True)
    except Exception as e:
        print("❌ Failed to list chat files:", e)
        return []

def load_chat_file(filename):
    """
    Downloads a specific chat history file from S3.
    """
    try:
        response = s3.get_object(Bucket=BUCKET_NAME, Key=filename)
        return response["Body"].read().decode("utf-8")
    except Exception as e:
        print(f"❌ Failed to load '{filename}':", e)
        return ""
