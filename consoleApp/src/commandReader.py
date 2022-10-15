import os

cmdsPath = "./src/commands/"

def commandExecutor(cmdName):
    commandsFolder = os.listdir(cmdsPath)
    for cmdF in commandsFolder:
        commands = os.listdir(cmdsPath + cmdF + "/")
        for cmd in commands:
            if cmd == cmdName + ".py":
                print("\nExecuting command... \n")
                exec(open(cmdsPath + cmdF + "/" + cmd).read())
                return
    
    print("\nThis command doesnt exists! \nFor help type: 'help'!")