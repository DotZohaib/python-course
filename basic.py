# data = []

# name = str(input("Enter Your name: " ))
# age = int(input("Enter Your Age: " ))
# department = str(input("Enter Your Department: " ))

# data.append([name, age, department])

# print(data)

# value = ["Coding", "Testing", "Deployment", "Coding", "Debugging"]

# value.remove("Coding")
# print(value)


# print(value[2:1])
# print(value[2:1:-1])


# for i in value:
#     print(i)

# for key,value in enumerate(value):
#     print(key, value)


# if "Deploymentw" in value:
#     print("Yes, Deployment is present in the list")
# else:
#     print("No, Deployment is not present in the list")



my_tuple = ("apple", "banana", "cherry")

# my_tuple[1] = "kiwi"  # This will raise an error because tuples are immutable
data = my_tuple.count("apple")  # This will return the count of "apple" in the tuple
ind = my_tuple.index("banana")  # This will return the index of "banana" in the tuple

new_tuple = my_tuple + ("orange",)  # This will create a new tuple by concatenating another tuple
extra_tuple = ("grape", "kiwi")
new_tuple = new_tuple + extra_tuple  # This will create a new tuple by concatenating another tuple


print(my_tuple)
print(data)
print(ind)
print(new_tuple)