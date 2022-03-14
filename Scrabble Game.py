def scrabble_game():
    # make list to store numbers
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # make two variables to store sum of 2 players 
    player1 = 0
    player2 = 0

    # print instructions to the user
    print ("instructons : choose number between 1 and 9")

    # make while loop to take input from users to 3 times
    i = 0
    while i < 3 :
        num1 = int(input("first player enter number :"))
        if num1 not in list1 :
            num1 = int(input("first player enter number again :"))
            if num1 in list1:
                    list1.remove(num1)
                    print (list1) 
                    player1 += num1
        else :
            list1.remove(num1)
            print ("player two should choose from that list",list1) 
            player1 += num1
        
        
        num2 = int(input("second player enter number :"))
        if num2 not in list1 :
            num2 = int(input("second player enter number again :"))
            if num2 in list1:
                list1.remove(num2)
                print (list1) 
                player2 += num2
        else :
            list1.remove(num2)
            print ("player one should choose from that list",list1)  
            player2 += num2
        
        i += 1       
    
    
    # check if one player won or draw between them 
    if player1 == 15 :
        print ("player one win ")
    elif player2 == 15 :
        print ("player two win")        
    else :
        print ("Draw")  
       
# make application window to user        
def main():
    print ("Welcome In Number Scrabble Game") 
    scrabble_game()
    
# calling the main fanction to run the program    
main()             