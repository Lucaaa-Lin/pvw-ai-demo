from strands import tool
from services.sanity import fetch_available_watches


@tool
def get_details(query: str):
    """
    Return detailed information for a specific watch.
    """

    print(f"get_details called: {query}")

    watches = fetch_available_watches()
    query = query.lower()

    for watch in watches:

        searchable = " ".join(
            [
                watch.get("brand", ""),
                watch.get("name", ""),
                watch.get("description", ""),
            ]
        ).lower()

        if query in searchable:

            return {
                "success": True,
                "action": "get_details",
                "data": {
                    "brand": watch.get("brand"),
                    "name": watch.get("name"),
                    "price": watch.get("price"),
                    "description": watch.get("description"),
                    "movement": watch.get("movement"),
                    "gender": watch.get("gender"),
                },
            }

    return {
        "success": False,
        "action": "get_details",
        "message": "No matching watch found.",
    }


if __name__ == "__main__":
    result = get_details("Omega")
    print(result)