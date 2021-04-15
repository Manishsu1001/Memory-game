import random
import os
import time

#This will give me a box of required size
def createbox(n):
    line = ''
    for i in range(1+7*n):
        line += '-'
    line2 = ''
    for i in range(1+7*n):
        if i % 7 == 0:
            line2 += '|'
        else:
            line2 += ' '
    minature = [line]
    for i in range(n):
        minature.append(line2)
        minature.append(line2)
        minature.append(line)
    return minature

def game(n,times,blinktime):
    loaded = createbox(n)
    #The blinking period code follows:
    for itr in range(times):
        os.system('cls')
        x,y = random.randint(0,n-1),random.randint(0,n-1)
        change = loaded[1+3*x][:3+7*y]+'**'+loaded[1+3*x][5+7*y:]
        loaded[1+3*x],loaded[2+3*x] = change,change
        print('\n\n')
        for j in loaded:
            print('\t\t\t\t\t\t',j)
        change = loaded[1+3*x][:3+7*y]+'  '+loaded[1+3*x][5+7*y:]
        loaded[1+3*x],loaded[2+3*x] = change,change
        history.append((x+1,y+1))
        numhis.append(n*x+y+1)
        time.sleep(blinktime)
        os.system('cls')
        print('\n\n')
        for j in loaded:
            print('\t\t\t\t\t\t',j)
        time.sleep(blinktime*4/5)
    # The asking from user period code follows
    print('\n\n')
    for i in range(len(numhis)):
        trial = input('\t\t\t\t\t\t'+str(i+1)+': ')
        try:
            ip = trial.split()
            if (int(ip[0]),int(ip[1])) != history[i]:
                c = i
                break
        except:
            if int(trial) != numhis[i]:
                c = i
                break
    try:
        print('\n\n\t\t\t\t\t\tYou lost! you remebered only',c,'words')
    except:
        print('\n\n\t\t\t\t\t\tcongrats you won')

def main_menu():
    os.system('cls')
    ip = -10
    while(ip > 4 or ip < 1):
        print('\t\t\t\tEnter the number corresponding to options to select!\n\n\n\n\n\n\n')
        print('\t\t\t\t\t\t1. Quick Play')
        print('\t\t\t\t\t\t2. Play Level Wise')
        print('\t\t\t\t\t\t3. How to play?')
        print('\t\t\t\t\t\t4. Quit')
        try:
            ip = int(input('Enter here: '))
        except:
            print('**************************************************Enter a valid option**************************************************\n')
        os.system('cls')
        if ip >4 or ip< 1:
            print('**************************************************Enter a valid option**************************************************\n')
    os.system('cls')
    while ip == 1:
        print('\n\n\t\t\t\t\tYou will have to remeber 5 blinks positions')
        time.sleep(2)
        game(3,5,1)
        play_again()
    if ip == 2:
        ip = -10
        while(ip > 5 or ip < 1):
            print('\t\t\t\tEnter the number corresponding to options to select!\n\n\n\n\n\n\n')
            print('\t\t\t\t\t\t1. Very Easy')
            print('\t\t\t\t\t\t2. Easy')
            print('\t\t\t\t\t\t3. Medium')
            print('\t\t\t\t\t\t4. Hard')
            print('\t\t\t\t\t\t5. Very Hard')
            try:
                ip = int(input('Enter here: '))
            except:
                print('**************************************************Enter a valid option**************************************************\n')
            os.system('cls')
            if ip >5 or ip< 1:
                print('**************************************************Enter a valid option**************************************************\n')
        os.system('cls')
        while ip == 1:
            print('\n\n\t\t\t\tYou will have to remeber 5 blinks positions')
            time.sleep(4)
            game(3,5,1)
            play_again()
        while ip == 2:
            print('\t\t\t\tYou will have to remeber 5 blinks positions')
            time.sleep(4)
            game(5,5,1)
            play_again()
        while ip == 3:
            print('\t\t\t\tYou will have to remeber 10 blinks positions')
            time.sleep(4)
            game(5,10,1.2)
            play_again()
        while ip == 4:
            print('\t\t\t\tYou will have to remeber 10 blinks positions')
            time.sleep(4)
            game(8,10,1.2)
            play_again()
        while ip == 5:
            print('\t\t\t\tYou will have to remeber 15 blinks positions')
            time.sleep(4)
            game(10,15,1.2)
            play_again()
    if ip == 3:
        print('This is a memory game where you have to remeber the blinks and when asked, you have to type in which box the stars were blinked. Sounds interesting right? So GO AND PLAY')
        input('\n\n\t\t\t\tPress ENTER/RETURN key to go back to main Menu')
        main_menu()
    while ip == 4:
        check = input('\t\t\t\t\t\tAre you sure you want to leave\n\n\t\t\t\t\t\t\tYES/NO\n\t\t\t\t\t\t\tY/N\n\n\t\t\t\t\t\t\t')
        if check in ['y','Y','Yes','yes','YES']:
            print('Leaving...')
            time.sleep(1)
            quit()
        elif check in ['n','N','NO','no','No','nO']:
            print('\n\n\n\t\t\t\t\t\tGetting back to main menu!')
            time.sleep(1)
            main_menu()
        else:
            continue

def play_again():
    while True:
        check = input('\n\n\t\t\t\t\t\tDo you want to play again?\n\n\t\t\t\t\t\t\tYES/NO\n\t\t\t\t\t\t\tY/N\n\n\t\t\t\t\t\t')
        if check in ['y','Y','Yes','yes','YES']:
            os.system('cls')
            break
        elif check in ['n','N','NO','no','No','nO']:
            print('Getting back to main menu!')
            time.sleep(1)
            main_menu()
        else:
            continue
            os.system('cls')


if __name__ == '__main__':
    history = []
    numhis = []
    main_menu()
    