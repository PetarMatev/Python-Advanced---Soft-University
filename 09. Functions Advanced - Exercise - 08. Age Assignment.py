# 08. Age Assignment:
def age_assignment(*args, associations=None, **kwargs):
    if associations is None:
        associations = dict()

    if not args:
        return associations

    first_name = args[0]
    first_letter = args[0][0]

    associations[first_name] = kwargs[first_letter]
    return age_assignment(*args[1:], associations=associations, **kwargs)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))