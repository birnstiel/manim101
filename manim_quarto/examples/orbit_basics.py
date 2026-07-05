"""OrbitBasics: a first astronomy-themed Manim scene.

Render with:
    manim -pql orbit_basics.py OrbitBasics

This example avoids LaTeX so it should work with a minimal Manim install.
"""

from manim import *
import numpy as np

config.background_color = "#0B1020"


class OrbitBasics(Scene):
    def construct(self):
        title = Text("Orbit from simple geometry", font_size=34)
        title.to_edge(UP)

        orbit_radius = 2.2
        angle = ValueTracker(0)  # <1>

        orbit = Circle(radius=orbit_radius, color="#6C7A89", stroke_width=2)
        sun = Dot(ORIGIN, radius=0.22, color="#FDB813")
        sun_glow = Circle(
            radius=0.38,
            color="#FDB813",
            stroke_width=6,
            stroke_opacity=0.25,
        )

        def planet_position():  # <2>
            a = angle.get_value()
            return orbit_radius * np.array([np.cos(a), np.sin(a), 0.0])

        planet = always_redraw(  # <3>
            lambda: Dot(point=planet_position(), radius=0.09, color="#6EC6FF")
        )
        radius_line = always_redraw(
            lambda: Line(ORIGIN, planet_position(),
                         color="#6EC6FF", stroke_width=2, stroke_opacity=0.55,
                         )
        )
        trail = TracedPath(planet.get_center,  # <4>
                           stroke_color="#6EC6FF", stroke_width=3)

        note = Text(
            "A ValueTracker drives the angle;\nobjects update every frame.",
            font_size=24,
            line_spacing=0.9,
        )
        note.to_corner(DL)

        self.play(Write(title))
        self.play(Create(orbit), FadeIn(sun_glow), FadeIn(sun))
        self.add(radius_line, trail, planet)
        self.play(
            angle.animate.set_value(TAU),  # <5>
            run_time=6, rate_func=linear)
        self.play(FadeIn(note, shift=UP * 0.2))
        self.wait()
