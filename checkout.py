student_key = input("Student key: ")

seed = sum(ord(ch) for ch in student_key.strip())

subtotal = 0
total_units = 0

while True:
    item_name = input("Item name (or DONE): ").strip()

    if item_name.upper() == "DONE":
        break

    if item_name == "":
        print("Item name cannot be blank.")
        continue

    while True:
        try:
            unit_price = float(input("Unit price: "))

            if unit_price > 0 and unit_price < float("inf"):
                break
            else:
                print("Price must be a valid number greater than 0.")

        except ValueError:
            print("Please enter a valid price.")

    while True:
        try:
            quantity = int(input("Quantity: "))

            if quantity >= 1:
                break
            else:
                print("Quantity must be at least 1.")

        except ValueError:
            print("Please enter a whole number.")

    subtotal = subtotal + (unit_price * quantity)
    total_units = total_units + quantity


if total_units >= 10 or subtotal >= 100:
    discount = 10
else:
    discount = 0

discount_amount = subtotal * (discount / 100)

total = subtotal - discount_amount

if seed % 2 == 1:
    total = total - 3
    perk_applied = "YES"
else:
    perk_applied = "NO"

if total < 0:
    total = 0


print("Seed:", seed)
print("Units:", total_units)
print("Subtotal: $" + format(subtotal, ".2f"))
print("Discount: " + str(discount) + "%")
print("Perk applied:", perk_applied)
print("Total: $" + format(total, ".2f"))