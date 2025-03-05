fn = "Darius-13-100m-Fly.txt"

# print(dir(fn))

# help(fn.split)

# print(fn.split("-"))

# name = fn.split("-")[0]
# age = fn.split("-")[1]
# distance = fn.split("-")[2]
# stroke = fn.split("-")[3]

# print(name, age, distance, stroke)

help(fn.removesuffix)

print(fn.removesuffix(".txt"))

"Fly.txt".removesuffix(".txt")
"Free.txt".removesuffix(".txt")
"Back.txt".removesuffix(".txt")
"Breast.txt".removesuffix(".txt")

swimmer, age, distance, stroke = fn.removesuffix(".txt").split("-")
print(swimmer, age, distance, stroke)


fn = "Abi-10-50m-Back.txt"
swimmer, age, distance, stroke = fn.removesuffix(".txt").split("-")
print(swimmer, age, distance, stroke)
