intro= "this is a code that will help you to know what your personality is\nit will also comment on your type of character"
print (intro)
into_prompt= input("would you like to use this code:\nyes/no\n")
Yes= "yes"
No="no"
if into_prompt== Yes:
    input('we shall begin!!!')
else:
    print("thank you!!! byee!!!")
    exit()
user_name= input("enter your name below please:\n")

main_info= (f"{user_name}, you will see a couple of questions down below\nanswer them sincerely and get your personality check\npick from numbers 1 to 3\nlets begin!!!")
print(main_info)
count_1= 0
count_2=0
count_3=0
question_1= "1. you regularly make new friends\n2. you hardly make new friends\n3. you make friends on a daily basis"
print(question_1)
option_1=1
option_2=2
option_3=3
answer_1=int(input("pick an option from 1 to 3\n"))
if answer_1==option_1:
    count_1+=1
    print("next question")
if answer_1==option_2:
    count_2+=1
    print("next question")
if answer_1==option_3:
    count_3+=1
    print("next question")

question_2= "1. complex ideas excite you\n2. simple ideas excite you\n3. both simple and complex ideas excite you"
print(question_2)
answer_2= int(input("pick an option from 1 to 3\n"))
if answer_2==option_1:
    count_1+=1
    print("next question")
if answer_2==option_2:
    count_2+=1
    print("next question")
if answer_2==option_3:
    count_3+=1
    print("next question")

question_3= "1. your living spaces are clean and organized\n2. your living spaces are messy but still clean\n3. your living spaces are rowdy and disarranged"
print(question_3)
answer_3= int(input("pick an option from 1 to 3\n"))
if answer_3==option_1:
    count_1+=1
    print("next question")
if answer_3==option_2:
    count_2+=1
    print("next question")
if answer_3==option_3:
    count_3+=1
    print("next question")

question_4= "1. you find the idea of networking or promoting yourself very easy\n2. you find the idea of networking or promoting yourself very hard\n3. you find the idea of networking or promoting yourself pretty okay but a bit tasking"
print(question_4)
answer_4= int(input("pick an option from 1 to 3\n"))
if answer_4==option_1:
    count_1+=1
    print("next question")
if answer_4==option_2:
    count_2+=1
    print("next question")
if answer_4==option_3:
    count_3+=1
    print("next question")

question_5= "1. peoples emotions speak louder to you than words\n2. peoples words speak louder to you than emotions\n3. you judge based on your mood "
print(question_5)
answer_5=int(input("pick an option from 1 to 3\n"))
if answer_5==option_1:
    count_1+=1
    print("next question")
if answer_5==option_2:
    count_2+=1
    print("next question")
if answer_5==option_3:
    count_3+=1
    print("next question")

question_6= "1. you prioritize  honesty over sensitivity\n2. you prioritize sensitivity over honesty \n3. you take both into account"
print(question_6)
answer_6= int(input("pick an option from 1 to 3\n"))
if answer_6==option_1:
    count_1+=1
    print("next question")
if answer_6==option_2:
    count_2+=1
    print("next question")
if answer_6==option_3:
    count_3+=1
    print("next question")

question_7= "1. you allow the day to unfold without any schedule at all\n2. you make sure you schedule your day and follow it\n3. you make a schedule but you dont follow it "
print(question_7)
answer_7= int(input("pick an option from 1 to 3\n"))
if answer_7==option_1:
    count_1+=1
    print("next question")
if answer_7==option_2:
    count_2+=1
    print("next question")
if answer_7==option_3:
    count_3+=1
    print("next question")
    
question_8= "1. you rarely worry about peoples opinions in your life\n2.you think about peoples opinions in your life\n3. your too worried thinking about your own life to care"
print(question_8)
answer_8=int(input("pick an option from 1 to 3\n"))
if answer_8==option_1:
    count_1+=1
    print("next question")
if answer_8==option_2:
    count_2+=1
    print("next question")
if answer_8==option_3:
    count_3+=1
    print("next question")

question_9="1. you like team based activities\n2. you dont like team based activites\n3. it depends on the team"
print(question_9)
answer_9=int(input("pick an option from 1 to 3\n"))
if answer_9==option_1:
    count_1+=1
    print("next question")
if answer_9==option_2:
    count_2+=1
    print("next question")
if answer_9==option_3:
    count_3+=1
    print("next question")

question_10="1. you do your chores before you relax\n2. you relax before you do your chores\n3. it all depends on your mood"
print(question_10)
answer_10=int(input("pick an option from 1 to 3\n"))
if answer_10==option_1:
    count_1+=1
    print("thank you coming this far!!!")
if answer_10==option_2:
    count_2+=1
    print("thank you coming this far!!!")
if answer_10==option_3:
    count_3+=1
    print("thank you coming this far!!!")

last_one= "now the code will take a guess about your personality based on the options you chose\nPS this is absolutely not accurate, im just a girl spreading false information :)"
print(last_one)
print({count_1})
print({count_2})
print({count_3})
if count_1 > count_2 and count_1>count_3:
    print(f"youre a nice person i guess\nkeep doing you  {user_name}!!!")
if count_2> count_1 and count_2>count_3:
    print(f"youre a very practical person\nyou hardly get dissapointed {user_name}")
if count_3>count_1 and count_3>count_2:
    print(f"youre genuienely just a chill guy, {user_name}\n(knock on wood<3)")
yurrr= "thank you for using this guessing game!!!\nrun the code again to play the guessing game again!!!"

