from strands import tool
from services.sanity import search_inventory


@tool
def check_inventory(
    brand: str = None,
    max_price: int = None,
    movement: str = None,
    gender: str = None,
):
    """
    Search available vintage watches.

    Args:
        brand: Watch brand (e.g. Omega, Rolex, Cartier).
        max_price: Maximum price in AUD.
        movement: Movement type (Automatic, Manual Wind, Quartz, Tuning Fork, Pocket Watch).
        gender: Men's, Women's or Unisex.
    """

    results = search_inventory(
        brand=brand,
        max_price=max_price,
        movement=movement,
        gender=gender,
    )

    return {
        "success": True,
        "action": "check_inventory",
        "count": len(results),
        "data": results,
    }
if __name__ == "__main__":
    result = check_inventory(brand="Omega", max_price=3000)
    print(result)