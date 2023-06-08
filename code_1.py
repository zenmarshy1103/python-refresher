# Sting formatting 
# - using f-string
# - using Template Literals

name = "bob"
name = "Jason"
today = "Thursday"
greeting = f">> f-string: Hello, {name}"  # Using f-string for string formatting
greeting3 = f">> f-string: Hello {name} today is {today}"
greeting1 = ">> Template Literal: Hello, {}".format(name) # Using template literal for string formatting
greeting2 = ">> Template Literal: Good morning {}, today is {}".format(name, today)

print(greeting)
print(greeting3)
print(greeting1)
print(greeting2)
