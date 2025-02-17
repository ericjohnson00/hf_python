fn = "Darius-13-100m-Fly.txt"

# print(dir(fn))

# help(fn.split)

print(fn.split("-"))

name = fn.split("-")[0]
age = fn.split("-")[1]
distance = fn.split("-")[2]
stroke = fn.split("-")[3]

print(name, age, distance, stroke)