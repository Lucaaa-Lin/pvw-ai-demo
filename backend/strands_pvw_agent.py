import os
from dotenv import load_dotenv

from strands import Agent
from strands.models import BedrockModel
from prompts.system_prompt import PVW_SYSTEM_PROMPT
from tools.inventory import check_inventory
from tools.details import get_details
from tools.recommend import make_recommendation
from tools.contact import contact_pvw
from tools.enquiry import send_enquiry

load_dotenv()

model = BedrockModel(
    model_id=os.getenv("BEDROCK_MODEL_ID"),
    region_name=os.getenv("AWS_REGION"),
)

agent = Agent(
    model=model,
    system_prompt=PVW_SYSTEM_PROMPT,
    tools=[
        check_inventory,
        get_details,
        make_recommendation,
        contact_pvw,
        send_enquiry,
    ],
)

if __name__ == "__main__":
    while True:
        user_input = input("Customer: ")

        if user_input.lower() in ["exit", "quit", "q"]:
            break

        response = agent(user_input)
        print(response)