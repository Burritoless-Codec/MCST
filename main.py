import os
import time
#Setup for start.bat file with Ram and Jar executable name
def sbat():
    print('Starting job start.bat')
    print('---------------------------------------------')
    print('Server will by default start with no gui only cli.')
    #asks for amount of ram to use
    aram = int(input('How many gigabytes of ram? :'))
    #asks for executable server jar
    jarname = str(input('What is the .jar name?(ie: server.jar) '))

    #creates/overwrites start.bat file with new variables
    sbf = open('start.bat', 'w')
    sbf.write('java -Xmx' + str(aram) + 'G -Xms' + str(aram) + 'G -jar ' + str(jarname) + ' nogui\n')
    sbf.write('pause\n')
    sbf.close()
    print('start.bat job finished!')
def eulat():
    print('Starting job eula.txt')
    euf = open('eula.txt', 'w')
    euf.write('eula=true')
    print('Eula set to true')
    euf.close()
    print('eula.txt job finished!')
def servers(question = "[y/n]", strict = True):
    print('Start server?')
    question = question.strip(" ")
    x = input("%s " % question)
    x = x.lower()
    if (x == "yes") or (x == "y"):
        os.startfile('start.bat')
    elif (x == "no") or (x == "n") :
        print('Exiting program.')
        time.sleep(20)
        exit()
    else:
        return servers(strict=strict)



#starts program and calls eula and start.bat functions
print('Starting program.')
print('---------------------------------------------')
eulat()
print('---------------------------------------------')
sbat()
print('---------------------------------------------')
servers()
