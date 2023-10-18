def main():
    meal_time = input("What time is it ?")
    convert(meal_time)

    
def convert(time):
    hours, minutes = time.split(":")
    h = float(hours)
    m = float(minutes) / 60
    z = h + m
    
    if z >= 7 and z <= 8:
        print("Breakfast time")

    elif z >= 12 and z <= 13:
        print("Lunch time")

    elif z >= 18 and z <= 19:
        print("Dinner time")
  

main()