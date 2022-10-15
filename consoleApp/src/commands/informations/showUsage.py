import os

print("Usage: \n")

cmdsPath = "./src/commands/"
dataPath = "./src/data/showUsage.txt"

index = 0

for cmdF in os.listdir("./src/commands/"):
    commands = os.listdir(cmdsPath + cmdF + "/")
    for cmd in commands:
        cmdR = cmd.split('.')

        with open(dataPath) as jF:
            JUF = jF.readlines()
            JUFU = JUF[index].split(": ")
            print(" - Command: " + JUFU[0] + ", Usage: " + JUFU[1])
            index = index + 1