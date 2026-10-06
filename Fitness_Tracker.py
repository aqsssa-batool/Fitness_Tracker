from abc import ABC, abstractmethod
#Abstract Class:
class Workout(ABC):
    def __init__(self,name,minutes):
        self.name = name
        self.__completed = False
        self.minutes = minutes

    @abstractmethod
    def core_action(self):
        pass

    def mark_completed(self):
        self.__completed = True

    def is_completed(self):
        return self.__completed

    def __str__(self):
        return f"Name : {self.name}, Minutes : {self.minutes}"

# Subclass Run
class Run(Workout):
    def __init__(self,name,minutes):
        super().__init__(name,minutes)

    def core_action(self):
        return self.minutes * 7

# Subclass Swim
class Swim(Workout):
    def __init__(self,name,minutes):
        super().__init__(name,minutes)

    def core_action(self):
        return self.minutes * 9

# For Fitness Tracker

class FitnessTracker:

    def __init__(self):
        self.workouts = []
        self.workout_types = set()
        self.calorie_summary = {}

# Using Default Argument

    def add_workouts(self,workout, update_summary =True):

        self.workouts.append(workout)
        self.workout_types.add(workout.__class__.__name__)
        calories = workout.core_action()

        if update_summary:

            workout_type = workout.__class__.__name__

            self.calorie_summary[workout_type] = (
            self.calorie_summary.get(workout_type, 0) + calories)

    def add_multiple(self, *workouts):  #*args

        for workout in workouts:
            self.add_workouts(workout)

# List Comorehension:
    def get_names(self):

        return [
            workout.name
            for workout in self.workouts
        ]
# Sorted()
    def sort_by_calories(self):
        return sorted(self.workouts, 
                key = lambda workout: workout.core_action(),reverse=True) 
    
# Instances
run1=Run("Aqsa", 30)
run2 = Run("Areesha", 20)

swim1 = Swim("Ayesha", 45)
swim2 = Swim("Ali",60)

# Tracker
tracker = FitnessTracker()

tracker.add_multiple(run1,run2,swim1,swim2)

print("\n === Types Of Workout ===")

print(tracker.workout_types)

print("\n === Overall WorkOut===")

for workout in tracker.workouts:
    print(workout, "Calories: ", workout.core_action())

# Polymorphism:
print("\n === Total Calories Burned by Each Person ===")

for workout in tracker.workouts:
    print(workout.name, "burned", workout.core_action(), "calories in", workout.minutes,"minutes.")

print("\n === Calories in Sorted Form ===")

for workout in tracker.sort_by_calories():
    print(f"{workout.name}'s Total Calories : {workout.core_action()}")


print("\n === Status ===")

run1.mark_completed()
print(run1.name, "Completed: ", run1.is_completed())

run2.mark_completed()
print(run2.name, "Completed: ", run2.is_completed())

swim1.mark_completed()
print(swim1.name, "Completed: ", swim1.is_completed())

swim2.mark_completed()
print(swim2.name, "Completed: ", swim2.is_completed())


# Dic:
print("\n === Calorie Summary ===")

print(tracker.calorie_summary)