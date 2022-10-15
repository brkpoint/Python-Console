import os

print("commands: \n")

cmdsPath = "./src/commands/"

for cmdF in os.listdir("./src/commands/"):
    commands = os.listdir(cmdsPath + cmdF + "/")
    for cmd in commands:
        cmdF = cmd.split('.')
        print(" - " + cmdF[0])