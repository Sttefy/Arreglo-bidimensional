# Declaring a 2D array for a weekly breakfast list
weekly_breakfasts = [
   ["Monday", "strawberry_smoothie", "toast"],
   ["tuesday", "coffee", "green_empanadas"],
   ["wednesday", "aromatic_water", "mashed"],
   ["thursday", "coffee_in_milk", "pancakes"],
   ["friday", "orange_juice", "warm_eggs"],
   ["saturday", "blackberry_milkshake", "cupcake"],
   ["sunday", "coffee", "ocelot"]
]
# Accessing and printing the breakfast list for a specific day
day_index = 2    # saturday
day = weekly_breakfasts[day_index][0]
items = weekly_breakfasts[day_index][1:2]
print(f"breakfast list for {day} : {"," . join(items)}")