import random
wins=0
strike=0
result =0
while 1:
    answer = random.randint(1,3)
    answertext=""
    if answer ==1:answertext="Rock"
    elif answer == 2: answertext= "Paper" 
    else: answertext = "Scissors"
    user_answer = int(input("Input an answer (Rock : 1, Paper : 2, Scissors : 3)"))
    sonuc=""
    
    if answer == user_answer: sonuc = "Draw";result=2
    elif answer ==1 and user_answer ==2: sonuc = "Win";result=1
    elif answer ==2 and user_answer ==3: sonuc = "Win";result=1
    elif answer ==3 and user_answer ==1: sonuc = "Win";result=1
    elif answer ==2 and user_answer ==1: sonuc = "Lose";result=0
    elif answer ==3 and user_answer ==2: sonuc = "Lose";result=0
    elif answer ==1 and user_answer ==3: sonuc = "Lose";result=0
    if result ==1:wins=wins+1;strike=strike+1
    else: strike=0
    if user_answer <=3 and user_answer>0:print("Answer\t:",answertext,"\nResult\t:",sonuc ,"\nWins\t:",wins,"\nStrike\t:",strike)
    else:print("Wrong Answer Type");pass
