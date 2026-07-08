import os
from pathlib import Path
from dotenv import load_dotenv
import requests

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

PROJECT_ID = os.getenv("SANITY_PROJECT_ID")
DATASET = os.getenv("SANITY_DATASET")
API_VERSION = os.getenv("SANITY_API_VERSION", "2024-01-01")


def fetch_available_watches():
    query = """
    *[_type == "product" && status == "available"]{
      _id,
      name,
      brand,
      price,
      movement,
      gender,
      status,
      description,
      "slug": slug.current,
      "imageUrl": images[0].asset->url
    }
    """

    url = f"https://{PROJECT_ID}.api.sanity.io/v{API_VERSION}/data/query/{DATASET}"

    response = requests.get(url, params={"query": query})
    response.raise_for_status()

    data = response.json()
    return data.get("result", [])


def search_inventory(
    brand=None,
    max_price=None,
    movement=None,
    gender=None,
):
    watches = fetch_available_watches()
    results = []

    for watch in watches:
        if brand and watch.get("brand", "").lower() != brand.lower():
            continue

        if max_price and watch.get("price", 0) > max_price:
            continue

        if movement and watch.get("movement", "").lower() != movement.lower():
            continue

        if gender:
          watch_genders = watch.get("gender", [])

          if isinstance(watch_genders, str):
              watch_genders = [watch_genders]

          normalized_gender = gender.lower().replace("’", "'")

          normalized_watch_genders = [
              g.lower().replace("’", "'") for g in watch_genders
          ]

          if normalized_gender not in normalized_watch_genders:
              continue

        results.append(watch)

    return results