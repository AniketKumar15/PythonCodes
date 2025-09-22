# Write a Python program to find the number of notes (Sample of notes: 10, 20, 50, 100, 200 and 500) against an given amount. Range Number of notes(n) n (1 = n = 1000000).
def count_notes(amount):
    notes = [500, 200, 100, 50, 20, 10]
    note_count = {}
    for note in notes:
        if amount >= note:
            note_count[note] = amount // note
            amount %= note
    return note_count

amount = int(input("Enter the amount (1 <= n <= 1000000): "))
if 1 <= amount <= 1000000:
    result = count_notes(amount)
    print("Number of notes:")
    for note, count in result.items():
        print(f"Rs {note}: {count}")
else:
    print("Invalid amount. Please enter a value between 1 and 1000000.")
