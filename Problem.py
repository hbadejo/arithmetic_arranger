Problem

Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:

  235
+  52
-----
Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

Example
Function Call:

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
Output:

   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
Function Call:

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
Output:

  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
Rules
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:
If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
If the user supplied the correct format of problems, the conversion you return will follow these rules:
There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.
Numbers should be right-aligned.
There should be four spaces between each problem.
There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
Development
Write your code in arithmetic_arranger.py. For development, you can use main.py to test your arithmetic_arranger() function. Click the "run" button and main.py will run.

Testing
The unit tests for this project are in test_module.py. We are running the tests from test_module.py in main.py for your convenience. The tests will run automatically whenever you hit the "run" button. Alternatively you may run the tests by inputting pytest in the console.

Submitting
Copy your project's URL and submit it below.



# x = ['3562 + 4', '5 - 4', '67 + 9']
#
# for _ in x:
#     y = _.split()
#     print(f'''
#         {int(y[0])}
#     {y[1]}   {int(y[2])}
#     ------
#     ''', end='')




# def arithmetic_arranger(numList, calcResult = 'fasle'):

def arithmetic_arranger(problems, B = None):
    let = "abcdefghijklmnopqrstuvwxyz"
    ans = ""
    soln = 0
    str = ""
    opStr = ""
    numspace = " "
    dash = ""
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        for i in enumerate(problems):
            if "+" not in i[1] and "-" not in i[1]:
                return "Error: Operator must be '+' or '-'."
            for letters in let:
                if letters in i[1] or letters.upper() in i[1]:
                   return "Error: Numbers must only contain digits."
            if len(i[1].split()[0]) > 4 or len(i[1].split()[2]) > 4:
                return "Error: Numbers cannot be more than four digits."
            else:
                if len(i[1].split()[0]) < len(i[1].split()[2]):
                    str += "  " + numspace*(len(i[1].split()[2]) - len(i[1].split()[0])) + i[1].split()[0] + "    "
                    opStr += i[1].split()[1] + " " + i[1].split()[2] + "    "
                    dash += "-"*(len(i[1].split()[2]) + 2) + "    "
                else:
                    str += "  " +  i[1].split()[0] + "    "
                    opStr += i[1].split()[1] + " " + numspace*(len(i[1].split()[0]) - len(i[1].split()[2])) + i[1].split()[2] + "    "
                    dash += "-"*(len(i[1].split()[0]) + 2) + "    "
            if i[1].split()[1] == "+":
                soln = int(i[1].split()[0]) + int(i[1].split()[2])
            elif i[1].split()[1] == "-":
                soln = int(i[1].split()[0]) - int(i[1].split()[2])
            ans += numspace*(len('{}'.format(max(int(i[1].split()[0]), int(i[1].split()[2])))) + 2 - len('{}'.format(soln))) + '{}'.format(soln) + "    "
    arranged_problems = str[:-4] + "\n" + opStr[:-4] + "\n" + dash[:-4]
    if B == True:
        arranged_problems = str[:-4] + "\n" + opStr[:-4] + "\n" + dash[:-4] + "\n" + ans[:-4]
    print(arranged_problems)
    return arranged_problems



# arithmetic_arranger(['3562 + 4', '5 - 4', '67 + 9'])
#--------------------------------------------------------
y = ['3562 + 4', '5 - 4', '67 + 9']
x = enumerate(y)
print(list(x))

