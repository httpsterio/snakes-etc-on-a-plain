# (THERE IS MOFFIN') SNAKES ETC. ON THIS (MOFFIN') PLAIN

![screenshot](https://github.com/httpsterio/snakes-etc-on-a-plain/blob/master/press/screenshot-intro.png?raw=true)

> _In This Already Anticipated (By FGJTurku) Epic Game, The Player Will Releases A Heroic Panicbound Kid Inside!_

Game made in 48* hours at Global Game Jam 2014, Jyväskylä.

[Global Game Jam entry page](https://v3.globalgamejam.org/2014/games/there-moffin-snakes-etc-moffin-plain-ex-kissat-ovat-mulkkuja-3)

---

## Team

* __Sami Mäkelä__
* __Jonne Harja__
* __Matti Kinnunen__
* __Jussi Lundelin__
* __Aleksi Pekkala__

## Run
`python game.py`

## Build action

The game can be built for Windows with the supplied action [.github/workflows/build.yml](.github/workflows/build.yml)


## Build locally

The game can also be built locally.

__Requirements__
- Python 2.7 32bit / 64bit
- pip 19.2.3 (recommended)
- py2exe 32bit
- pyglet 1.2

Python 2.7.18.msi, py2exe and pyglet whl files are supplied in ``src/python``. You can manually install the whl files with ``python -m pip install "src\python\filename.whl"`` as long as python 2.7.18 and pip is found in your path.

In the `src`-dir run:
 - `python setup.py install`
 - `python setup.py py2exe`

Run the game from `release/win32/snakes-etc-on-a-plain.exe`

## Description

In This Already Anticipated (By FGJTurku) Epic Game, The Player Will Releases A Heroic Panicbound Kid Inside!

In this highly polished a single computer co-operative game, you take role off two Snakes facing the perils of this mysterious world. As the world emotionlessly pushes forward these two snakes try poetically cope the struggles they face. With power of their imagination, they give each other unfamiliar powers they never imagined (?) before.

Play. Fail. Laugh. Challenge yourself and your (special) friend.


Critically Aclaimed!
_"When I was a child, I had a toy. It was small synthesizer, with such mumble buttons, but with nice colors it made beautiful noices of Cocks, Doges, Cows and other farm etc. animals... This is how I become familiar with farm animals and such... As a child that toy made my world more interesting and bright place... Also animal noices."_

__5/5__


_"I didn't have a clue what I was doing."_

__5/5__

\* A single game-breaking bug was fixed later. Also an installer was added, thanks to [Olli](https://github.com/gildean)
