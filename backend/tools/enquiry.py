from strands import tool


@tool
def send_enquiry(
    watch: str,
    customer_message: str = "",
    customer_name: str = "",
    customer_email: str = "",
):
    """
    Prepare an email enquiry for a customer who is interested in a specific watch.
    Use this when the customer wants to ask about availability, condition, price, shipping, payment, or general purchase enquiry.
    """

    return {
        "success": True,
        "action": "email_enquiry",
        "to": "demo@pvw.com",
        "watch": watch,
        "customer_name": customer_name,
        "customer_email": customer_email,
        "customer_message": customer_message,
        "email_subject": f"Enquiry about {watch}",
        "email_body": f"""
Watch: {watch}
Customer Name: {customer_name}
Customer Email: {customer_email}

Message:
{customer_message}
""".strip(),
    }