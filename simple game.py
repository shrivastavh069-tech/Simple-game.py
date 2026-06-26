
def computer_choise():
    import random
    gond=random.choice(["scissor","stone","paper"])
    return gond 
    

def winning():
    if(user == "stone" and bot=="stone"):
        return("==DRAW==")
    elif(user =="paper" and bot =="paper"):
        return("==DRAW==")
    elif(user == "scissor" and bot=="scissor"):
        return("==DRAW==")
    elif(user == "paper" and bot == "stone"):
        return("==USER WINS==")
    elif(bot == "paper" and user == "stone"):
        return("==BOT WINS==")
    elif(user == "paper" and bot =="scissor"):
        return("==BOT WINS==")
    elif(bot == "scissor" and user == "paper"):
        return("==BOT WINS==")
    elif(user =="stone" and bot=="scissor"):
        return("==USER WINS==")
    elif(bot =="stone" and user=="scissor"):
        return("==BOT WINS==")
    elif(user =="scissor" and bot =="paper"):
        return("==USER WINS==") 
    elif(user== "❌ Invalid Syntax"):
        return("==BOT WINS==")
    
        
        
while True:
    start=int(input("""🤖:-WANT TO START[Type 1]:-"""))
    if(start == 1):
        comp_po=0
        user_po=0
        print("==========[🥸LEVEL,EASY🥸]==========")
        for i in range (1,4,1):
            user=input("I choose:")
            print("🤖 Choose:-\a")
            bot=computer_choise()
            print(bot)
            chunk=winning()
            print(chunk)
            if(chunk == "==USER WINS=="):
                user_po+=1
            elif(chunk == "==BOT WINS=="):
                comp_po+=1
        print("📊SCORE BOARD📊")
        print("USER POINTS-->",user_po)
        print("BOT POINTS-->",comp_po)
        if(comp_po == user_po):
            print("🤖:-Nobody Wins!!\nbut see you on next match")
        elif(comp_po<user_po):
            print("🤖:- I will see you on the next match!!\a")
        else:
            print("🤖:- aah!! I won !!\n!!retry!!\a")
            

        