# 07. Keyword Arguments Length:
def kwargs_length(keys=None, **kwargs):
    if keys is None:
        keys = list(kwargs.keys())

    if not keys:
        return 0

    return kwargs_length(keys=keys[1:], **kwargs)+1


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
