# Exercise 1: Vowel or Consonant


def check_letter():
    letter = input("Enter a single letter: ")

    if len(letter) != 1 or not letter.isalpha():
        print("invalid input. Please enter a single letter.")
        return
        
    letter = letter.lower()

    if letter in "aeiou":
        return(f"The letter {letter} is a vowel.")
    else:
        return(f"The letter {letter} is a consonant.")

   
check_letter()


# Exercise 2: Old enough to vote?

def check_voting_eligibility(age):
    voting_age = 18
    age = int(input("Please enter your age:"))
    if age < 0:
        return("Age cannot be negative.")
    elif age < voting_age:
        return("Not eligible to vote.")
    else:
        return("Eligible to vote.")

check_voting_eligibility()



# Exercise 3: Calculate Dog Years


def calculate_dog_years():
   age = int(input("Input a dog's age:"))

   if age <= 2:
       dog_years = age *10
   else:
       dog_years =20 + (age -2) * 7

       return dog_years
   

print (f"The dog's age in dog years is {calculate_dog_years}.")


# Exercise 4: Weather Advice

def weather_advice():
   temp_cold = input("Is it cold? (yes/no): ").lower()
   raining = input("Is it raining? (yes/no): ").lower()
    
   if temp_cold == "yes" and raining == "yes":
        print("Wear a waterproof coat.")
   elif temp_cold == "yes" and raining == "no":
        print("Wear a warm coat.")
   elif temp_cold == "no" and raining == "yes":
        print("Carry an umbrella.")
   else:
        print("Wear light clothing.")
   
# Call the function
weather_advice()


# Exercise 5: What's the Season?


def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ")
    day = int(input("Enter the day of the month: "))
    if (month == "Dec" and day >= 21) or (month in ("Jan", "Feb")) or (month == "Mar" and day <= 19):
        season = "Winter"
    elif (month == "Mar" and day >= 20) or (month in ("Apr", "May")) or (month == "Jun" and day <= 20):
        season = "Spring"
    elif (month == "Jun" and day >= 21) or (month in ("Jul", "Aug")) or (month == "Sep" and day <= 21):
        season = "Summer"
    else:
        season = "Fall"

return f"{month} {day} is in {season}."

# Call the function
print (determine_season())





