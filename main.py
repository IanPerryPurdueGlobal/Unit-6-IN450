from scenario import Scenario

def get_user_input():
    raw = input("Number of rooms (or type 'exit'): ").strip()

    if raw.lower() == "exit":
        return None

    num_rooms = int(raw)
    num_customers = int(input("Number of customers: "))
    num_items = int(input("Items (0 = random): "))

    # Validation
    if num_rooms < 1:
        raise ValueError("Need at least 1 room.")
    if num_customers < 1:
        raise ValueError("Need at least 1 customer.")
    if num_items < 0 or num_items > 6:
        raise ValueError("Items must be between 0 and 6.")

    return num_rooms, num_customers, num_items


def main():
    scenario_number = 1

    print("\n=== Dressing Room Simulation ===")
    print("Type 'exit' at the first prompt to quit.\n")

    while True:
        print(f"--- Scenario #{scenario_number} ---")

        try:
            user_input = get_user_input()

            if user_input is None:
                print("\nExiting simulation.")
                break

            num_rooms, num_customers, num_items = user_input

            scenario = Scenario(num_rooms, num_customers, num_items)
            scenario.run()

            scenario_number += 1

        except ValueError as e:
            print(f"\nERROR: {e}")
            print("Please try again.\n")


if __name__ == "__main__":
    main()


