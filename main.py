import os
import time
#Setup for start.bat file with Ram and Jar executable name
div = '---------------------------------------------'
def sbat():
    print('Starting job start.bat')
    print(div)
    print('Server will by default start with no gui only cli.')
    #asks for amount of ram to use
    aram = int(input('How many gigabytes of ram? :'))
    #asks for executable server jar
    jarname = str(input('What is the .jar name?(ie: server.jar) '))

    #creates/overwrites start.bat file with new variables
    sbf = open('start.bat', 'w')
    sbf.write('@echo off\ncls\n:start\n')
    sbf.write('java -Xmx' + str(aram) + 'G -Xms' + str(aram) + 'G -jar ' + str(jarname) + ' nogui\n')
    sbf.write('echo (%time%) Server closed/crashed... restarting!\ngoto start')
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
        time.sleep(5)
        exit()
    else:
        return servers(strict=strict)

def sprop():
    print('Starting job server.properties')


    spf = open('server.properties', 'w')

    wl = str(input('white listed true/false:'))
    hc = str(input('Hardcore mode true/false:'))
    mp = int(input('Max players (i.e. 10): '))
    pvp = str(input('PVP true/false: '))
    motd = str(input('Server Motd: '))


    print('Updating settings')

    spf.write('#server.properties generated with MCST\n')
    spf.write('generator-settings=\n')
    spf.write('op-permission-level=4\n')
    spf.write('allow-nether=true\n')
    spf.write('level-name=world\n')
    spf.write('enable-query=false\n')
    spf.write('allow-flight=false\n')
    spf.write('announce-player-achievements=true\n')
    spf.write('server-port=25565\n')
    spf.write('max-world-size=29999984\n')
    spf.write('level-type=DEFAULT\n')
    spf.write('enable-rcon=false\n')
    spf.write('level-seed=\n')
    spf.write('force-gamemode=false\n')
    spf.write('server-ip=\n')
    spf.write('network-compression-threshold=256\n')
    spf.write('max-build-height=256\n')
    spf.write('spawn-npcs=true\n')
    spf.write('white-list=' + wl.lower() + '\n')
    spf.write('spawn-animals=true\n')
    spf.write('hardcore=' + hc.lower() + '\n')
    spf.write('snooper-enabled=true\n')
    spf.write('resource-pack-sha1=\n')
    spf.write('online-mode=true\n')
    spf.write('resource-pack=\n')
    spf.write('pvp=' + pvp.lower() + '\n')
    spf.write('difficulty=1\n')
    spf.write('enable-command-block=false\n')
    spf.write('gamemode=20\n')
    spf.write('player-idle-timeout=0\n')
    spf.write('max-players=' + str(mp) + '\n')
    spf.write('max-tick-time=60000\n')
    spf.write('spawn-monsters=true\n')
    spf.write('generate-structures=true\n')
    spf.write('view-distance=10\n')
    spf.write('motd=' + motd + '\n')
    spf.close()
    print('server.properties job finished')


#starts program and calls eula and start.bat functions
print('Starting program.')
print(div)
eulat()
print(div)
sbat()
print(div)
sprop()
print(div)
servers()
