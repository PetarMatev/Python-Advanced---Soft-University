# 03. ValueCannotBeNegative:
class Error(Exception):
    pass


class ValueCannotBeNegative(Error):
    """Raised when the input value is too small"""


num = int(input())
if num < 0:
    raise ValueCannotBeNegative
