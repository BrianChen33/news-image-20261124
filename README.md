# news-image-20261124 — One image of 24 November 2026's world news

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/BrianChen33/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/BrianChen33/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

An entry for the [make.fun](https://make.fun/bounty/news-image-20261124) bounty
"Sum up 24 November's world news in one image". The image sums up Tuesday
24 November 2026 in 33 panels, each verified against news reported that day.
This is a from-scratch rebuild (v2): the first build was rejected on a
transcript technicality, so the image, the program and this README were all
remade in a fresh session. v3 revises v2 per a GPT review (ChatGPT Work,
GPT-6.2 Astra High): factual corrections, a dominant Hormuz lead, and a
5-column grid.

## The 33 stories

Lead stories:

- **HORMUZ CROSSINGS PLUNGE 45%** — Tracked weekly vessel crossings fell
  from 226 (Nov 1-7) to 125 (Nov 17-23), Marine Traffic data; Iran's navy
  is blamed for mine strikes on two tankers Tuesday; Tehran vows "all
  available means" vs the US blockade.
- **HUANG APOLOGISES TO STAFF AS NVIDIA FALLS 5.9%** — At an hour-long
  all-hands meeting Tuesday, he admits code-of-conduct violations and says
  he is in therapy (Reuters).
- **EU SEEKS OVERHAUL OF CLIMATE TALKS AFTER COP31 FAILURE** — Hoekstra
  tells the FT the EU will propose scrapping consensus rules after Sunday's
  collapse; the draft dropped fossil fuels.

The other 30:

- **TAIWAN STOCKS JUMP 9%** — Taiex +8.99% to a record 40,122; TSMC hits
  its 10% limit, +$158bn in a day.
- **EBOLA VACCINE DEAL FOR CONGO** — Gavi agrees to buy up to 1.5m doses
  if trials succeed; the outbreak has killed 5,700+.
- **GAZA STRIKES KILL SEVEN** — Israeli strikes kill Hamas internal
  security chief Naim Abu Nahal and six others.
- **ZAPORIZHZHIA STRIKE WOUNDS 48** — Russian overnight strike kills two
  and wounds 48, including four children.
- **NATO VOWS SPACE DEFENCE** — Rutte, asked about reports of a Russian
  nuclear satellite, pledges to keep allies safe.
- **ASIAN MARKETS RALLY** — Nikkei +3.91% and Kospi +6.32% as Huang's
  return revives the AI trade.
- **BRAZIL PASSES LULA'S $10BN FISCAL PACKAGE** — Lower house approves
  spending curbs; Lula to sign; more measures to follow.
- **CANDY FACTORY FIRE KILLS 26** — Indonesia confirms 26 dead in the
  Serang blaze; most died trying to reach the exit.
- **700,000+ RUSSIAN DEATHS ESTIMATED** — Leaked Rosstat data puts
  confirmed deaths near 490,000; toll likely far higher.
- **WALL ST SPLITS** — S&P -0.5%, Nasdaq -1.5%; Dow +0.9%, closing above
  50,000.
- **GERMANY TO USE UKRAINE'S DELTA** — Berlin signs a letter of intent
  for first access to the DELTA system.
- **UK SANCTIONS FIVE MYANMAR OFFICERS** — London acts after the ICJ
  genocide ruling; the president is not among those named.
- **STATES SUE MUSK FIRMS OVER GROK IMAGES** — Virginia and Oregon allege
  Grok's "spicy mode" made sexualised images of children.
- **KOREA TIGHTENS SCHOOL EXAMS** — Metal detectors and Wi-Fi shutdowns
  to catch AI cheating in school exams.
- **SINGAPORE KEEPS PROBING MEGASPEED** — PM Wong says the probe continues
  after the US blacklist over chip diversion.
- **ANTHROPIC FALLS BELOW IPO PRICE** — Shares -6.5% to $81.90, under the
  $83 float price.
- **CANADA REJECTS PENTAGON REBUKE** — "We don't report to the United
  States," McGuinty says after Monday's Pentagon memo.
- **TRUMP SIGNS DEATH PENALTY MEMO** — Order signed Monday widens federal
  death cases and seeks faster executions.
- **ANMER HALL BREAK-IN ARRESTS** — Two men arrested Tuesday after a
  suspected break-in at William and Kate's country home.
- **GIULIANI RECEIVES MEDAL OF FREEDOM** — Trump honours Giuliani in a
  private Oval Office ceremony.
- **ANALOG DEVICES SINKS 17%** — Record quarter, but mixed guidance after
  an earnings beat spooks investors.
- **MINES KILLED OR INJURED NEARLY 7,000 IN 2025** — Five-year high, the
  ICBL reports; Myanmar and Syria lead the toll.
- **INDIA PLEDGES $1.62BN FOR NEPAL REBUILD** — Grant plus energy credit
  line for reconstruction after August's floods.
- **DENMARK PLANS SCHOOL PHONE BAN FOR 2027** — Ministry proposes banning
  phones through 10th grade, citing classroom distraction.
- **TAIWAN'S DPP WARNS OF POLL INTERFERENCE** — DPP lawmakers accuse China
  of funding and flight deals ahead of Saturday's vote.
- **HOAX BOMB THREATS HIT SCHOOLS** — Hoax emails reach hundreds of
  schools in Germany and Denmark; police see no danger.
- **RIYADH TOWER ATTACK INJURES 11** — Houthi drone hits the PIF Tower
  for the second time in a week, officials say.
- **ZELENSKY URGES FOUR-WAY PEACE TALKS** — In a video address to NATO
  lawmakers in Berlin, he renews his NATO membership plea.
- **MERZ: 2008 NATO SNUB WAS A MISTAKE** — Germany's chancellor says
  withholding a membership path in 2008 was an error.
- **RUSSIAN JETS TRIGGER ISLAND ALERT** — Five warplanes near Ulleung
  Island; Seoul issues a first air-raid alert.

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

Verified locally (2026-11-25, v3): the image is 1024×1024 px, 171,337 bytes
(under the 1 MiB limit), and two runs produce byte-identical output
(sha256 `12f4342fb65ce4b236a49ee5abff6e0077643caec95a8214c9274dfac79f574d`).
The committed `entry.png.b64` (228,452 chars, no trailing newline) decodes
with `validate=True` to the same hash. Also verified as uid 65534 against a
root-owned output directory: exit 0, same hash. Legibility checked at 512 px:
the leads are immediately legible and grid headlines scan without zooming.

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124).
