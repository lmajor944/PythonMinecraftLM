from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

name = ""
scoreboard = []

while True:
    name = input("Enter Name: ")
    if name != "exit":
        scoreboard.append(name)
    if name == "exit":
        break
    time.sleep(6) 
blockHits = mc.events.pollBlockHits()
blockHitsLength = len(blockHits)
mc.postToChat("Your score is " + str(blockHitsLength))
scoreboard.append(blockHitsLength)

for name in scoreboard:
    print(scoreboard)
    

