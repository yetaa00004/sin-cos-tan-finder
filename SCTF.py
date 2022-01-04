import math
# sin/sinh/cos/cosh/tan/tanh finder
# available commands: adj, hyp, opp. Do not attempts trying any other command or else and error will pop up!

__whatsx__ = input("Enter whats the x/Uknown: ")
__whatsgivenside__ = input("Enter whats the given side: ")
__whatsgivennum__ = float(input("Enter whats the given number of " + str(__whatsgivenside__) + ": "))
__whatsvalueofangle__ = float(input("Enter the value of the angle: "))


if __whatsgivenside__ == "hyp" and __whatsx__ == "opp" and __whatsvalueofangle__ and __whatsgivennum__:
    print("We are going to be using sin!")
    print("let the math do its magic!!!")
    result = math.sin(math.radians(__whatsvalueofangle__)) * __whatsgivennum__
    print(result)
elif __whatsgivenside__ == "opp" and __whatsx__ == "hyp" and __whatsvalueofangle__ and __whatsgivennum__:
    print("We are going to be using sin!")
    print("let the math do its magic!!!")
    result = math.sin(math.radians(__whatsvalueofangle__)) / __whatsgivennum__
    print(result)
elif __whatsgivenside__ == "adj" and __whatsx__ == "hyp" and __whatsvalueofangle__ and __whatsgivennum__:
    print("We are going to be using cos!")
    print("let the math do its magic!!!")
    result = math.cos(math.radians(__whatsvalueofangle__)) / __whatsgivennum__
    print(result)
elif __whatsgivenside__ == "hyp" and __whatsx__ == "adj" and __whatsvalueofangle__ and __whatsgivennum__:
    print("We are going to be using cos!")
    print("let the math do its magic!!!")
    result = math.cos(math.radians(__whatsvalueofangle__)) * __whatsgivennum__
    print(result)
elif __whatsgivenside__ == "adj" and __whatsx__ == "opp" and __whatsvalueofangle__ and __whatsgivennum__:
    print("We are going to be using tan!")
    print("let the math do its magic!!!")
    result = math.tan(math.radians(__whatsvalueofangle__)) * __whatsgivennum__
    print(result)
elif __whatsgivenside__ == "opp" and __whatsx__ == "adj" and __whatsvalueofangle__ and __whatsgivennum__:
    print("We are going to be using tan!")
    print("let the math do its magic!!!")
    result = math.tan(math.radians(__whatsvalueofangle__)) / __whatsgivennum__
    print(result)

