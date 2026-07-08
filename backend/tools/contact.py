from strands import tool


@tool
def contact_pvw(
    intent: str,
    watch: str = "",
    message: str = "",
):
    """
    Provide the correct contact method for PVW customers.
    """

    if intent.lower() == "appointment":
        return {
            "success": True,
            "intent": "appointment",
            "message": "Customers can book an appointment through Instagram, WhatsApp, or Facebook.",
            "contact_options": {
                "instagram": "Demo PVW Instagram link",
                "whatsapp": "Demo PVW WhatsApp link",
                "facebook": "Demo PVW Facebook link",
            },
        }

    return {
        "success": False,
        "message": "Please specify whether this is an appointment.",
    }