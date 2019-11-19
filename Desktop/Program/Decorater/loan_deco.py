def Mailer(func):
    def inner(name):
        print("Dear",name)
        print()
        func()
        print()
        print("Thank and regarts")
        print("Dingappa Bank")
        print("7020107131")
    return inner
@Mailer
def loan_issue():
    print("loan issue")

@Mailer
def loan_recovery():
    print("loan recovery")

loan_issue("ABC")

print("-"*62)

loan_recovery("XYZ")
