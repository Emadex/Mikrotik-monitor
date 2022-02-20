import socket
linecount = 0
handle = open("s.log")
for line in handle:
    fline = line.rstrip()
#assigning line numbers
    linecount = linecount +1
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
    try:
        domainn = socket.gethostbyaddr(Outip)
    except socket.error: # for hosts that don't exist
      pass
#finding reqested port
    Outportepos = fline.find(",",Outipepos)
    Outport = fline[Outipepos+1:Outportepos]
#finding date
    datespos = fline.find('in',Outportepos)
    dateepos = fline.find(" f",datespos)
    date=fline[datespos:dateepos]
#    print(linecount," ",MAC," ",Ininterface," ",Outinterface," ",Inip," ",Ipport," ",Outip," ",Outport," ",date," ")
    print(domainn)
