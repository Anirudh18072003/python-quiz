question1="ROUND 1:-\nQUESTION 1:The atomic number of lithium is 17\n(a)True\n(b)False"
question2="\nRound 2:-\nQuestion 2:Pinocchio was Walt Disney's first animated film in full colour.\n(a)True\n(b)False\n"
question3="\nRound 3:-\nQuestion 3:The national sports of India is Hockey.\n(a)True\n(b)False\n"
question4="\nRound 4:-\nQuestion 4:Nepal is the only country in the world without the flag.\n(a)True\n(b)False\n"
question5="\nRound 5:-\nQuestion 5:The world's largest island is Greenland.\n(a)True\n(b)False\n"
dict={question1:"b",question2:"b",question3:"a",question4:"a",question5:"a"}
score=0
for i in dict:
    print(i)
    ans=input("Enter your answer here:")
    if ans==dict[i]:
        print("Your answer is Correct. Congratulations!!!")
        score=score+1
    else:
        print("Your answer is Incorrect")
print("Total score obtained: ",score+"/5")







