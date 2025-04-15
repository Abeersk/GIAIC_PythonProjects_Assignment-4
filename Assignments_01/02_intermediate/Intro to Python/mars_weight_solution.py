print("Planetary Weight Calculator")

def main():
    print("Welcome to the Planetary Weight Calculator")

    earth_weight = float(input("Enter your weight on Earth (kg): "))

    gravity_ratio = {
        "mercury": 0.38,
        "venus": 0.91,
        "mars": 0.38,
        "jupiter": 2.34,
        "saturn": 1.08,
        "uranus": 0.92,
        "neptune": 1.17
    }

    print("\nSelect a planet:")
    for planet in gravity_ratio:
        print(f"- {planet.title()}")

    planet_choice = input("Enter the name of your planet: ").lower()

    if planet_choice in gravity_ratio:
        new_weight = earth_weight * gravity_ratio[planet_choice]
        print(f"Your weight on {planet_choice.title()} is {new_weight:.2f} kg")
    else:
        print("Invalid planet choice.")

if __name__ == "__main__":
    main()
