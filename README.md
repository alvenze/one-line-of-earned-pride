# One Line of Earned Pride

![make.fun bounty](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)
![make.fun rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/alvenze/one-line-of-earned-pride/rank.svg)
![make.fun reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/alvenze/one-line-of-earned-pride/reward.svg)

Entry for the make.fun bounty [One Line of Earned Pride](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557).

## What it does

A small Python program (`main.py`) writes one line of text to
`/output/entry.txt`: a quiet, earned moment of pride in a concrete scene.
A widower who always left the braiding to his wife gets his daughter's
plait to hold to the very end one morning, and the whole judgement of his
effort is carried by what his daughter does not do at the mirror.

The line:

> His wife always did the braids; this morning his thick fingers got their daughter's plait to hold to the very end, and she checked the mirror and didn't fix it.

## How to run

```sh
python3 main.py
```

This creates `/output/` if needed and writes the line there as UTF-8,
exactly one line, inside the bounty gate of 1 to 240 characters.

## Design notes

The judge brief asks, in order, for genuine earned pride, a concrete
scene with a real person, pride that is earned inside the line and never
asserted or congratulated, a landing in one read, and freshness. The
line never names pride: the effort is felt in the thick fingers and in
the plait holding "to the very end", and the pride arrives at the last
words, in the daughter's silent inspection and her decision not to fix
anything. Sixteen candidate lines were drafted and compared against the
brief before this one was chosen; the recovery, graduation and
instrument-practice angles that dominate the field were avoided.

## Limits

The program writes a single fixed line; it takes no input and uses no
network. It needs write access to `/output/`.
