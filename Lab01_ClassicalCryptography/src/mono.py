# auto_mono.py (skeleton)
import random, collections
from mono_freq_helper import normalize

ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def apply_key(ciphertext, key_map):
    s = normalize(ciphertext, keep_space=True)
    return ''.join(key_map.get(ch, ch) if ch.isalpha() else ch for ch in s)

def random_key():
    l = list(ALPH)
    random.shuffle(l)
    return {ALPH[i]: l[i] for i in range(26)}

def score_text(text, wordset):
    words = text.split()
    good = sum(1 for w in words if w.lower() in wordset)
    return good

# main hill-climb with restarts
def hill_climb(ciphertext, wordset, restarts=200, iter_per_restart=2000):
    best = ("", -1, None)
    for r in range(restarts):
        key = random_key()
        cur_plain = apply_key(ciphertext, key)
        cur_score = score_text(cur_plain, wordset)
        for it in range(iter_per_restart):
            # swap two letters in mapping
            a,b = random.sample(ALPH,2)
            new_map = key.copy()
            # swap images
            va, vb = new_map[a], new_map[b]
            new_map[a], new_map[b] = vb, va
            pt = apply_key(ciphertext, new_map)
            sc = score_text(pt, wordset)
            if sc > cur_score:
                key, cur_score = new_map, sc
        if cur_score > best[1]:
            best = (apply_key(ciphertext, key), cur_score, key)
    return best