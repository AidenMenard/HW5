
import requests

student_key = input("Student key: ")
seed = sum(ord(ch) for ch in student_key.strip())

if seed % 3 == 0:
    threshold = 15
elif seed % 3 == 1:
    threshold = 12
else:
    threshold = 9

total_skus = 0
reorder_count = 0

while True:
    sku = input("SKU: ").strip()

    if sku.upper() == "DONE":
        break
    if sku == "":
        print("SKU cannot be blank.")
        continue

    while True:
        try:
            on_hand = int(input("On hand: "))
            if on_hand >= 0:
                break
            print("Quantity cannot be negative.")
        except ValueError:
            print("Enter a whole number.")

    total_skus = total_skus + 1

    if on_hand < threshold:
        reorder_count = reorder_count + 1
        print(sku, "- REORDER")
    else:
        print(sku, "- OK")

if seed % 2 == 0:
    term = "weezer"
else:
    term = "drake"

songs_returned = "N/A"

try:
    response = requests.get(
        "https://itunes.apple.com/search",
        params={"term": term, "entity": "song", "limit": 5},
        timeout=10
    )
    response.raise_for_status()

except requests.exceptions.RequestException:
    api_status = "FAILED"

else:
    try:
        data = response.json()
        songs = data["results"]

        if type(songs) == list:
            count = 0

            for song in songs:
                if song.get("kind") == "song":
                    count = count + 1

            songs_returned = count
            api_status = "OK"
        else:
            api_status = "INVALID_RESPONSE"

    except (ValueError, KeyError, TypeError, AttributeError):
        api_status = "INVALID_RESPONSE"

print("Seed:", seed)
print("Threshold:", threshold)
print("SKUs entered:", total_skus)
print("Reorder flagged:", reorder_count)
print("Spotcheck term:", term)
print("Songs returned:", songs_returned)
print("API status:", api_status)
