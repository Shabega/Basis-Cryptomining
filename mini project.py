def machine():
    keys = "abcdefghijklmnopqurstuvwxyz !"
    value = keys[-1] + keys[0:-1]ora

    encryptDict = dict(zip(keys,value))
    decryptDict = dict(zip(value,keys))

    message=input("Enter your Secret message: ")
    mode = input("Enter the mode : Encode(E) or Decode(D): ")
    if mode.upper() == 'E':
        newmessage = ''.join([encryptDict[letter] for letter in message.lower()])
    elif mode.upper() == 'D':
        newmessage = ''.join([decryptDict[letter] for letter in message.lower()])
    else:
        print("Please enter the correct choice")

    return newmessage

print(machine() )