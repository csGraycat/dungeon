# Dungeon
## A test project for VK Backend Developer internship
### Room conditions:
1. All rooms are square.
2. Rooms can be dead-ends (have one door through which a player can enter and exit) or have at least one door which leads to a different room.
3. There is always a path to exit.
4. Dungeon length is random.
### Player:
1. The count of player's points cannot be negative.
2. The player can go to any adjacent room through a door and must interact with whatever is inside (if there is anything).
### Room types:
1. Treasure room. Adds a random amount of points to the player. The chests inside can be of three rarities: wooden, iron or golden. Each of the rarities can give different amount of points
(2 - 4 for wooden chest, 5 - 7 for iron chest, 8 - 10 for golden chest).
2. Monster room. If the player defeats a monster they get points equal to the strength level of the monster. The battle occurs by generating a random number and comparing it with monster's
strength. If the number is greater than strength, the monster is defeated and the player recieves the reward. If less or equal to, the monster's strength decreases and the battle continues until
the monster is defeated. There can be different types of monsters (add later). The type affects the starting strength range that a monster can have and value by which the strength decreases
in case of a failed round.
3. Empty room.
4. The room that was already visited by the player. Counts as an empty room.
### Tasks:
1. Import information about the dungeon.
2. Put the player inside the start room.
3. Process inputed player movements until the player has reached the exit.
4. Save total points upon exiting.
5. After the game ends, output the shortest path through the dungeon.
### Note:
1. The dungeon is pre-generated.
2. There is only one player and only one dungeon active at a time.
