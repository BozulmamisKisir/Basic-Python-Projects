import random
wins=0
strike=0
result =0
while 1:
    answer = random.randint(1,3)
    answertext=""
    if answer ==1:answertext="Taş"
    elif answer == 2: answertext= "Kağıt" 
    else: answertext = "Makas"
    user_answer = int(input("Cevap Giriniz (Taş : 1, Kağıt : 2, Makas : 3)"))
    sonuc=""
    
    if answer == user_answer: sonuc = "Berabere";result=2
    elif answer ==1 and user_answer ==2: sonuc = "Kazandın";result=1
    elif answer ==2 and user_answer ==3: sonuc = "Kazandın";result=1
    elif answer ==3 and user_answer ==1: sonuc = "Kazandın";result=1
    elif answer ==2 and user_answer ==1: sonuc = "Kaybettin";result=0
    elif answer ==3 and user_answer ==2: sonuc = "Kaybettin";result=0
    elif answer ==1 and user_answer ==3: sonuc = "Kaybettin";result=0
    if result ==1:wins=wins+1;strike=strike+1
    else: strike=0
    if user_answer <=3 and user_answer>0:print("Cevap\t:",answertext,"\nSonuç\t:",sonuc ,"\nWins\t:",wins,"\nStrike\t:",strike)
    else:print("Yalnış cevap türü");pass
