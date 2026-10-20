
import requests

# Student key
student_key = input("Student key: ")
seed = sum(ord(ch) for ch in student_key.strip())

# Determine reorder threshold
if seed % 3 == 0:
    threshold = 15
elif seed % 3 == 1:
    threshold = 12
else:
    threshold = 9

# Start inventory counters
total_skus = 0
reorder_count = 0

# Enter inventory items
while True:
    sku = input("SKU: ").strip()

    if sku.upper() == "DONE":
        break

    if sku == "":
        print("SKU cannot be blank.")
        continue

    # Ask for inventory quantity
    while True:
        try:
            on_hand = int(input("On hand: "))

            if on_hand >= 0:
                break
            else:
                print("On hand cannot be negative.")

        except ValueError:
            print("Please enter a whole number.")

    # Count the SKU
    total_skus = total_skus + 1

    # Determine if reorder is needed
    if on_hand < threshold:
        print(sku, "- REORDER")
        reorder_count = reorder_count + 1
    else:
        print(sku, "- OK")


# Choose API search term
if seed % 2 == 0:
    search_term = "weezer"
else:
    search_term = "drake"

# API information
url = "https://itunes.apple.com/search"

parameters = {
    "entity": "song",
    "limit": 5,
    "term": search_term
}

songs_returned = "N/A"

# Connect to the iTunes API
try:
    response = requests.get(url, params=parameters, timeout=10)
    response.raise_for_status()

except requests.exceptions.RequestException:
    api_status = "FAILED"

else:
    try:
        data = response.json()
        results = data["results"]

        if not isinstance(results, list):
            raise ValueError()

        song_count = 0

        # Count the songs
        for item in results:
            if not isinstance(item, dict):
                raise ValueError()

            if item.get("kind") == "song":
                song_count = song_count + 1

        songs_returned = song_count
        api_status = "OK"

    except (ValueError, KeyError, TypeError):
        api_status = "INVALID_RESPONSE"


# Print final results
print("Seed:", seed)
print("Threshold:", threshold)
print("SKUs entered:", total_skus)
print("Reorder flagged:", reorder_count)
print("Spotcheck term:", search_term)
print("Songs returned:", songs_returned)
print("API status:", api_status)
