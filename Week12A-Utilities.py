#INSERT GITHUB REPO LINK HERE
#Chase Shope
#CSCI 102 Section E
#Week 12A Utility


def printOutput(string):
    return('OUTPUT ' + string)

def loadFile(string):
    list_ = []
    f = open(f, 'r')
    for line in f:
        words = line.split()
        for word in words:
            list_.append(word)
    f.close()
    return(list_)

def updateString(str1,str2,num):
    str3 = ""
    for i in range (len(str1)):
        if i == num:
            str3 = str3 + str2
        else:
            str3 = str3 + str1[i]
    print(str3)

def findWordCount(List, String):
    count = 0
    for i in (len(List)):
        if List[i] == String:
            count += 1
    return (count)

def scoreFinder(names, scores, name):
    for i in (len(names)):
        if name = names[i]:
            print(names[i], ' got a score of ', scores[i])
        else:
            print('Player not found')

def union(players1, players2):
    players3 = []
    for i in range(len(players1)):
        for j in range(len(players2)):
            if players1[i] != players2[j]:
                players3.append(players1[i])
                players3.append(players2[j])
    return (players3)

def intersection(players1, players2):
    players3 = []
    for i in range(len(players1)):
        for j in range(len(players2)):
            if players1[i] == players2[j]:
                players3.append(players1[i])
                players3.append(players2[j])
    return (players3)

def notIn(list1,list2):
    list3 = []
    for i in range (len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                list3.append(list1[i])


