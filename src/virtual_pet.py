import tkinter as tk
import json
import random


class Pet:
    def __init__(self, name):
        """Initialize the pet with a name and default stats"""
        self.name = name
        self.hunger = 50  # Hunger level (0-100 scale, 100 being very hungry)
        self.energy = 50  # Energy level (0-100 scale, 100 being very energetic)
        self.happiness = 50  # Happiness level (0-100 scale, 100 being very happy)
        self.days_since_last_care = 0  # Track the number of "days" since the last care event
        self.age = 0  # Pet's age (starting from 0 years)
        self.is_sick = False
        self.action_count = 0  # Track the number of actions performed (feeding, playing, etc.)



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

    def check_age(self):
        """Increment the pet's age after a certain number of actions"""
        if self.action_count >= 5:  # After 5 actions, increment age
            self.age_pet()
            self.action_count = 0  # Reset action count after aging the pet

    def age_pet(self):
        """Aging the pet with dynamic milestones"""
        self.age += 1
        milestone_message = ""
        
        if self.age == 3:
            milestone_message = f"{self.name} is now a young adult!"
        elif self.age == 6:
            milestone_message = f"{self.name} is in the prime of their life!"
        elif self.age == 9:
            milestone_message = f"{self.name} is becoming a senior pet."
        elif self.age == 12:
            milestone_message = f"{self.name} is now a senior pet!"
        
        # Additional milestones every 5 years
        if self.age % 5 == 0:
            milestone_message = f"Happy {self.age}th birthday, {self.name}!"
        
        # Aging effects for older pets
        if self.age >= 10:
            self.energy = max(0, self.energy - 5)  # Reduced energy as the pet gets older
            self.happiness = max(0, self.happiness - 3)  # Less happiness for senior pets
            print(f"{self.name} is feeling a bit slower as they age.")
        
        # Prevent the pet from aging forever (set a maximum age)
        if self.age >= 15:
            print(f"{self.name} has lived a long and fulfilling life!")
        
        return milestone_message

    def deteriorate_stats(self):
        """Deteriorate stats if the pet has not been cared for in a while"""
        if self.days_since_last_care > 3:  # After 3 days without care
            self.hunger = min(100, self.hunger + 10)
            self.energy = max(0, self.energy - 10)
            self.happiness = max(0, self.happiness - 5)
            print(f"{self.name} is feeling worse due to neglect!")

        # Chance of pet getting sick over time
        if self.days_since_last_care > 5:
            if random.random() < 0.1:  # 10% chance of getting sick
                self.is_sick = True
                print(f"Oh no! {self.name} is sick!")

    def check_needs(self):
        """Check if pet's stats are too low and notify the user"""
        if self.age >= 10:  # Senior pet needs extra care
            if self.hunger > 70:
                return f"{self.name} is extremely hungry! Senior pets need more food."
            elif self.energy < 30:
                return f"{self.name} is very tired! Senior pets need extra rest."
            elif self.happiness < 30:
                return f"{self.name} looks sad. Senior pets need more love and playtime."
        elif self.age < 3:  # Young pets are more energetic
            if self.energy < 40:
                return f"{self.name} seems low on energy! Young pets are usually active."
            elif self.happiness < 50:
                return f"{self.name} is a bit sad. Play with them to boost their mood."
        else:
            # Default care for pets in the middle of their life
            return f"{self.name} is doing well. Keep up the good work!"

    def get_ascii_art(self):
        """Return ASCII art based on pet's happiness"""
        if self.age >= 10:  # Older pets look different
            return """
             (x_x)
            /|  |  
             |  |  
            """

        if self.happiness >= 70:
            return """
             (\(o)>
             \_  O  )    
              |  |    
            """
        elif self.happiness <= 30:
            return """
             :( 
            /|\  |     
             |   |  
            """
        else:
            return """
             (^_^) 
            /|  |    
             |  |    
            """
        
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


# GUI
class PetGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Virtual Pet Simulator")
        self.pet = None

        # Setup labels and buttons
        self.pet_name_label = tk.Label(self.master, text="Enter the name of your pet: ")
        self.pet_name_label.pack()

        self.pet_name_entry = tk.Entry(self.master)
        self.pet_name_entry.pack()

        self.start_button = tk.Button(self.master, text="Start Game", command=self.start_game)
        self.start_button.pack()

        self.action_label = tk.Label(self.master, text="")
        self.action_label.pack()

        self.status_label = tk.Label(self.master, text="")
        self.status_label.pack()

        self.pet_ascii_label = tk.Label(self.master, text="")
        self.pet_ascii_label.pack()

        # Action buttons
        self.feed_button = tk.Button(self.master, text="Feed", state=tk.DISABLED, command=self.feed_pet)
        self.feed_button.pack()

        self.play_button = tk.Button(self.master, text="Play", state=tk.DISABLED, command=self.play_pet)
        self.play_button.pack()

        self.sleep_button = tk.Button(self.master, text="Sleep", state=tk.DISABLED, command=self.sleep_pet)
        self.sleep_button.pack()

        self.save_button = tk.Button(self.master, text="Save", state=tk.DISABLED, command=self.save_game)
        self.save_button.pack()

        self.load_button = tk.Button(self.master, text="Load", state=tk.DISABLED, command=self.load_game)
        self.load_button.pack()

        self.quit_button = tk.Button(self.master, text="Quit", command=self.quit_game)
        self.quit_button.pack()

    def start_game(self):
        pet_name = self.pet_name_entry.get()
        if pet_name:
            self.pet = Pet(pet_name)
            self.pet_name_label.config(text=f"Pet name: {self.pet.name}")
            self.start_button.config(state=tk.DISABLED)
            self.pet_name_entry.config(state=tk.DISABLED)
            self.feed_button.config(state=tk.NORMAL)
            self.play_button.config(state=tk.NORMAL)
            self.sleep_button.config(state=tk.NORMAL)
            self.save_button.config(state=tk.NORMAL)
            self.load_button.config(state=tk.NORMAL)
            self.update_status()

    def update_status(self):
        status_message = self.pet.check_needs()
        ascii_art = self.pet.get_ascii_art()
        self.status_label.config(text=status_message)
        self.pet_ascii_label.config(text=ascii_art)

    def feed_pet(self):
        if self.pet:
            action = self.pet.feed()
            self.action_label.config(text=action)
            self.update_status()

    def play_pet(self):
        if self.pet:
            action = self.pet.play()
            self.action_label.config(text=action)
            self.update_status()

    def sleep_pet(self):
        if self.pet:
            action = self.pet.sleep()
            self.action_label.config(text=action)
            self.update_status()

    def save_game(self):
        if self.pet:
            self.pet.save_pet()
            self.action_label.config(text=f"{self.pet.name}'s state has been saved.")

    def load_game(self):
        if self.pet:
            self.pet.load_pet()
            self.action_label.config(text=f"{self.pet.name}'s state has been loaded.")
            self.update_status()

    def quit_game(self):
        self.master.quit()

def main():
    root = tk.Tk()
    pet_gui = PetGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()