import os
import streamlit as st

# Inject secrets for boto3 and OpenAI
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["AWS_ACCESS_KEY_ID"] = st.secrets["AWS_ACCESS_KEY_ID"]
os.environ["AWS_SECRET_ACCESS_KEY"] = st.secrets["AWS_SECRET_ACCESS_KEY"]
os.environ["AWS_DEFAULT_REGION"] = st.secrets["AWS_DEFAULT_REGION"]
os.environ["S3_BUCKET_NAME"] = st.secrets["S3_BUCKET_NAME"]
