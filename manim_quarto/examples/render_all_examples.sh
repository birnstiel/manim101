#!/usr/bin/env bash
set -euo pipefail

# From inside this examples directory, render fast preview versions.
manim -pql orbit_basics.py OrbitBasics
manim -pql exoplanet_transit.py ExoplanetTransit
manim -pql stellar_parallax.py StellarParallax
manim -pql hr_diagram.py HRDiagram
