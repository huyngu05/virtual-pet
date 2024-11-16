import time

class Pet:
    def __init__(self, name):
        """Initialize the pet with a name and default stats"""
        self.name = name
        self.hunger = 50  # Hunger level (0-100 scale, 100 being very hungry)
        self.energy = 50  # Energy level (0-100 scale, 100 being very energetic)
        self.happiness = 50  # Happiness level (0-100 scale, 100 being very happy)

    def feed(self):
        """Feed the pet, decrease hunger, increase energy and happiness"""
        if self.hunger > 0:
            self.hunger -= 20  # Decrease hunger
            self.energy = min(100, self.energy + 10)  # Increase energy
            self.happiness = min(100, self.happiness + 10)  # Increase happiness
            print(f"{self.name} has been fed.")
        else:
            print(f"{self.name} is not hungry!")

    def play(self):
        """Play with the pet, decrease energy, increase happiness"""
        if self.energy > 0:
            self.energy -= 20  # Decrease energy
            self.happiness = min(100, self.happiness + 20)  # Increase happiness
            print(f"{self.name} is playing!")
        else:
            print(f"{self.name} is too tired to play!")

    def sleep(self):
        """Let the pet sleep, increase energy and happiness"""
        self.energy = min(100, self.energy + 30)  # Increase energy
        self.happiness = min(100, self.happiness + 5)  # Small happiness boost
        print(f"{self.name} is sleeping and resting.")

    def reset_days_since_care(self):
        """Reset the days since the last care action"""
        self.days_since_last_care = 0

    def age_pet(self):
        """Age the pet over time and trigger events based on age"""
        self.age += 1
        if self.age % 5 == 0:  # Trigger a birthday event every 5 years
            print(f"Happy {self.age}th Birthday, {self.name}!")

    def get_status(self):
        """Return the current status of the pet"""
        return f"{self.name}'s Status:\nHunger: {self.hunger}%\nEnergy: {self.energy}%\nHappiness: {self.happiness}%"
    
def main():
    # Initialize the pet object
    pet_name = input("Enter the name of your pet: ")
    pet = Pet(pet_name)

    # Game loop
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed the pet")
        print("2. Play with the pet")
        print("3. Let the pet sleep")
        print("4. Check pet's status")
        print("5. Quit the game")

        action = input("Choose an option (1-5): ")

        if action == "1":
            pet.feed()
        elif action == "2":
            pet.play()
        elif action == "3":
            pet.sleep()
        elif action == "4":
            print(pet.get_status())
        elif action == "5":
            print(f"Goodbye! {pet.name} will miss you!")
            break
        else:
            print("Invalid choice, please select a number between 1 and 5.")


if __name__ == "__main__":
    main()