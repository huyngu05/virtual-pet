import time
import json

class Pet:
    def __init__(self, name):
        """Initialize the pet with a name and default stats"""
        self.name = name
        self.hunger = 50  # Hunger level (0-100 scale, 100 being very hungry)
        self.energy = 50  # Energy level (0-100 scale, 100 being very energetic)
        self.happiness = 50  # Happiness level (0-100 scale, 100 being very happy)
        self.days_since_last_care = 0  # Track the number of "days" since the last care event
        self.age = 0  # Pet's age (starting from 0 years)



    def feed(self):
        """Feed the pet, decrease hunger, increase energy and happiness"""
        if self.hunger > 0:
            self.hunger -= 20  # Decrease hunger
            self.energy = min(100, self.energy + 10)  # Increase energy
            self.happiness = min(100, self.happiness + 10)  # Increase happiness
            print(f"{self.name} has been fed.")
        else:
            print(f"{self.name} is not hungry!")
        self.reset_days_since_care()


    def play(self):
        """Play with the pet, decrease energy, increase happiness"""
        if self.energy > 0:
            self.energy -= 20  # Decrease energy
            self.happiness = min(100, self.happiness + 20)  # Increase happiness
            print(f"{self.name} is playing!")
        else:
            print(f"{self.name} is too tired to play!")
        self.reset_days_since_care()


    def sleep(self):
        """Let the pet sleep, increase energy and happiness"""
        self.energy = min(100, self.energy + 30)  # Increase energy
        self.happiness = min(100, self.happiness + 5)  # Small happiness boost
        print(f"{self.name} is sleeping and resting.")
        self.reset_days_since_care()


    def reset_days_since_care(self):
        """Reset the days since the last care action"""
        self.days_since_last_care = 0

    def age_pet(self):
        """Age the pet over time and trigger events based on age"""
        self.age += 1
        if self.age % 5 == 0:  # Trigger a birthday event every 5 years
            print(f"Happy {self.age}th Birthday, {self.name}!")

    def deteriorate_stats(self):
        """Deteriorate stats if the pet has not been cared for in a while"""
        if self.days_since_last_care > 3:  # After 3 days without care
            self.hunger = min(100, self.hunger + 10)
            self.energy = max(0, self.energy - 10)
            self.happiness = max(0, self.happiness - 5)
            print(f"{self.name} is feeling worse due to neglect!")

    def check_needs(self):
        """Check if pet's stats are too low and notify the user"""
        if self.hunger > 80:
            print(f"{self.name} is extremely hungry! Please feed it soon.")
        elif self.energy < 20:
            print(f"{self.name} is very tired! It needs some rest.")
        elif self.happiness < 20:
            print(f"{self.name} looks sad. Play with it to make it happy.")

    def get_ascii_art(self):
        """Get an ASCII art representation of the pet based on its stats"""
        if self.happiness < 30:
            return f"Sad {self.name}: :( \n  |   |\n / \\ / \\"
        elif self.energy < 30:
            return f"Tired {self.name}: Zzz... \n  |   |\n  |   |\n / \\"
        else:
            return f"Happy {self.name}: :D \n  |   |\n / \\ / \\"
        
    def save_pet(self, filename="pet_state.json"):
        """Save the pet's state to a file"""
        pet_data = {
            "name": self.name,
            "hunger": self.hunger,
            "energy": self.energy,
            "happiness": self.happiness,
            "age": self.age,
            "days_since_last_care": self.days_since_last_care
        }
        with open(filename, "w") as f:
            json.dump(pet_data, f)
        print(f"Pet state saved to {filename}.")

    def load_pet(self, filename="pet_state.json"):
        """Load the pet's state from a file"""
        try:
            with open(filename, "r") as f:
                pet_data = json.load(f)
                self.name = pet_data["name"]
                self.hunger = pet_data["hunger"]
                self.energy = pet_data["energy"]
                self.happiness = pet_data["happiness"]
                self.age = pet_data["age"]
                self.days_since_last_care = pet_data["days_since_last_care"]
            print(f"Pet state loaded from {filename}.")
        except FileNotFoundError:
            print("No saved pet state found.")

    def get_status(self):
        """Return the current status of the pet"""
        return f"{self.name}'s Status:\nHunger: {self.hunger}%\nEnergy: {self.energy}%\nHappiness: {self.happiness}%\nAge: {self.age} years"
    


    
def main():
    # Initialize the pet object
    pet_name = input("Enter the name of your pet: ")
    pet = Pet(pet_name)

    # Game loop
    while True:
        # Display pet's ASCII art
        print(pet.get_ascii_art())

        # Simulate passing time
        pet.days_since_last_care += 2
        pet.deteriorate_stats()  # Pet stats may deteriorate due to neglect

        # Aging process
        if pet.days_since_last_care % 30 == 0:  # Age the pet once per month (30 days)
            pet.age_pet()

        # Display the menu
        print("\nWhat would you like to do?")
        print("1. Feed the pet")
        print("2. Play with the pet")
        print("3. Let the pet sleep")
        print("4. Check pet's status")
        print("5. Quit the game")
        print("6. Load saved game")
        print("7. Quit the game")

        action = input("Choose an option (1-7): ")

        if action == "1":
            pet.feed()
        elif action == "2":
            pet.play()
        elif action == "3":
            pet.sleep()
        elif action == "4":
            print(pet.get_status())
        elif action == "5":
            pet.save_pet()
        elif action == "6":
            pet.load_pet()
        elif action == "7":
            print(f"Goodbye! {pet.name} will miss you!")
            break
        else:
            print("Invalid choice, please select a number between 1 and 7.")

# Simulate real-time waiting (1 second per action for realism)
        time.sleep(1)

if __name__ == "__main__":
    main()