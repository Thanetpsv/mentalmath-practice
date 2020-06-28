print("This program will generate two integers given a range")
print("It will then perform operation given the operator")
print("Please specify the range and operator as instructed")

import random


# In[6]:


while True:
    try:
        lim1 = float(input("input first lowest number: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break
        
while True:
    try:
        lim2 = float(input("input first largest number: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    except lim2<lim1:
        print("Sorry, the value must be higher than the previous one")
        continue
    else:
        break

while True:
    try:
        lim3 = float(input("input second lowest number: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break
        
while True:
    try:
        lim4 = float(input("input second largest number: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break


# In[7]:


ope = input("input operator + or - or * or /:   ")
while True:
    if ope == "+":
        print("Addition selected")
        break
    elif ope == "-":
        print("Subtraction selected")
        break
    elif ope == "*":
        print("Multiplication selected")
        break
    elif ope == "/":
        print("Division selected")
        break
    else:
        print("Please enter a valid operator")
        ope = input("input operator + or - or * or /:   ")


# In[8]:


loop = "y"
op_count = 0
score_count = 0
while loop != "n":
    v1 = random.randint(lim1, lim2)
    v2 = random.randint(lim3, lim4)
    if ope == "+":
        r = v1 + v2
    if ope == "-":
        r = v1 - v2
    if ope == "*":
        r = v1 * v2
    if ope == "/":
        r = v1/v2
    print("{} {} {}".format(v1, ope, v2))
    loop = input("enter answer or enter 'n' to exit:       ")
    op_count += 1
    if loop == str(r):
        score_count += 1
        print("Correct!")
    elif loop == "n":
        op_count = op_count -1
    else:
        print('Incorrect! the answer is: {}'.format(r))
    print("********************{}********************".format(op_count))
percent_score = score_count/op_count
percent_round = "%.2f" % percent_score
percent_times100 = float(percent_round)*100
print("Your score: {} of {} or {}% correct".format(score_count, op_count,
                                                   percent_times100))
print(input("enter anything to exit program"))

