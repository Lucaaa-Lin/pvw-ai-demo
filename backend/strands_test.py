import os
from dotenv import load_dotenv
from strands import Agent
from strands.models import BedrockModel

load_dotenv("../.env")

model = BedrockModel(
    model_id=os.getenv("MODEL_ID"),
    region_name=os.getenv("AWS_REGION"),
)

agent = Agent(model=model)

response = agent("Hello! Please introduce yourself in one sentence.")

print(response)