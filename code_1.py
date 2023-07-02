# List Comprehensions
# Allows us to create new list on the fly

numbers = [1, 3 ,5]

doubled = []
 # List Comprehensions
 # <SYNTAX> [<output> for <index> in <list>]
double = [number * 2 for number in numbers]

# Is literally the same as:
for num in numbers:
    doubled.append(num * 2)

print("double List: ", double)
print("doubled List: ", doubled)


friends = ["Cyrus", "Claire", "Clara", "Jason", "Faye"]
# Using list comprehension
# <SYNTAX> [<output> for <index> in <list> <condition> ]
starts_c = [friend for friend in friends if friend.startswith("C")]

# Is the same as:
# for friend in friends:
#     if friend.startswith("C"):
#         starts_c.append(friend)
        
print(starts_c)






