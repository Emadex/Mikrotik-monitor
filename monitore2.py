import os
import socket
linecount = None
def resetcounter():
    number = open ("config.txt")
    for line in number:
        fline = line.rstrip()
        conepos = fline.find(" ") +999999
        linecount = int(fline[0:conepos])
        if linecount < 0 :
            c = open("config.txt", "w")
            c.write("0")
            c.close()
def writedatatofile():
    f.write(str(linecount))
    f.write(",")
    f.write(MAC)
    f.write(",")
    f.write(Ininterface)
    f.write(",")
    f.write(Outinterface)
    f.write(",")
    f.write(Inip)
    f.write(",")
    f.write(Ipport)
    f.write(",")
    f.write(Outip)
    f.write(",")
    f.write(Outport)
    f.write(",")
    f.write(date)
    f.write("\n")
def linecountid():
    #save last linecount
    c = open("config.txt", "w")
    c.write(str(linecount))
    c.close()

resetcounter()
lines = open("tmplog.log", "r")
handle = lines.readlines()
lines.close()
#delete old log data (close syslog daemon, delete log old log file, start syslog daemon again)
os.system('cmd /c "taskkill /FI "WINDOWTITLE eq MikroTik*" /f"')
os.system('cmd /c "del /f tmplog.log"')
os.system('cmd /c "start MT_Syslog.exe"')
#os.system('cmd /c "del /f tmplog.log"')
#read previous linecount value
number = open ("config.txt")
for line in number:
    fline = line.rstrip()
    conepos = fline.find(" ") +999999
    linecount = int(fline[0:conepos])
for line in handle:
    fline = line.rstrip()
    #assigning line numbers
    linecount = linecount + 1
    #Finding MAC ADDRESS
    MACspos = fline.find("src-mac") +8
    MACepos = fline.find(",",MACspos)
    MAC = fline[MACspos:MACepos]
    #in interface
    Inspos = fline.find("in:") + 3
    Inepos = fline.find(" o",Inspos)
    Ininterface = fline[Inspos:Inepos]
    #out outinterface
    Outspos = fline.find("out:") + 4
    Outepos = fline.find(",",Outspos)
    Outinterface = fline[Outspos:Outepos]
    #finding pc ip
    Ipspos = fline.find("), ") +3
    Ipepos = fline.find(":",Ipspos)
    Inip = fline[Ipspos:Ipepos]
    #finding ip port
    Portepos = fline.find("-",Ipepos)
    Ipport = fline[Ipepos+1:Portepos]
    #finding requested Ip
    Outipspos = fline.find(">",Portepos)+1
    Outipepos = fline.find(":",Outipspos)
    Outip = fline[Outipspos:Outipepos]
    #finding the host name of Outip addresses
    #    try:
    #        domainn = socket.gethostbyaddr(Outip)
    #    except socket.error: # for hosts that don't exist
    #      pass
    #finding reqested port
    Outportepos = fline.find(",",Outipepos)
    Outport = fline[Outipepos+1:Outportepos]
    #finding date
    datespos = fline.find('in',Outportepos)
    dateepos = fline.find(" f",datespos)
    date=fline[datespos:dateepos]
    f = open("demofile2.csv", "a")
    writedatatofile()
    f.close()
    #print(linecount," ",MAC," ",Ininterface," ",Outinterface," ",Inip," ",Ipport," ",Outip," ",Outport," ",date," ")





linecountid()


