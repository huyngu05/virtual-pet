import random
import time

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50  # 0-100 scale, 0 being very hungry
        self.energy = 50  # 0-100 scale, 0 being very tired
        self.happiness = 50  # 0-100 scale, 0 being sad
        self.age = 0  # Pet's age in rounds
        self.is_alive = True

    def feed(self):
        """Feed the pet to increase hunger and happiness."""
        if self.is_alive:
            print(f"You fed {self.name}.")
            self.hunger = min(self.hunger + 20, 100)  # Max hunger at 100
            self.happiness = min(self.happiness + 10, 100)  # Max happiness at 100
        else:
            print(f"{self.name} is no longer with us...")

    def play(self):
        """Play with the pet to increase happiness and decrease energy."""
        if self.is_alive:
            print(f"You played with {self.name}.")
            self.happiness = min(self.happiness + 15, 100)  # Max happiness at 100
            self.energy = max(self.energy - 20, 0)  # Energy can't go below 0
        else:
            print(f"{self.name} is no longer with us...")

    def sleep(self):
        """Let the pet sleep to restore energy."""
        if self.is_alive:
            print(f"{self.name} is sleeping.")
            self.energy = min(self.energy + 30, 100)  # Max energy at 100
        else:
            print(f"{self.name} is no longer with us...")

    def check_status(self):
        """Check the pet's current status (hunger, energy, happiness)."""
        print(f"{self.name}'s status:")
        print(f"Hunger: {self.hunger}/100")
        print(f"Energy: {self.energy}/100")
        print(f"Happiness: {self.happiness}/100")
        print(f"Age: {self.age} rounds\n")

    def update(self):
        """Update the pet's stats over time and check if it is alive."""
        if self.is_alive:
            self.age += 1
            # Pet's stats degrade over time
            self.hunger = min(self.hunger + random.randint(5, 10), 100)  # Pet gets hungrier
            self.energy = max(self.energy - random.randint(5, 10), 0)  # Pet gets more tired
            self.happiness = max(self.happiness - random.randint(5, 10), 0)  # Pet gets less happy

            # If pet's hunger or energy reaches critical levels, it might "die"
            if self.hunger >= 100 or self.energy == 0:
                self.is_alive = False
                print(f"{self.name} has passed away due to neglect...")

        else:
            print(f"{self.name} is no longer with us.")

def main():
    # Start the game by asking for the pet's name
    pet_name = input("What will you name your pet? ")
    pet = Pet(pet_name)

    # Game loop
    while pet.is_alive:
        # Display current pet status
        pet.check_status()

        # Present the user with options
        print("What would you like to do?")
        print("1. Feed the pet")
        print("2. Play with the pet")
        print("3. Let the pet sleep")
        print("4. Check pet status")
        print("5. Quit the game")

        # Get user's choice
        choice = input("Choose an option (1/2/3/4/5): ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.sleep()
        elif choice == "4":
            pet.check_status()
        elif choice == "5":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice, please try again.")

        # Update the pet's stats and simulate time passing
        pet.update()

        # Add a small delay to make the game feel more interactive
        time.sleep(1)

if __name__ == "__main__":
    main()
