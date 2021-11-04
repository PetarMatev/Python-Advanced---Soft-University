# 04. Concatenate:
def concatenate(*strings):
    if strings:
        return concatenate(*strings[:-1]) + strings[-1]
    result = ""
    return result


print(concatenate("Soft", "Uni", "Is", "Great", "!"))
print(concatenate("I", " ", "Love", " ", "Python"))
