import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017/')
#connected to mongodb

db = client['Project0']
collection = db['top_scores']
# connected to db and created collection of users

#menu
def menu():
    print('[1] Play game')
    print('[2] View player high scores')
    print('[3] Update player initials')
    print('[4] Delete a player')
    print('[0] Exit game.')

option = 5
while option != 0:
    #display menu options
    menu()
    option = int(input('Enter the number of your choice: '))
    #begin game if they chose option 1
    if option == 1:
        print("hi! welcome to my little game!")
        print('this game will consist of questions about world history')
        playing = input('soo... would you like to play? enter yes or no ')
        if playing.lower() != 'yes':
            break
        else:
            print('awesome! let the game begin!! :D')
            score = 0
            answer = input('what animal did the ancient Egyptians consider gods? ')
            if answer.lower() == 'cat':
                print('correct!')
                score += 1
            else:
                print('Sorry incorrect.')
            answer = input('Which was the weapon of choice for Samurais? ')
            if answer.lower() == 'katana':
                print('correct! woohoo')
                score += 1
            else:
                print('incorrect! better luck next time')
            answer = input('Who was the first US President to resign from office? ')
            if answer.lower() == 'richard nixon':
                print('correct! good job!')
                score += 1
            else:
                print('incorrect! better luck next time')
            answer = input('ln Greek mythology which goddess represents love? ')
            if answer.lower() == 'aphrodite':
                print('correct! <3')
                score += 1
            else:
                print('incorrect! better luck next time')
            answer = input('Who was the first king of Rome, according to the Roman tradition? ')
            if answer.lower() == 'romulus':
                print('correct! that was a great game')
                score += 1
            else:
                print('incorrect! no worries you played an awesome game')
                #print their score, created string out of score so that i can combine all strings to make a valid operation
            print("congrats! you got " + str(score) + ' questions correct!')
            print('in total you got ' + str((score/5)*100) + '%.')
            #create
            print("that's the game")
#assigning variables
            hs = score
            i = input("Please enter your 3 initials")
            # created dict with key value pairs
            mydict = {"initials": i, "high_score": hs}
            db.top_scores.insert_one(mydict)
            g = input('Would you like to play again? Yes or no? ')
            if g == 'no':
                break
            else:
                continue

    elif option == 2:
        #read, finds the top scores as well as initials
        print('Here is a list of all the top scores.')
        # lists top scores in descending order and limited and top score of 5
        variable_name = db.top_scores.aggregate([{'$project': {'_id': 0}}, {'$sort': {'high_score': -1}}, {'$limit': 5}])
        for x in variable_name:
            print(x)
        continue
    elif option == 3:
        # updates the initials
        optx = str(input('Enter the exact initials you would like to update: '))
        myq = {'initials': optx}
        opty = str(input('Thanks. Please enter new initials: '))
        newinit = {'$set': {'initials': opty}}
        db.top_scores.update_one(myq, newinit)
        print('New initial has been entered.')
        #finds and displays new initials
        o = db.top_scores.find({'initials': opty})
        for x in o:
            print(x)
        continue
    elif option == 4:
        #delete initials
        print("Let's delete a players initials.")
        opt4 = str(input('Enter the player initials you would like to delete: '))
        myquery = {'initials': opt4}
        db.top_scores.delete_one(myquery)
        print('Player initials have been deleted.')
        continue
    else:
        print('Exiting game...')


print('Thanks for stopping by! See ya later!')
