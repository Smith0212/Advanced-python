import os

def log_exercises():
    data = input("enter the data: ")
    exercise_type = input("Enter the exercise type: ")
    duration = float(input("Enter the duration (in minutes): "))
    calories_burned = float(input("Enter the calories burned: "))

    with open("exercises.txt", "a") as f:
        f.write(f"{data},{exercise_type},{duration},{calories_burned}\n")
    print("Exercise logged successfully!")

def view_exercises():
    if not os.path.exists("exercises.txt"):
        print("No exercise logs found.")
        return
    with open("exercises.txt", "r") as f:
        exercises_list = f.readlines()
    if not exercises_list:
        print("No exercise logs found.")
        return
    print("Exercise Logs:")
    print("-" * 60)
    print("Date\t\tExercise Type\tDuration (mins)\tCalories Burned")
    print("-" * 60) 
    for log in exercises_list:
        date, exercise_type, duration, calories_burned = log.strip().split(',')
        print(f"{date}\t{exercise_type}\t\t{duration}\t\t{calories_burned}")
    print("-" * 60)
    
def main() :
    while True:
        print("1. Log Exercises")
        print("2. View Exercises")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            log_exercises()
        elif choice == "2":
            view_exercises()
        elif choice == "3":
            print("Exiting..")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
        
reviews