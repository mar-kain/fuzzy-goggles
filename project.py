#%%
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 13:47:10 2020

@author: maria
"""

members = {'Jeon So Min': {'firstEp': '360',
  'joinYear': '2018',
  'lastEp': '-',
  'nicknames': [],
  'occupation': 'Actress'},
 'Song Ji Hyo': {'firstEp': '1',
  'joinYear': '2010',
  'lastEp': '-',
  'nicknames': ['Mong Ji Hyo', 'Ace'],
  'occupation': 'Actress'},
 'Yoo Jae Seok': {'firstEp': '1',
  'joinYear': '2010',
  'lastEp': '-',
  'nicknames': ['Grasshopper'],
  'occupation': 'Comedian'}}
 # use members.update(newMemb()) to add member etc. https://realpython.com/python-dicts/
 
#%%
#--------------Misc. Functions--------------------------#
def check(list1, element):
    if type(list1) == dict:
        list2 = [x.lower() for x in list(list1.keys())]
        if element.lower() in list2:
            return 1
        else:
            return 0
    else:
        list2 = [x.lower() for x in list1]
        if element.lower() in list2:
            return 1
        else:
            return 0
    
def pause():
    programPause = input("Press <ENTER> to continue...")
    
def changeCase(string1):
    string2 = string1[0].upper()
    for i in range(1, len(string1)):
        if string1[i-1] == ' ':
            string2 += string1[i].upper()
        else:
            string2 += string1[i].lower()
    return string2


#%%
#--------------Ep Functions--------------------------#
def newEp(mainCast): #input dictionary of main cast
    episode = {}
    episode['number'] = input('Enter episode number: ')
    episode['year'] = input('Enter the year the episode was aired: ')
    episode['main_cast'] = []
    for i in range(0, len(mainCast)):
        if int(mainCast[str(i+1)]['firstEp']) <= int(episode['number']):
            while True:
                q = 'Is ' + mainCast[str(i+1)]['name'] + ' in the episode? y/n: '
                inEp = input(q)
                if inEp.lower() =='y':
                    episode['main_cast'].append(mainCast[str(i+1)]['name'])
                    break
                elif inEp.lower() == 'n':
                    break
                else:
                    print('---------------')
                    print('Unknown input:', inEp, '.')
                    print('Acceptable inputs are "y", "Y", "n" and "N".')
                    continue
        else:
            continue
    return episode
    

def viewEp():
    print('Viewing...')

def editEp():
    print('Editing...')

def deleteEp():
    print('Deleting...')


def chooseActEp():
    acceptInp = ['n', 'v', 'e', 'd', 'q']
    print('EPISODE MENU')
    print('  n -- Add an episode.')
    print('  v -- View data of an episode.')
    print('  e -- Edit the data of an episode.')
    print('  d -- Delete an episode.')
    print('  q -- Go back to main menu.')
    choice = input('Choose one of the above: ')
    choice = choice.lower()
    if choice in acceptInp:
        return choice
    else:
        print('What is', choice,'?')
        print('Not acceptable input.')
        print('Learn how to read you moron.')
        return None


def epLoop():
    while True:
        choice = chooseActEp()
        if choice == 'n':
            newEp()
        elif choice == 'v':
            viewEp()
        elif choice == 'e':
            editEp()
        elif choice == 'd':
            deleteEp()
        elif choice == 'q':
            print('Going back to main menu.')
            print()
            break
        else:
            print('...Bye...')
            continue

#%%
#--------------Cast Functions--------------------------#

# Add a member to the list
def addMembDet(name): # OK--------
    member = {}
    member[name] = {}
    member[name]['occupation'] = input('Other Job: ')
    member[name]['joinYear'] = input('Joined in: ')
    member[name]['firstEp'] = input('First episode: ')
    member[name]['lastEp'] = input('Last episode: ')
    member[name]['nicknames'] = []
    flag1 = True # Checks if you want to add a nickname. The loop ensures that with any input other than the allowed the program reasks the question.
    while flag1 == True:
        q = 'Does '+ name + ' have nicknames? y/n: '
        flag2 = input(q)
        if flag2.lower() == 'y':
            i = 1
            flag3 = True
            while flag3 == True: # Input the nicknames and ask if there are other.
                out_ = 'Type nickname #' + str(i) + ': '
                nickN = input(out_)
                member[name]['nicknames'].append(nickN)
                print('Added nickname "', nickN, '" for ', name, '.')
                while True:
                    addAnother = input('Is there another nickname? y/n: ')
                    if addAnother.lower() == 'n':# No other nicknames
                        flag3 = False # Exit the adding nickname loop.
                        flag1 = False # Exit the main nickname loop.
                        break # Exit the additional nickname loop.
                    elif addAnother.lower() == 'y':
                        i = i+1 # Increase nickname counter by 1.
                        break # Go back to asking for the i+1 nickname.
                    else:
                        print('Did not recognize input.')
                        continue # Reask the question for additional nicknames.
        elif flag2.lower() == 'n':
            break # No nicknames. Exit the main nickname loop.
        else:
            print('Did not recognize answer.')
            continue # Reask if there are nicknames.
        print()
        print('Going back to member menu.')
    return member
    
def newMemb(members): # OK--------
    name = input('Name: ')
    alExists = check(members, name) # Check if input name already logged
    name = changeCase(name)
    if alExists == 1:
        print(name, 'is already in the database.')
        flag1 = input('Do you want to add them a second time? y/n: ')
        while True:
            if flag1.lower() == 'y':
                member = addMembDet(name)
                return member
            elif flag1.lower() == 'n':
                print('Going back to member menu.')
                break
            else:
                print('Did not recognize input.')
                continue # Reask the question.
    else:
        member = addMembDet(name)
        return member

# Choose member menu
def choose(list_): # Prints a list and asks you to pick one of the elements.
    print('----------------------------------')
    print('List of current and former members')
    i = 1 # counter
    for element_ in list_:
        temp = '  ' + str(i) + ' -- ' + element_ # List all the members.
        print(temp)
        i = i+1
    print('----------------------------------')
    while True:
        choice = input('Type the name to view details: ')
        flag1 = check(members, choice)
        choice = changeCase(choice)
        if flag1 == 1: # Check if the input is a name from the list
            return(choice)
        else:
            print('-------------')
            print('Unknown input', choice) # User input no in the list. Ask again for input.
            print('Select a name from the list.')
            continue
    
            
# Print a chosen member's details
def printMembDet(members, choice): # Dictionary input
    out_ = "{0:>28}  {1:<25}"
    print('------------------------------------------------------')
    print(out_.format('Name:', choice))
    print(out_.format('Occupation:',members[choice]['occupation']))
    print(out_.format('Joined in Year:', members[choice]['joinYear']))
    print(out_.format('First appeared in episode:', members[choice]['firstEp']))
    print(out_.format('Last appeared in episode:', members[choice]['lastEp']))
    if len(members[choice]['nicknames']) != 0:
        print(out_.format('Nicknames:', members[choice]['nicknames'][0])) # 1st nickname
        for i in range(1, len(members[choice]['nicknames'])):
            print(out_.format(' ', members[choice]['nicknames'][i])) # The rest of the nicknames
    else:
        print(out_.format('Nicknames:', '-')) # No nicknames.
    print('------------------------------------------------------')
    
# View a member from the list
def viewMemb(members):
    choice = choose(members)
    printMembDet(members,choice)
    

# Delete a member form the list
def delMemb(members): # OK--------
    choice = choose(members)
    print()
    print('Details of the member you want to delete')
    print()
    printMembDet(members, choice)
    choice = changeCase(choice)
    quest_ = 'Are you sure you want to permenantly delete ' + choice + '? Y/N: '
    while True:
        flag1 = input(quest_)
        if flag1.lower() == 'y':
            del members[choice]
            delMes =  choice + ' no longer in the members list.' # Message that informs who you deleted.
            print(delMes)
            print('Going back to member menu.')
            break
        elif flag1.lower() == 'n':
            print(choice, 'NOT deleted.')
            break
        else:
            print('-------------')
            print('Unknown input', choice)
            print('Select a name from the list.')
            continue

# Edit a member's information
def editMemb(members):
    choice = choose(members)
    while True:
        print()
        print('Details of the member you want to edit')
        printMembDet(members, choice)
        print()
        print('Do you want to edit:')
        print('  1 -- the name,')
        print('  2 -- the occupation,')
        print('  3 -- the year they joined the show,')
        print('  4 -- the first episode they appeared in,')
        print('  5 -- the last episode they appeared in,')
        print('  6 -- one or more of the nicknames')
        editAction = input('Choose the corresponing number. ')
#--------------------#
        if editAction == '1':
            state_ = 'Change name ' + choice + ' to: '
            newName = input(state_)
            newName = changeCase(newName)
            members[newName] = members[choice]
            del members[choice]
            choice = newName
            editAgain = 'Do you want to keep editing ' + choice +'? Y/N: '
            flag2 = input(editAgain)
            if flag2.lower() == 'y':
                continue
            elif flag2.lower() == 'n':
                break
            else:
                print('Did not recognize input. Returning...')
                break
#--------------------#
        elif editAction == '2':
            state_ = 'Change ' + choice + "'s occupation from " + members[choice]['occupation'] + ' to: '
            newOcc = input(state_)
            members[choice]['occupation'] = newOcc
            editAgain = 'Do you want to keep editing ' + choice +'? Y/N: '
            flag2 = input(editAgain)
            if flag2.lower() == 'y':
                continue
            elif flag2.lower() == 'n':
                break
            else:
                print('Did not recognize input. Returning...')
                break
#--------------------#
        elif editAction == '3':
            state_ = choice + ' joined in year: '
            year = input(state_)
            members[choice]['joinYear'] = year
            editAgain = 'Do you want to keep editing ' + choice +'? Y/N: '
            flag2 = input(editAgain)
            if flag2.lower() == 'y':
                continue
            elif flag2.lower() == 'n':
                break
            else:
                print('Did not recognize input. Returning...')
                break
#--------------------#
        elif editAction == '4':
            state_ = choice + ' first appeared in episode: '
            ep = input(state_)
            members[choice]['firstEp'] = ep
            editAgain = 'Do you want to keep editing ' + choice +'? Y/N: '
            flag2 = input(editAgain)
            if flag2.lower() == 'y':
                continue
            elif flag2.lower() == 'n':
                break
            else:
                print('Did not recognize input. Returning...')
                break
#--------------------#
        elif editAction == '5':
            state_ = choice + ' appeared last in episode: '
            ep = input(state_)
            members[choice]['lastEp'] = ep
            editAgain = 'Do you want to keep editing ' + choice +'? Y/N: '
            flag2 = input(editAgain)
            if flag2.lower() == 'y':
                continue
            elif flag2.lower() == 'n':
                break
            else:
                print('Did not recognize input. Returning...')
                break
#--------------------#
        elif editAction == '6':
            print('For', choice, 'do you want to:')
            print('  1 -- Add a nickname')
            print('  2 -- Edit a nickname')
            print('  3 -- Delete a nickname')
            nickAct = input('Choose the corresponding number: ')
            if nickAct == '1':
                nickN = input('Type the new nickname: ')
                members[choice]['nicknames'].append(nickN)
                editAgain = 'Do you want to keep editing ' + choice +'? Y/N: '
                if flag2.lower() == 'y':
                    continue
                elif flag2.lower() == 'n':
                    break
                else:
                    print('Did not recognize input. Returning...')
                    break     
            elif nickAct == '2':
                if len(members[choice]['nicknames']) != 0:
                    oldN = input('Which nickname do you want to edit? ')
                    flag1 = check(members[choice]['nicknames'], oldN)
                    if flag1 == 1:
                        state_ = 'Change nickname "' + oldN + '" to: '
                        newN = input(state_)
                        members[choice]['nicknames'].remove(oldN)
                        members[choice]['nicknames'].append(newN)
                    else:
                        print(choice, 'does not have', oldN, 'in nickname list.')
                        editAgain = 'Do you want to keep editing ' + choice +'? Y/N: '
                        flag2 = input(editAgain)
                        if flag2.lower() == 'y':
                            continue
                        elif flag2.lower() == 'n':
                            break
                        else:
                            print('Did not recognize input. Returning...')
                            break
                else:
                    state_ = choice + "'s data do not include any nicknames yet."
                    print(state_)
                    editAgain = 'Do you want to keep editing ' + choice +'? Y/N: '
                    flag2 = input(editAgain)
                    if flag2.lower() == 'y':
                        continue
                    elif flag2.lower() == 'n':
                        break
                    else:
                        print('Did not recognize input. Returning...')
                        break
            elif nickAct == '3':
                if len(members[choice]['nicknames']) != 0:
                    state_ = 'Which nickname you want to delete for ' + choice + '? '
                    delN = input(state_)
                    members[choice]['nicknames'].remove(delN)
                    editAgain = 'Do you want to keep editing ' + choice +'? Y/N: '
                    flag2 = input(editAgain)
                    if flag2.lower() == 'y':
                        continue
                    elif flag2.lower() == 'n':
                        break
                    else:
                        print('Did not recognize input. Returning...')
                        break
                else:
                    state_ = choice + "'s data do not include any nicknames yet."
                    print(state_)
                    editAgain = 'Do you want to keep editing ' + choice +'? Y/N: '
                    flag2 = input(editAgain)
                    if flag2.lower() == 'y':
                        continue
                    elif flag2.lower() == 'n':
                        break
                    else:
                        print('Did not recognize input. Returning...')
                        break
            else:
                print('Did not recognize input. Choose again what you want to edit.')
                continue
        else:
            print('Did not recognize input.')
            continue

def chooseActMemb():
    acceptInp = ['n', 'v', 'e', 'd', 'q']
    print()
    print('MEMBER MENU')
    print()
    print('  n -- Add a new member.')
    print('  v -- View member dets.')
    print('  e -- Edit member dets.')
    print('  d -- Delete a member.')
    print('  q -- Go back to main menu.')
    choice = input('Choose one of the above: ')
    choice = choice.lower()
    if choice in acceptInp:
        return choice
    else:
        print('What is', choice,'?')
        print('Not acceptable input.')
        print('Learn how to read you moron.')
        return None

def castLoop():
    while True:
        choice = chooseActMemb()
        if choice == 'n':
            mem = newMemb(members)
            if mem != None:
                members.update(mem)
            print(mem) # Just for checking, must go when finished.
        elif choice == 'v':
            viewMemb(members)
            pause()
        elif choice == 'e':
            editMemb(members)
        elif choice == 'd':
            delMemb(members)
        elif choice == 'q':
            print('Going back to main menu.')
            print()
            break
        else:
            print('...Bye...')
            continue



#%%
#--------------Guest Functions--------------------------#
def newGuest():
    print('Adding guest')
    
def viewGuest():
    print('Viewing guest data')
    
def editGuest():
    print('Editing guest data')
    
def delGuest():
    print('Deleting guest')


def chooseActGuest():
    acceptInp = ['n', 'v', 'e', 'd', 'f', 'q']
    print('GUEST MENU')
    print('  n -- Add new guest.')
    print('  v -- View guest dets.')
    print('  e -- Edit guest dets.')
    print('  d -- Delete a guest.')
    print('  q -- Go back to main menu.')
    choice = input('Choose one of the above: ')
    choice = choice.lower()
    if choice in acceptInp:
        return choice
    else:
        print('What is', choice,'?')
        print('Not acceptable input.')
        print('Learn how to read you moron.')
        return None

def guestLoop():
    while True:
        choice = chooseActGuest()
        if choice == 'n':
            newGuest()
        elif choice == 'v':
            viewGuest()
        elif choice == 'e':
            editGuest()
        elif choice == 'd':
            delGuest()
        elif choice == 'q':
            print('Going back to main menu.')
            print()
            break
        else:
            print('...Bye...')
            continue

#%%
#-------------Main Loop---------------------------------#

def mainChoice():
    acceptInp = ['e', 'm', 'g', 'q']
    print('MAIN MENU')
    print('  e -- Enter episode menu.')
    print('  m -- Enter member menu.')
    print('  g -- Enter guest menu.')
    print('  q -- Quit.')
    choice = input('Choose one of the above: ')
    choice = choice.lower()
    if choice in acceptInp:
        return choice
    else:
        print('What is', choice,'?')
        print('Not acceptable input.')
        print('Learn how to read you moron.')
        return None

def mainLoop():
    while True:
        choice = mainChoice()
        if choice == 'e':
            epLoop()
        elif choice == 'm':
            castLoop()
        elif choice == 'g':
            guestLoop()
        elif choice == 'q':
            print('Quiting...')
            break
        else:
            print('...Bye...')
            continue
#%%
import csv
if __name__ == '__main__':
    mainLoop()