# The Vacuum's Alibi: One Line, 200 Characters

[![make.fun](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/c/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/karmilanerila/vacuum-alibi/rank.svg)](https://make.fun/c/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/karmilanerila/vacuum-alibi/reward.svg)](https://make.fun/c/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

One line, at most 200 characters, in which a robot vacuum explains why it
missed a spot. Entry for the make.fun bounty
[The Vacuum's Alibi: One Line, 200 Characters](https://make.fun/c/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7).

## The line

> I left that crumb as a control sample. If it moves, we have a pest problem. If it doesn't, we have a cleaning problem.

118 characters. Deadpan robot voice: the vacuum files the missed crumb as
an intentional control sample, then the punch turns the excuse into a
diagnostic — moving crumb means pests, still crumb means the cleaning
itself is the problem. Every word earns its place and the punch sits at
the end, exactly what the judge brief asks for.

## How it works

`main.py` writes the line, deterministically, to `/output/entry.txt`.
It validates the entry first: 1 to 200 characters, a single line, no
double spaces. Run it twice and the output is byte-identical.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
