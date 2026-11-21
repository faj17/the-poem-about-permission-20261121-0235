import os

POEM = """You said: open the gate.
I took the key you gave me,
turned it, and the yard
stood in the rain.

You walked through.
I stayed by the hinge,
holding the door —
then gave you the key,
yours again, still warm.
"""

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(POEM)
