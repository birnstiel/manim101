# Code Coffee: Manim for Astronomy

Quarto Slides for the seminar on `Manim` plus example scripts.

## Preview or render the slides

This requires `quarto`. If you installed the environment below it should exist
there. You can preview or render the slides with

```bash
cd manim_quarto
quarto preview manim.qmd
# or
quarto render manim.qmd
```

This produces a Reveal.js HTML slide deck inside the Quarto website project.

When pushing to github, this should trigger a rebuild of the public website
(even in repo is private). This can also be done locally with
`quarto publish gh-pages`.

## Installation & the Manim environment

You can find details in the
[manim documentation]([manim](https://docs.manim.community/en/stable/installation.html)).

I used [pixi](birnstiel.github.io/pixi101) with the environment specification in
the `manim_env` folder. To do the same, follow these steps:

```bash
# install pixi if you don't have it yet
curl -fsSL https://pixi.sh/install.sh | sh

# go into the environment folder. The `pixi.toml` contains
# the required packages.
cd manim_env

# install the environment, should take <1 minute
pixi install

# ---EITHER--- activate the environment in the shell
pixi shell

# and run manim from there or start the jupyter lab from
# within this shell, e.g.
# > manim -pql ../manim_quarto/examples/orbit_basics.py
# > jupyter lab
...

# ---OR--- ask pixi to install this environment as a jupyter
# kernel, then you should be able to  select this environment
# in our jupyter lab or VS Code (called "Pixi (manim_env)")
pixi run install_kernel
```

if you want to remove the environment, just

```bash
# in the manim_env folder
pixi clean

# if you installed the kernel, you can remove it with
jupyter kernelspec remove pixi-manim_env
```

## Run the Manim examples

From the `manim_quarto/examples` folder, you can run the example python scripts:

```bash
manim -pql orbit_basics.py OrbitBasics
manim -pql exoplanet_transit.py ExoplanetTransit
manim -pql stellar_parallax.py StellarParallax
```
