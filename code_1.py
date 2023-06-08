# Lists, Tuples and Sets
# - Lists (element is in order)
# - Tuples (Not Mute-able)
# - Sets (Duplicated element is ignored and does not have order)

#Lists
# - Subscript is used to get get the position of the element ie l[0] first element etc
l = [ "Bob", "Rolf", "Anne"]

#Tuples
# Cannot add or remove elements
# - Subscript is used to get get the position of the element ie l[0] first element etc
t = ("Bob", "Rolf", "Anne")

#Sets
# Cannot contain duplicates, ignores the duplicated element
# - cannot use subscript to get the position of the element
# - sets do not have order
s = {"Bob", "Rolf", "Anne", "Anne"}
print(s)

for element in s:
    print(element)


# > Change value of element
# - List
l[2] = "Jason"
print(l)

# - Tuples (not mute-able)
# t[0] = "nick"
# print(t)

# - Sets (does not have subscription so values cannot be changed)

# > Add Element
# - List
l.append('Faye')
print(l)

# - Tuple (not Mute-able)

# - Sets
s.add("Cyrus")
print(s)


# > Remove Element
# - List
l.remove('Jason')
print(l)

# - Tuple (not Mute-able)




