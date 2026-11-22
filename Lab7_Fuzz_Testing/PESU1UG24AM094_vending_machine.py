
def parse_coins(coins_csv):
    """Parse a comma-separated list of positive coin values."""
    if not isinstance(coins_csv, str) or not coins_csv.strip():
        return None

    try:
        parts = coins_csv.split(",")
        coins = [int(part.strip()) for part in parts]

        if any(coin <= 0 for coin in coins):
            return None

        return coins
    except ValueError:
        return None


def slot_position(code):
    """Convert a slot code such as B7 into zero-based coordinates."""
    if not isinstance(code, str):
        return None

    code = code.strip()

    if len(code) < 2:
        return None

    row_code = code[0].upper()
    column_code = code[1:]

    if not ("A" <= row_code <= "Z"):
        return None

    if not column_code.isdigit():
        return None

    column_number = int(column_code)

    if column_number <= 0:
        return None

    row = ord(row_code) - ord("A")
    column = column_number - 1

    return row, column


def change_due(payment):
    """Calculate the number of five-value coins returned as change."""
    if not isinstance(payment, str):
        return None

    parts = payment.split("/")

    if len(parts) != 2:
        return None

    try:
        paid = int(parts[0].strip())
        price = int(parts[1].strip())
    except ValueError:
        return None

    if paid < 0 or price < 0 or paid < price:
        return None

    change = paid - price
    return str(change // 5) + " five-coins"


def main():
    print("==== Running parse_coins ====")
    user_input = input("Enter coin values as CSV (e.g. 5,10,25): ")
    result = parse_coins(user_input)
    print("Coins:", result)

    print("\n==== Running slot_position ====")
    user_input = input("Enter a slot code (e.g. B7): ")
    result = slot_position(user_input)
    print("Row and Column:", result)

    print("\n==== Running change_due ====")
    user_input = input("Enter paid/price (e.g. 200/150): ")
    result = change_due(user_input)
    print("Change Due:", result)


if __name__ == "__main__":
    main()

