#Code writen by Hakeem BADEJO for FREECODECAMP : Scientific
#computing with Python certification.

def arithmetic_arranger(val, showRes = False):
    #varibale declaration
    varDict = {
        "charTest": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "topValHolder": "",
        "lowValHolder": "",
        "separator": "",
        "opeVal": "",
        "space": " ",
        "tempAns": "",
        "answer": "",
        "arranged_problems": "",
        "calc": True
    }

    #Checking the length of array provided
    if len(val) > 5:
        return 'Error: Too many problems.'

    for _ in enumerate(val):
        #Varaible declaration
        num1, num2, sep,  = _[1].split()[0], _[1].split()[2], _[1].split()[1]
        maxVal = max(len(num1), len(num2))

        # Fulfilment of condition 1. Operations can only be + or -.
        if "+" not in _[1] and "-" not in _[1]:
            return "Error: Operator must be '+' or '-'."

        # Fulfilment of condition 2. Values must be digit.
        for char in varDict["charTest"]:
            if char in _[1] or char.lower() in _[1]:
                return 'Error: Numbers must only contain digits.'

        # fulfilmet of condition 3. Each values cannot be more that 4 digits.
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        #Performing math operation
        if sep == "+":
            ##Performing addition operation
            varDict["tempAns"] = int(num1) + int(num2)
        elif sep == "-":
            ##Performing subtraction operation
            varDict["tempAns"] = int(num1) - int(num2)

        # Code to run when all conditions are fulfilled.
        if varDict["calc"] == True:
            # if statement to handle space difference due digit and space length.
            # This case is to handle only the first occurrence.
            varDict["topValHolder"] += num1.rjust(maxVal + 2)
            varDict["lowValHolder"] += sep + " " + num2.rjust(maxVal)
            varDict["separator"] += "-" * (maxVal + 2)
            varDict["answer"] += str(varDict["tempAns"]).rjust(maxVal + 2)
            varDict["calc"] = False
        else:
            # else statement to handle space difference due digit and space length.
            # This case is to handle second occurrence and after.
            varDict["topValHolder"] += num1.rjust(maxVal + 6) #Six spaces before to handle operator and space.
            varDict["lowValHolder"] += sep.rjust(5) + " " + num2.rjust(maxVal)
            varDict["separator"] += "    " + "-" * (maxVal + 2)
            varDict["answer"] += "    " + str(varDict["tempAns"]).rjust(maxVal + 2)


    varDict["arranged_problems"] = varDict["topValHolder"] + '\n' + varDict["lowValHolder"] +'\n' + varDict["separator"]

    if showRes == True:
        ##Concatenating result
        varDict["arranged_problems"] = varDict["topValHolder"] + '\n' + varDict["lowValHolder"] + '\n' + varDict["separator"] + '\n' + varDict["answer"]

    return varDict["arranged_problems"]