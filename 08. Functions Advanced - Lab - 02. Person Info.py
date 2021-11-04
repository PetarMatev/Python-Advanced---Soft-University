# 02. Person Info:
def get_info(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"


person = {"age": 20, "name": "George", "town": "Sofia"}
print(get_info(**person))
