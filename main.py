def check_gpa(gpa):
    # Work inside of this function to check the persons gpa,
    # if the gpa is greater than or equal to 3.8 return a string that says, Automatically Accepted
    if gpa >= 3.8:
        return "Automatically Accepted!"
    # if the gpa is between 3.3 and 3.8, return a string that says, Needs In Person Interview
    if gpa >= 3.3 and 3.8:
        return 'Needs in-person interview'
    # if the gpa is below 3.3, return a string that says, Not Accepted
    if gpa < 3.3:
        return 'Not Accepted'

    # Remove the below print statement once you return something, python doesn't like empty blocks :)
print(check_gpa(3.8))
