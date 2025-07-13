# Mauricio Florez
# Get movie rating from user

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def movie_rating():
    my_rating = 5
    #Can also use int() or float()
    user_rating = eval(input('From 1-5 stars. What is your rating for k-pax ?. '))
    if (user_rating > 5):
        return
    diff = my_rating - user_rating
    if (diff > 0):
        print("Mine is: ", my_rating, "I like it better by: ", abs(diff) , " stars")
    elif diff == 0:
        print("We like it the same!")
    else:
        print("Mine is: ", my_rating, "You like it better by: ", abs(diff) ," stars")





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    movie_rating()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
