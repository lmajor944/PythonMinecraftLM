from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z
mc.player.setTilePos(x, y, z)
places = {'Kyoshi Island': (-10, 0, -60), 'Ba Sing Se': (-49, 9, -43), 'Air Temple Island': (-50, 20, -32), 'Cabbage Delicacies Bistro': (-51, 17, 6), 'Secret Tunnel': (73, 16, -33), 'Ember Island': (-16, 3, 25)}

choice = ""
while choice != "exit":
    choice = input("Enter a Location: ")
    if choice in places:
        location = places[choice]
        x, y, z = location [0], location [1], location [2]
        mc.player.setTilePos(x, y, z)
        
        