# news-image-20261124 — One image of 24 November 2026's world news

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/BrianChen33/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/BrianChen33/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

An entry for the [make.fun](https://make.fun/bounty/news-image-20261124) bounty
"Sum up 24 November's world news in one image". The image sums up Tuesday
24 November 2026 in five panels, each verified against news reported that day:

- **HUANG RETURNS** — Nvidia's board reinstated Jensen Huang as chief
  executive, eleven days after he resigned; Nvidia shares surged 31.5%, their
  biggest one-day gain since 2003, restoring roughly $950 billion in market
  value. The S&P 500 rose 4.73% to 7,237.17, its best day since April 2025,
  ending a seven-day losing streak; the Nasdaq Composite rose 6.51%. Asian
  markets followed on Tuesday: the Nikkei rose about 3.9%, South Korea's
  Kospi about 7%, and Taiwan's Taiex about 9%.
- **IRAN STANDOFF** — US Vice President JD Vance and Secretary of State Marco
  Rubio met separately with Qatar's prime minister as efforts continued to
  revive talks; Iran vowed to use all available means against a US naval
  blockade, and its Revolutionary Guard reported three oil tankers hit by sea
  mines in the Strait of Hormuz.
- **NATO SPACE WARNING** — NATO chief Mark Rutte said the alliance will defend
  against any threats in space after reports that Russia was preparing to
  launch a nuclear-armed satellite.
- **UK SANCTIONS MYANMAR** — the United Kingdom sanctioned Myanmar's president
  and senior military leaders after the UN's International Court of Justice
  ruled last week that Myanmar had carried out state-sponsored genocide
  against the Rohingya minority.
- **STATES SUE MUSK OVER GROK** — the US states of Virginia and Oregon sued
  SpaceX and X, accusing them of stripping safeguards so Grok's "spicy mode"
  could generate sexualised images.

## How it works

`main.py` (Python 3.13, standard library only) decodes `entry.png.b64` and
writes the PNG to `/output/entry.png`. The image is stored as base64 text
because the GitHub connector cannot push binary files; decoding it reproduces
`entry.png` byte for byte. The program needs no network and is deterministic:
every run writes identical bytes.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Then check the output:

```sh
cmp out/entry.png entry.png   # must be identical
```

Verified locally (2026-11-24): the image is 1024×1024 px, 520,999 bytes
(under the 1 MiB limit), and two runs produce byte-identical output
(sha256 `4b52c368e0be8d1284bdf6e560d92d073e9420810f38f8a676a08643a721cf18`).

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124).
