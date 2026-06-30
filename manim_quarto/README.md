# Code Coffee: Manim for Astronomy

Quarto version of the Manim seminar deck plus example scripts.

## Preview / render the slides

```bash
quarto preview manim.qmd
# or
quarto render manim.qmd
```

This produces a Reveal.js HTML slide deck inside the Quarto website project.

## Run the Manim examples

Install Manim in a local project environment, then from this folder:

```bash
cd examples
manim -pql orbit_basics.py OrbitBasics
manim -pql exoplanet_transit.py ExoplanetTransit
manim -pql stellar_parallax.py StellarParallax
manim -pql hr_diagram.py HRDiagram
```

For a quick batch render:

```bash
cd examples
bash render_all_examples.sh
```
