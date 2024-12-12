# Dictionary -> key : value Pair
# 1. it is unordered
# 2. we dont have any indexes
# 3. dict are mutable

# dict={
#     "name":"Chinki",
#     "Marks":[95,92,98],
#     "CGPA":9.6
# }
# print(type(dict))
# print(dict)

# print(dict["name"])

# dict["CGPA"]=8.6

# print(dict)

# dict["state"]="Karnataka"

# print(dict)

# Nested Dictionary

student={
    "name":"Rakesh",
    "Score":{
        "Chem":84,
        "Phy":55,
        "Maths":33
    }
}

# print(student["Score"]["Chem"])


# dict={
#     "name":"Chinki",
#     "Marks":[95,92,98],
#     "CGPA":9.6
# }

# Methods

# print(student.keys())

# print(student.values())

# print(dict.items())

# print(dict.get("name"))


dict={
    "name":"Chinki",
    "Marks":[95,92,98],
    "CGPA":9.6
}

new_dict={
    "name":"Babu Rao",
    "city":"delhi"
}

dict.update(new_dict)

print(dict)

