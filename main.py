from habit_utils import load_habits, save_habits, display_habits

def main():
    habits = load_habits()
    while True:
        print("\n=== Personal Habit Tracker ===")
        print("1. View Habits")
        print("2. Add New Habit")
        print("3. Mark Habit Done")
        print("4. Exit")
        choice = input("\nChoose an option: ")

        if choice == '1':
            display_habits(habits)

        elif choice == '2':
            new_habit = input("\nEnter the new habit: ").strip()
            habits[new_habit] = 0
            save_habits(habits)
            print(f"\n✅ '{new_habit}' added to your habits!")

        elif choice == '3':
            display_habits(habits)
            habit_name = input("\nWhich habit did you complete? (type exactly): ").strip()
            if habit_name in habits:
                habits[habit_name] += 1
                save_habits(habits)
                print(f"\n🎉 Great! '{habit_name}' progress updated.")
            else:
                print("\n❗ That habit doesn't exist.")

        elif choice == '4':
            print("\nGoodbye. Keep up the habits!")
            break

        else:
            print("\nInvalid choice. Try again.")


if __name__ == "__main__":
    main()  


