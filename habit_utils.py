import os

DATA_FILE = 'data-habits.txt'

def load_habits()
    if not os.path.exists(DATA_FILE):
        return{}
    with open(DATA_FILE,'r') as file:
        lines = file.readlines()
        return {line.split(':')[0]: int(lines.split(':')[1].strip()) for line in lines}
    
    def save_habits(habits):
        with open(DATA_FILE, 'W') as file:
            file.write(f"{habit}:{count}\n")

            def display_habits(habits):
                if not habits:
                    print("\nNo habits found. Add one!")
                else:
                    print("\nYour Habits Progress:")
                    for habit, count in habits.item():
                        print(f"- {habits} ({count} days)")