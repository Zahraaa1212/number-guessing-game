import random

def welcome():
    print("welcome to this funny game")
    print("I will guess a number between 1 and 20")
    print("you have to guess it ...")
    print("go go go")
    print()
    
def finish(number , count, best_record):   
    print("good game")  
    print(f"My number was {number} and you found it in {count} guesses")
    
    if best_record is None or count < best_record:
        print(f"you are the best player in this game! new record : {count} guesses")
        best_record = count
    else:
        print(f"the record is still {best_record} guesses. try again")
    
    answer = input("do you want to play again?(Y/N)")
    
    if answer.upper() =='Y':
        return True , best_record
    else:
        return False , best_record
    
def win (computer_number , guess):
    return computer_number == guess

def respond(computer , user):
    if computer > user:
        result = "My number is larger"
    elif computer < user :
        result = "Noooo ,mine is smaller"
    else:
        result="WOW!!!!! you won good guess"
        
    return result

def get_a_guess():
    while True:
        ans = int(input("what is your guess? :"))
        
        if 1 <= ans <=20:
            return ans
        else:
            print("please enter a number between 1 and 20")
    

welcome()
continue_playing= True
best_record =None
while(continue_playing):
    computer_number = random.randint(1, 20)
    
    guess =0
    
    count =0 
    
    while( not win(computer_number , guess) ):
        guess = get_a_guess()
        count +=1
        print(respond(computer_number , guess))
    
    continue_playing , best_record =finish(computer_number ,count, best_record)