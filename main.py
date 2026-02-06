#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project: Deterministic Finite Automaton Simulation (Automaton A)
Course: Theory of Languages

"""

import string

# Alphabet Δ = {A..Z}
ALPHABET = set(string.ascii_uppercase)

# States
INITIAL_STATE = 8
FINAL_STATES = {1, 2, 3}

# Special transitions table
SPECIAL_TRANSITIONS = {
    8: {'W': 4, 'I': 9},
    4: {'H': 5},
    5: {'I': 6},
    6: {'L': 7},
    7: {'E': 1},
    9: {'F': 2},
}

def is_in_alphabet(c: str) -> bool:
    return c in ALPHABET

def transition(state: int, symbol: str) -> int:
    if not is_in_alphabet(symbol):
        raise ValueError(f"Invalid symbol: {symbol}")

    # States 1 and 2 always go to 3
    if state in (1, 2):
        next_state = 3

    # State 3 loops on itself
    elif state == 3:
        next_state = 3

    # Other states: use table, otherwise go to 3
    else:
        next_state = SPECIAL_TRANSITIONS.get(state, {}).get(symbol, 3)

    print(symbol, " ", state, "->", next_state)
    return next_state

def normalize_input(s: str) -> str:
    s = s.strip()
    if s in {'ε', 'epsilon', 'EPSILON'}:
        return ''
    return s.replace(' ', '').upper()

def run_automaton(start_state: int, word: str):
    current = start_state
    path = [current]

    for ch in word:
        current = transition(current, ch)
        path.append(current)

    return current in FINAL_STATES, path


if __name__ == "__main__":
    word = normalize_input(input("Enter a word over Δ={A..Z} (or ε): "))

    try:
        accepted, path = run_automaton(INITIAL_STATE, word)
        decision = "ACCEPTED" if accepted else "REJECTED"
        display_word = word if word != '' else 'ε'

        print("\nWord:", display_word)
        print("Decision:", decision)
        print("Path:", " -> ".join(map(str, path)))

    except ValueError as e:
        print("Error:", e)