# 1. A way to store data
# 2. A way to loop over data
# 3. A way to make decisions
# 4. Display data


# Ways to store data in python

# variables

# example_variable = 'example'

# example_list = [1,2,3,4,5]

# example_dictionary = {'1': 1, '2': 2}

# example_tuple = ('a', 'b', 'b')


# Ways to loop over data

# A for loops will automatically stop when the work is done,



# for each_number in example_list:
#     print(each_number)

# for key, value in example_dictionary.items():
#     print('key', key, 'value', value)


# list_of_users = ['john', 'mary', 'jane', 'cyndi']


# for user in list_of_users:
#     print(user.capitalize())



# While loops
# While loops do something as long as a condition is met.
# its a for loop that needs to make a decision.

#list_of_users = ['john', 'mary', 'jane', 'cyndi']
#                  0       1        2       3


# while list_of_users:
#     print(list_of_users[0])
#     list_of_users.pop(count)


# count = 0

# only loop while count is less or equal to the length of the list
# while count <= (len(list_of_users) - 1):
    # len neasures the length of the list. Which is 4.
    # if we look at the list, there are 4 items.
    # but the fourth item has an idex of 3.
    # thats because the index starts at 0.
    # print(f'Count is {count}', list_of_users[count])
    # count += 1


# A way to make decisions

# if some condition is met
# do thing

# if it is not met
# do another thing

# either way
# do this


# list_of_users = ['john', 'mary', 'jane', 'cyndi']

# for user in list_of_users:
#     if user == 'jane': # this condition is met or True
#         print('Hey I found Jane!')
#     else:
#         print('Not Jane!')

# if
# elif
# else

# total = 2 + 2
# if total == 4:
#     print('Yes, 4.')



# A way of displaying data

#print('Hello, world.')


# import pprint

# list_of_users = ['john', 'mary', 'jane', 'cyndi']

# pretty_print = pprint.PrettyPrinter(width=2, compact=True)

# pretty_print.pprint(list_of_users)