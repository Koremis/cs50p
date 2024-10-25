#!/usr/bin/env python3
"""convert ascii emoji to emoji"""

face = input("Make a face: ")
if ":)" in face:
    print(face.replace(":)", "🙂"))
if ":(" in face:
    print(face.replace(":(", "🙁"))
else:
    print("I don't like that face")
