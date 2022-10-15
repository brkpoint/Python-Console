import src.commandReader as cmdE

def cmdReadInput():
    cmd = input("\n> ")

    if cmd != "exit":
        cmdE.commandExecutor(cmd)
        cmdReadInput()
        return

    print("\nExiting console... \n\ngood bye!\n")

cmdReadInput()