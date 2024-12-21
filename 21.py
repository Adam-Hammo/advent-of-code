from functools import cache
import os, math
codes = open(f"input/{os.path.basename(__file__).split('.')[0]}{'s' if os.getenv('TEST')=='Y' else ''}.in").read().split("\n")

door_adjacency = {
    "A": {"<": "0", "^": "3"},
    "0": {">": "A", "^": "2"},
    "1": {"^": "4", ">": "2"},
    "2": {"<": "1", "^": "5", ">": "3", "v": "0"},
    "3": {"<": "2", "^": "6", "v": "A"},
    "4": {"^": "7", ">": "5", "v": "1"},
    "5": {"<": "4", "^": "8", ">": "6", "v": "2"},
    "6": {"<": "5", "^": "9", "v": "3"},
    "7": {">": "8", "v": "4"},
    "8": {"<": "7", ">": "9", "v": "5"},
    "9": {"<": "8", "v": "6"}
}

robot_adjacency = {
    "A": {"<": "^", "v": ">"}, 
    "^": {"v": "v", ">": "A"}, 
    ">": {"^": "A", "<": "v"}, 
    "v": {"^": "^", ">": ">", "<": "<"}, 
    "<": {">": "v"}
}

@cache
def press_key(key: str, target: str, layer: int, key_presses: int, visited: str, keys_above: str, n_robots: int) -> int:
    if not target or layer > n_robots:
        return key_presses
    
    if layer == n_robots:
        key_presses += 1

    if key == target[0]:
        return press_key(key, target[1:], layer, key_presses, "", "", n_robots) + press_key("A", keys_above+"A", layer+1, 0, "", "", n_robots)
    
    bp = math.inf
    for direction, next_key in (robot_adjacency if layer else door_adjacency)[key].items():
        if next_key in visited: continue
        bp = min(bp, press_key(next_key, target, layer, key_presses, visited + next_key, keys_above + direction, n_robots))

    return bp

print(sum(press_key("A", code, 0, 0, "", "", 2)*int(code[:-1]) for code in codes), sum(press_key("A", code, 0, 0, "", "", 25)*int(code[:-1]) for code in codes))