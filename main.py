import re
from icecream import ic
import random

MONSTER_TYPES = {'0': None,
                 '1': 'slime',
                 '2': 'skeleton',
                 '3': 'zombie'}

CHEST_TYPES = {'0': None,
               '1': 'a wooden',
               '2': 'an iron',
               '3': 'a golden'}

ROOM_TYPES = {'0': None,
              '1': 'empty',
              '2': CHEST_TYPES,
              '3': MONSTER_TYPES,
              '4': 'exit',
              '5': 'start'}


def import_dungeon(where_from, where_to: list):
    with open(where_from) as file:
        for row in file:
            where_to.append(row.split(';')[:-1])


def handle_movement(direction):
    match direction:
        case 'n':
            print("Going north\n")
            return -1, 0
        case 'e':
            print("Going east\n")
            return 0, 1
        case 's':
            print("Going south\n")
            return 1, 0
        case 'w':
            print("Going west\n")
            return 0, -1


def handle_room(location, type):
    global chests, points, found_exit
    match type:
        case 'empty':
            pass
        case '2':
            found_chest = [ch for ch in chests if list(ch.room) == location]
            points += handle_treasure(found_chest[0].type)
            rooms[location[0]][location[1]].type = 1
        case '3':
            found_monster = [m for m in monsters if list(m.room) == location]
            points += handle_monster(found_monster[0].type)
            rooms[location[0]][location[1]].type = 1
        case '4':
            print(f"You've escaped the dungeon.\nPoints collected: {points}.")
            found_exit = True



def handle_treasure(chest_type):
    print(f"There is {CHEST_TYPES[chest_type]} chest here.")
    match CHEST_TYPES[chest_type]:
        case 'a wooden':
            loot = random.randint(2, 4)
        case 'an iron':
            loot = random.randint(5, 7)
        case 'a golden':
            loot = random.randint(8, 10)
    print(f"You've acquired {loot} points.\nPress Enter to continue.")
    input()
    return loot


def handle_monster(monster_type):
    print(f"There is a {MONSTER_TYPES[monster_type]} here.")
    match MONSTER_TYPES[monster_type]:
        case 'slime':
            power = random.randint(5, 8)
            debuff = 4
        case 'skeleton':
            power = random.randint(9, 12)
            debuff = 3
        case 'zombie':
            power = random.randint(13, 16)
            debuff = 2
    reward = power
    while power >= 0:
        attack = random.randint(2,7)
        print(f"\nYou hit the {MONSTER_TYPES[monster_type]} for {attack} points.")
        if attack > power:
            print(f"The {MONSTER_TYPES[monster_type]} falls to the ground, defeated.")
            print(f"You've acquired {reward} points.\nPress Enter to continue.")
            input()
            return reward
        else:
            print(f"The {MONSTER_TYPES[monster_type]} is weakened.")
            input("Press Enter to continue.")
            power -= debuff
            ic(power)



class Player:
    def __init__(self, room: tuple, points: int):
        self.room = room
        self.points = points


class Room:
    def __init__(self, type, exits):
        self.type = type
        self.exits = exits


class Monster:
    def __init__(self, room, type):
        self.room = room
        self.type = type


class Chest:
    def __init__(self, room, type):
        self.room = room
        self.type = type


rooms = []
chests = []
monsters = []
points = 0
found_exit = False
import_dungeon("example_dungeon.txt", rooms)
dung_height = dung_width = len(rooms)
for j in range(dung_height):
    for i in range(dung_width):
        if rooms[j][i][0] == '2':
            chests.append(Chest((j, i), rooms[j][i][1]))
            rooms[j][i] = Room(type=rooms[j][i][0], exits=rooms[j][i][2:])
        elif rooms[j][i][0] == '3':
            monsters.append(Monster((j, i), rooms[j][i][1]))
            rooms[j][i] = Room(type=rooms[j][i][0], exits=rooms[j][i][2:])
        else:
            rooms[j][i] = Room(type=rooms[j][i][0], exits=rooms[j][i][1:])
        if ROOM_TYPES[rooms[j][i].type[0]] == 'start':
            player = Player((j, i), points)

while not found_exit:
    exits = [i for i in rooms[player.room[0]][player.room[1]].exits]
    print("You are in an empty room. Exits available:", ' '.join(exits))
    direction = input("Where would you like to go?\n")
    while direction not in exits:
        direction = input("There is no exit there.\n")
    player.room = [x + y for x, y in zip(player.room, handle_movement(direction))]
    handle_room(player.room, rooms[player.room[0]][player.room[1]].type)
    # print(player.room, points)
