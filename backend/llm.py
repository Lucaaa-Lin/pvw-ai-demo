import os
import boto3
from dotenv import load_dotenv

load_dotenv("../.env")

model_id = os.getenv("MODEL_ID")

client = boto3.client(
    "bedrock-runtime",
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)


def ask_llm(prompt):
    response = client.converse(
        modelId=model_id,
        messages=[
            {
                "role": "user",
                "content": [{"text": prompt}],
            }
        ],
    )

    return response["output"]["message"]["content"][0]["text"]


if __name__ == "__main__":
    answer = ask_llm("Please introduce yourself in one sentence.")
    print(answer)