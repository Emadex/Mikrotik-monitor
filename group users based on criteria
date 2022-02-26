S = 0
IP = None
firstIP = None
ra = None
previousIP = None
previousMAC = None
previousportr = None
previousVisited = None
previousdate = None



dlines = open("demofile2.csv", "r")
dhandle = dlines.readlines()
dlines.close()

for dline in dhandle:
    gline = dline.rstrip()
    firstpos = dline.find(",")
    secondpos = dline.find(",", firstpos+1)
    thirdpos = dline.find(",", secondpos+1)
    fourthpos = dline.find(",", thirdpos+1)
    fifthpos = dline.find(",", fourthpos+1)
    sixthpos = dline.find(",", fifthpos+1)
    seventhpos = dline.find(",", sixthpos+1)
    eighthpos = dline.find(",", seventhpos+1)
    endpos = dline.find(" ", eighthpos)
    IP = gline[fourthpos+1:fifthpos]
    if previousIP == IP:

        q = open('c:\Mabcowatch\ip\%s.txt' % IP, 'a')
        q.write(dline)
        q.write("\n")
        q.close()
        continue
    previousIP = IP

for dline in dhandle:
    gline = dline.rstrip()
    firstpos = dline.find(",")
    secondpos = dline.find(",", firstpos+1)
    thirdpos = dline.find(",", secondpos+1)
    fourthpos = dline.find(",", thirdpos+1)
    fifthpos = dline.find(",", fourthpos+1)
    sixthpos = dline.find(",", fifthpos+1)
    seventhpos = dline.find(",", sixthpos+1)
    eighthpos = dline.find(",", seventhpos+1)
    endpos = dline.find(" ", eighthpos)
    MAC = gline[firstpos+1:secondpos]
    if previousMAC == MAC:

        q = open('c:\Mabcowatch\mac\%s.txt' % MAC, 'a')
        q.write(dline)
        q.write("\n")
        q.close()
        continue
    previousMAC = MAC

for dline in dhandle:
    gline = dline.rstrip()
    firstpos = dline.find(",")
    secondpos = dline.find(",", firstpos+1)
    thirdpos = dline.find(",", secondpos+1)
    fourthpos = dline.find(",", thirdpos+1)
    fifthpos = dline.find(",", fourthpos+1)
    sixthpos = dline.find(",", fifthpos+1)
    seventhpos = dline.find(",", sixthpos+1)
    eighthpos = dline.find(",", seventhpos+1)
    endpos = dline.find(" ", eighthpos)
    Visited = gline[sixthpos+1:seventhpos]
    if previousVisited == previousVisited:

        q = open('c:\Mabcowatch\Visited\%s.txt' % Visited, 'a')
        q.write(dline)
        q.write("\n")
        q.close()
        continue
    previousVisited = previousVisited

for dline in dhandle:
    gline = dline.rstrip()
    firstpos = dline.find(",")
    secondpos = dline.find(",", firstpos+1)
    thirdpos = dline.find(",", secondpos+1)
    fourthpos = dline.find(",", thirdpos+1)
    fifthpos = dline.find(",", fourthpos+1)
    sixthpos = dline.find(",", fifthpos+1)
    seventhpos = dline.find(",", sixthpos+1)
    eighthpos = dline.find(",", seventhpos+1)
    endpos = dline.find(" ", eighthpos)
    portr = gline[seventhpos+1:eighthpos]
    if previousportr == portr :
        q = open('C:\Mabcowatch\Portr\%s.txt' %portr, 'a')
        q.write(dline)
        q.write("\n")
        q.close()
        continue
    previousportr = portr

for dline in dhandle:
    gline = dline.rstrip()
    firstpos = dline.find(",")
    secondpos = dline.find(",", firstpos+1)
    thirdpos = dline.find(",", secondpos+1)
    fourthpos = dline.find(",", thirdpos+1)
    fifthpos = dline.find(",", fourthpos+1)
    sixthpos = dline.find(",", fifthpos+1)
    seventhpos = dline.find(",", sixthpos+1)
    eighthpos = dline.find(",", seventhpos+1)
    ninthpos = dline.find(" ", eighthpos+1)
    endpos = dline.find(" ", ninthpos+1)
    date = gline[eighthpos+1:endpos]
    if previousdate == date :
        q = open('C:\Mabcowatch\date\%s.txt' %date, 'a')
        q.write(dline)
        q.write("\n")
        q.close()
        continue
    previousdate = date
