from strands import tool

from services.sanity import fetch_available_watches


@tool
def make_recommendation(
    brand: str = "",
    movement: str = "",
    gender: str = "",
    max_price: float = 0,
):
    """
    Recommend watches based on customer preferences.
    """

    watches = fetch_available_watches()

    results = []

    for watch in watches:

        if brand and watch.get("brand", "").lower() != brand.lower():
            continue

        if movement and watch.get("movement", "").lower() != movement.lower():
            continue

        if gender and watch.get("gender", "").lower() != gender.lower():
            continue

        if max_price and watch.get("price", 0) > max_price:
            continue

        results.append(
            {
                "name": watch.get("name"),
                "brand": watch.get("brand"),
                "price": watch.get("price"),
            }
        )

    return {
        "success": True,
        "action": "recommendation",
        "data": results
    }

if __name__ == "__main__":
    print(make_recommendation(brand="Omega"))