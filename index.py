from dataset import users, countries
from pprint import pprint


# function check password consists of numbers only
def check_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


users_wrong_password = []
girls_drivers = []
user_countries = []
friends_salary = 0
max_salary = 0
driver_number = 0
flights_number = 0
avg_flights = 0
best_occupation = {}
vip_user = ''

for user in users:
    # clean lis user_salary for user
    user_salary = [0]
    # function check password consists of numbers only, if true add user to list users_wrong_password
    if check_int(user['password']):
        users_wrong_password.append({'name': user['name'], 'mail': user['mail'], 'password': user['password']})

    if user.get('friends', False):
        user_friends = user['friends']
        # looking for user's friends
        for user_friend in user_friends:
            # check user has female drivers friend and add friend to list girls_drivers
            if user_friend['sex'] == 'F' and user_friend.get('cars', False):
                girls_drivers.append(user_friend['name'])

            # check user has driver friend
            if user_friend.get('cars', False):
                driver_number = +1
                if user_friend.get('flights', False):
                    flights_number = + len(user_friend['flights'])

            # check flights from list countries and add user's name in list user_countries

            if user_friend.get('flights', False):
                for user_flight in user_friend['flights']:
                    if user_flight['country'] in countries and user not in user_countries:
                        user_countries.append(user)

            # find job with max salary
            occupation = user_friend['job']

            if occupation['salary'] > friends_salary:
                friends_salary = occupation['salary']
                best_occupation = occupation.copy()
            # add salary to user_salary list
            user_salary.append(occupation['salary'])
    # calculate sum salary from user_salary list, check max if true change vip_user
    if sum(user_salary) > max_salary:
        max_salary = sum(user_salary)
        vip_user = user['name']

avg_flights = flights_number / driver_number

# remove element from users equal element from list user_countries
for user in user_countries:
    if user in users:
        users.remove(user)


pprint(users)
#pprint(countries)
#pprint(users_wrong_password)
#pprint(girls_drivers)
#pprint(best_occupation)
#pprint(vip_user)
#pprint(driver_number)
#pprint(flights_number)
#pprint(avg_flights)
#pprint(user_countries)

