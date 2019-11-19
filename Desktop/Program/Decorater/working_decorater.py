#sample working of decorater

def deco(func):
    print("Control entered into decorater")
    def inner():
        print("Control entered into inner")
        func()
        print("Control is leaving inner ")
    print("Control is leaving outer")
    return inner

@deco
def sample():
    print("-"*62)
    print("Control entered into sample")
    print("Control is leaving sample")
    print("-"*62)
print("-"*62)

sample()
        
