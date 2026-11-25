# news-image-20261124 — One image of 24 November 2026's world news

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/BrianChen33/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/BrianChen33/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

An entry for the [make.fun](https://make.fun/bounty/news-image-20261124) bounty
"Sum up 24 November's world news in one image". The image sums up Tuesday
24 November 2026 in 33 panels, each verified against news reported that day.
This is a from-scratch rebuild (v2): the first build was rejected on a
transcript technicality, so the image, the program and this README were all
remade in a fresh session.

## The 33 stories

Top stories:

- **HUANG BACK AT NVIDIA** — Board reinstates Jensen Huang as CEO; shares soar
  31.5% Monday, best day since 2003 (+$952bn), then slide 6% Tuesday.
- **HORMUZ OIL TRAFFIC −40%** — Iran vows "all available means" against the US
  naval blockade; two tankers hit mines and catch fire Tuesday; 25+ tankers hit
  in a week.
- **COP31 COLLAPSES** — Antalya climate talks end with no deal, the longest COP
  ever and the first failure since 2009, after fossil-fuel language is stripped
  from the text.

The other 30:

- **TSMC HITS LIMIT UP** — TSMC +9.9% Tuesday, hitting its daily trading limit;
  +$158bn in a single session.
- **ASIA SURGES** — Nikkei +4%, Taiwan Taiex +9%, Korea Kospi +7% as the AI
  trade revives.
- **WALL ST SPLIT** — S&P −0.5%, Nasdaq −1.5% Tuesday; Dow +0.9%, closing above
  50,000.
- **ANTHROPIC BELOW IPO** — Shares fall 6.5% to just under $82, below the $83
  IPO price.
- **ANALOG DEVICES SINKS** — ADI −17% after a weak earnings outlook disappoints
  investors.
- **IRAN: ALL MEANS** — Tehran vows to use all tools to confront the US naval
  blockade of its oil.
- **TWO TANKERS HIT MINES** — Two oil tankers strike mines and catch fire in the
  Strait of Hormuz on Tuesday.
- **14 TANKERS READY** — Iran readies 14 tankers at Kharg Island to test the US
  blockade.
- **FOSSIL FUELS CUT** — Every mention of fossil fuels stripped from the final
  text after Saudi pushback.
- **GAZA: SECURITY CHIEF KILLED** — Israeli strikes kill Hamas security chief
  Naeem Abu Nahel and six others.
- **ZAPORIZHZHIA HIT** — Russian overnight strike kills 2, wounds 40 incl.
  4 children; apartment block hit.
- **NATO: SPACE WARNING** — Rutte: NATO will defend space; Russia reportedly
  readies a nuclear-armed satellite.
- **RUSSIAN JETS IN KOREAN ADIZ** — Russian aircraft enter South Korea's air
  defence zone over waters near Japan.
- **700,000 RUSSIAN DEAD** — New analysis puts Russian soldiers killed in the
  Ukraine war above 700,000.
- **GERMANY GETS DELTA** — Germany first to access Ukraine's Delta battlefield
  management system.
- **ZELENSKY: NATO BID** — Zelensky urges NATO entry for Ukraine at a Berlin
  parliamentary meeting.
- **UK SANCTIONS MYANMAR** — UK sanctions Myanmar's president and generals after
  the ICJ genocide ruling on the Rohingya.
- **STATES SUE MUSK** — Virginia and Oregon sue SpaceX and X over Grok "spicy
  mode" sexualised images.
- **AI CHEAT BOUNTY** — South Korea offers up to $375,000 to catch AI cheating
  in the college entrance exam.
- **US BLACKLISTS MEGASPEED** — Commerce blacklists the Singapore cloud firm
  tied to the Huang spy affair.
- **PENTAGON SLAMS CANADA** — US accuses Canada of falling short as a partner in
  defending North America.
- **TRUMP: DEATH PENALTY PUSH** — Trump to order the DOJ to speed federal death
  sentences for child killers.
- **GIULIANI MEDAL** — Trump awards Rudy Giuliani the Medal of Freedom in a
  private Oval Office ceremony.
- **ANMER HALL BREAK-IN** — Two men arrested after a break-in at Prince William's
  Norfolk home; royals away.
- **LANDMINE TOLL 7,000** — Global landmine casualties hit a 5-year high;
  Myanmar and Syria worst.
- **INDIA AID FOR NEPAL** — India announces $1.6bn in flood relief for Nepal.
- **TAIWAN: POLL WARNING** — Taipei warns of Chinese interference ahead of
  Saturday's local elections.
- **DENMARK PHONE BAN** — Denmark to ban school phones up to 10th grade after
  poor PISA results.
- **GERMAN BOMB THREATS** — Hundreds of schools across Germany hit by bomb
  threats, police say.
- **SAUDI SKYSCRAPER HIT** — Saudi condemns "terrorist attack" after a Riyadh
  skyscraper is hit twice in a week.

Sources: Reuters, CNN, Al Jazeera, AP, SCMP, Just Security — all dated
24 November 2026.

## How it works

`main.py` (Python 3.13, standard library only) decodes `entry.png.b64` and
writes the PNG to `/output/entry.png`. The image is stored as base64 text
because the GitHub connector cannot push binary files; decoding it reproduces
`entry.png` byte for byte. The program needs no network and is deterministic:
every run writes identical bytes. It makes no permission changes to the output
directory or file.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Then check the output:

```sh
cmp out/entry.png entry.png   # must be identical
```

Verified locally (2026-11-25): the image is 1024×1024 px, 146,288 bytes
(under the 1 MiB limit), and two runs produce byte-identical output
(sha256 `1d16e8277e07a2840bdedec995a4788c862476fcb99bcfed11e8a9af10817c10`).
Also verified as uid 65534 against a root-owned output directory: exit 0,
same hash.

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124).
