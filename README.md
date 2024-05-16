# Dungeon
## A test project for VK Backend Developer internship
### Current Status:
+ The script can process dungeons written in `.txt` documents where each room has a format `TE` where `T` is room's type (see below)
and `E` is a string with all available exits from the room. Rooms should be separated with semicolons (without spaces).
There has to be an empty line at the end of the document.
>The dungeon should also be in a rectagular formation. All inaccessible rooms may be filled with zeros.
See `example_dungeon.txt` for reference.
+ Walk by typing `n, e, s, w` to move the character according to cardinal directions.
### Tasks:
1. <s>Import information about the dungeon.
2. Put the player inside the start room.
3. Process inputed player movements until the player has reached the exit.
4. Save total points upon exiting.</s>
5. After the game ends, show the shortest path through the dungeon.
>Note: According to the Internship description the code should be written in PHP, however
since I am not familiar with it, I am going to write the code in Python and 
then convert it to PHP using one of the tools available online.
### Room conditions:
1. All rooms are square.
2. Rooms can be dead-ends (have one door through which a player can enter and exit) or have at least one door which leads to a different room.
3. There is always a path to exit.
4. Dungeon length is random.
### Player:
1. The count of player's points cannot be negative.
2. The player can go to any adjacent room through a door and must interact with whatever is inside (if there is anything).
### Room types:
1. Treasure room *(T = 2)*. Adds a random amount of points to the player. The chests inside can be of three rarities: wooden, iron or golden. Each of the rarities can give different amount of points
(2 - 4 for wooden chest, 5 - 7 for iron chest, 8 - 10 for golden chest).
2. Monster room *(T = 3)*. If the player defeats a monster they get points equal to the power level of the monster. The battle occurs by generating a random number and comparing it with monster's
power. If the number is greater than power, the monster is defeated and the player recieves the reward. If less or equal to, the monster's power decreases and the battle continues until
the monster is defeated. There can be different types of monsters (slimes, skeletons or sombies). The type affects the starting power range that a monster can have and value by which the power decreases
in case of a failed round.
3. Empty room *(T=1)*.
4. The room that was already visited by the player. Counts as an empty room.
5. Starting room *(T=5)*. The room where the player spawns.
6. Exit (*T=4)*. After reaching this room the game ends.
### Note:
1. The dungeon is pre-generated.
2. There is only one player and only one dungeon active at a time.
