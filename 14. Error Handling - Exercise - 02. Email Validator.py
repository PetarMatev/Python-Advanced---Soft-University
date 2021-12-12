# 02. Email Validator:
class Error(Exception):
    pass


class NameTooShortError(Error):
    """Name must be more than 4 characters"""


class MustContainAtSymbolError(Error):
    """Email must contain @"""


class InvalidDomainError(Error):
    """Domain must be one of the following: .com, .bg, .org, .net"""


while True:
    command = input()
    if command == "End":
        break
    email = command

    body = email.split("@")[0]
    if len(body) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    domain = email.split(".")[1]
    correct_domains = ["com", "bg", "org", "net"]
    if domain not in correct_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
