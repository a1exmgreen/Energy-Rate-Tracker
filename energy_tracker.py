def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")

def get_recommendation(variable, fixed, trend):
    threshold = variable * 1.05

    if fixed <= threshold and trend == "up":
        return "✔️ FIX NOW - good deal before prices rise"
    elif trend == "down":
        return "❌ WAIT - prices are falling"
    else:
        return "⚠️ HOLD - not worth fixing yet"

def main():
    print("=== Engery Tariff Decision Tool ===\n")

    # User input
    variable = get_float("Enter current VARIABLE monthly (£): ")
    fixed = get_float("Enter best FIXED deal monthly (£): ")

    trend = input("Market trend? (up/down/stable): ").lower()

    # Get recommendation
    result = get_recommendation(variable, fixed, trend)

    # Display result
    print("\n--- Recomendation ---")
    print(result)

if __name__ == "__main__":
    main()
