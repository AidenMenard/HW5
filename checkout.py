
student_key = input("Student key: ")
seed = sum(ord(ch) for ch in student_key.strip())

subtotal = 0
units = 0

while True:
    item = input("Item name (or DONE): ").strip()

    if item.upper() == "DONE":
        break
    if item == "":
        print("Item name cannot be blank.")
        continue

    while True:
        try:
            price = float(input("Unit price: "))
            if price > 0 and price < float("inf"):
                break
            print("Price must be greater than 0.")
        except ValueError:
            print("Enter a valid price.")

    while True:
        try:
            quantity = int(input("Quantity: "))
            if quantity >= 1:
                break
            print("Quantity must be at least 1.")
        except ValueError:
            print("Enter a whole number.")

    subtotal = subtotal + price * quantity
    units = units + quantity

discount = 0

if units >= 10 or subtotal >= 100:
    discount = 10

total = subtotal - subtotal * discount / 100

perk = "NO"

if seed % 2 == 1:
    total = total - 3
    perk = "YES"

if total < 0:
    total = 0

print("Seed:", seed)
print("Units:", units)
print("Subtotal: $" + format(subtotal, ".2f"))
print("Discount:", str(discount) + "%")
print("Perk applied:", perk)
print("Total: $" + format(total, ".2f"))
