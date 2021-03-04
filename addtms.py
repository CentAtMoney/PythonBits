#!/usr/bin/python

import os
import json
import sys

def main(argv):
    stats_dir = "./pixelmon/stats/"
    
    my_tms = all_tms()
    
    if len(argv) == 2:
        my_tems = set()
        with open(argv[1]) as f:
            for line in f:
                if(len(line) < 1):
                    continue
                
                token = line.strip()
                my_tms.add(token)

    sorted_tms = sorted(list(my_tms))

    print("TMs:")
    for tm in sorted_tms:
        print(tm)

    print("write TMs?")
    response = input()

    if response[0] == 'y':
        write_tms(stats_dir, my_tms)
        print("TMs written")


    print("TRs:")
    my_trs = all_trs()
    for tr in my_trs:
        print(tr)

    print("write TRs?")
    response = input()

    if response[0] == 'y':
        write_trs(stats_dir, my_trs)
        print("TRs written")

    print("exiting...")


def collect_tms(stats_dir):
    tms = set()
    for filename in os.listdir(stats_dir):
        with open(stats_dir + filename) as f:
            o = json.load(f)
            if "tmMoves" in o:
                tms.update(o["tmMoves"])
    return tms

def update_mons(stats_dir, key, value, verbose=False):
    for filename in os.listdir(stats_dir):
        o = None
        name = "Unknown"
        file_path = stats_dir + filename
        with open(file_path) as f:
            o = json.load(f)

        if o is None:
            continue

        if key not in o:
            continue
        else:
            o[key] = value
        if "pixelmonName" in o:
            name = o["pixelmonName"]
        elif "pokemon" in o:
            name = o["pokemon"]
        
        if verbose is True:
            print("Updating: " + key + " for: " + name)

        with open(file_path, "w") as f:
            json.dump(o, f, indent=4, sort_keys=True)
        

def write_tms(stats_dir, tms):
    if type(tms) != set:
        print("Bad tms type! tms should be a set.")
        return

    if len(tms) == 0:
        print("No tms to write!")
        return

    sorted_tms = sorted(list(tms))
    
    update_mons(stats_dir, "tmMoves", sorted_tms)

def write_trs(stats_dir, trs):
    update_mons(stats_dir, "trMoves", list(trs))

def all_trs():
    trs = list(range(0, 100))
    return trs

            
def all_tms():
    return [
"Acrobatics",
"Aerial Ace",
"Ally Switch",
"Assurance",
"Attract",
"Aurora Veil",
"Avalanche",
"Bide",
"Blizzard",
"Body Slam",
"Brick Break",
"Brine",
"Brutal Swing",
"Bubble Beam",
"Bulk Up",
"Bulldoze",
"Bullet Seed",
"Calm Mind",
"Captivate",
"Charge Beam",
"Confide",
"Counter",
"Curse",
"Cut",
"Dark Pulse",
"Dazzling Gleam",
"Defense Curl",
"Detect",
"Dig",
"Double Team",
"Double-Edge",
"Dragon Breath",
"Dragon Claw",
"Dragon Pulse",
"Dragon Rage",
"Dragon Tail",
"Drain Punch",
"Dream Eater",
"Dynamic Punch",
"Earthquake",
"Echoed Voice",
"Egg Bomb",
"Embargo",
"Endure",
"Energy Ball",
"Explosion",
"Facade",
"False Swipe",
"Fire Blast",
"Fire Punch",
"Fissure",
"Flame Charge",
"Flamethrower",
"Flash",
"Flash Cannon",
"Fling",
"Fly",
"Focus Blast",
"Focus Energy",
"Focus Punch",
"Frost Breath",
"Frustration",
"Fury Cutter",
"Giga Drain",
"Giga Impact",
"Grass Knot",
"Gyro Ball",
"Hail",
"Headbutt",
"Hidden Power",
"Hone Claws",
"Horn Drill",
"Hyper Beam",
"Ice Beam",
"Ice Punch",
"Icy Wind",
"Incinerate",
"Infestation",
"Iron Tail",
"Leech Life",
"Light Screen",
"Low Kick",
"Low Sweep",
"Magical Leaf",
"Mega Drain",
"Mega Kick",
"Mega Punch",
"Metronome",
"Mimic",
"Mud-Slap",
"Natural Gift",
"Nature Power",
"Nightmare",
"Overheat",
"Pay Day",
"Payback",
"Pluck",
"Poison Jab",
"Power-Up Punch",
"Protect",
"Psych Up",
"Psychic",
"Psyshock",
"Psywave",
"Quash",
"Rage",
"Rain Dance",
"Razor Wind",
"Recycle",
"Reflect",
"Rest",
"Retaliate",
"Return",
"Roar",
"Rock Polish",
"Rock Slide",
"Rock Smash",
"Rock Tomb",
"Rollout",
"Roost",
"Round",
"Safeguard",
"Sandstorm",
"Scald",
"Screech",
"Secret Power",
"Seismic Toss",
"Self-Destruct",
"Shadow Ball",
"Shadow Claw",
"Shock Wave",
"Silver Wind",
"Skill Swap",
"Skull Bash",
"Sky Attack",
"Sky Drop",
"Sleep Talk",
"Sludge Bomb",
"Sludge Wave",
"Smack Down",
"Smart Strike",
"Snarl",
"Snatch",
"Snore",
"Soft-Boiled",
"Solar Beam",
"Solar Blade",
"Stealth Rock",
"Steel Wing",
"Stone Edge",
"Struggle Bug",
"Submission",
"Substitute",
"Sunny Day",
"Superpower",
"Surf",
"Swagger",
"Sweet Scent",
"Swift",
"Swords Dance",
"Take Down",
"Taunt",
"Telekinesis",
"Teleport",
"Thief",
"Thunder",
"Thunder Punch",
"Thunder Wave",
"Thunderbolt",
"Torment",
"Toxic",
"Tri Attack",
"Trick Room",
"U-Turn",
"Uproar",
"Venoshock",
"Volt Switch",
"Water Gun",
"Water Pulse",
"Waterfall",
"Whirlwind",
"Wild Charge",
"Will-O-Wisp",
"Work Up",
"X-Scissor",
"Zap Cannon"
]
if __name__ == "__main__":
    main(sys.argv)

