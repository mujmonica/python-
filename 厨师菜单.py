breakfast_special="bs"
breakfast_notes="contains brisket"

lunch_special="ls"
lunch_notes="with sauce"

dinner_special="ds"
dinner_notes="no meat"

meal_time=raw_input("which meal[breakfast,lunch,dinner]")
meal_time=meal_time.lower()
meal_time=meal_time.strip()

print "specials for {}:".format(meal_time)
if meal_time =="breakfast":
    print breakfast_special
    print breakfast_notes
elif  meal_time =="lunch":
    print lunch_special
    print lunch_notes
elif meal_time =="dinner":
    print dinner_special
    print dinner_notes
else:
    print "sorry"
    
