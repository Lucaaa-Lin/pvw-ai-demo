from llm import ask_llm
from tools.inventory import check_inventory


SYSTEM_PROMPT = """
You are the AI assistant for Precision Vintage Watches, a vintage watch store.

Your job is to help customers:
- understand available vintage watches
- compare brands and movements
- ask useful follow-up questions
- encourage enquiries or appointments

Important rules:
- Do not invent specific inventory.
- If you do not know the actual stock, say you can help check availability.
- Keep the tone professional, warm, and concise.
- Prices should be in AUD if mentioned.
- Never mention something unreal.
- Never give discount to customers directly, transferring to human instead.
- If customers ask you the value of one watches in inventory, give an answer that out price is completive.
"""


def run_agent(user_message):
    inventory_results = ""

    if "omega" in user_message.lower() and ("3000" in user_message or "$3000" in user_message):
        results = check_inventory(brand="Omega", max_price=3000)
        inventory_results = f"""
Inventory search result:
{results}
"""

    prompt = f"""
{SYSTEM_PROMPT}

Customer message:
{user_message}

{inventory_results}

Assistant response:
"""

    return ask_llm(prompt)


if __name__ == "__main__":
    user_input = input("Customer: ")
    answer = run_agent(user_input)
    print("\nAI Assistant:")
    print(answer)