"""ExoplanetTransit: animate a planet crossing a star and the light curve.

Render with:
    manim -pql exoplanet_transit.py ExoplanetTransit

The transit depth function is deliberately simple for teaching purposes.
"""

from manim import *
import numpy as np

config.background_color = "#0B1020"

p = 0.22
STAR_RADIUS = 1.0
PATH_SCALE = 1.65


def relative_flux(phase: float) -> float:
    """Toy transit with contact timing and a flat-bottom full-overlap phase."""
    depth = 0.026

    # Same geometry as the animation: planet x-position = PATH_SCALE * phase.
    x_sep = abs(PATH_SCALE * phase)
    contact_sep = STAR_RADIUS + p
    full_overlap_sep = STAR_RADIUS - p

    # Outside contact there is no flux drop.
    if x_sep >= contact_sep:
        return 1.0

    # Fully in front of the stellar disk -> flat-bottom transit.
    if x_sep <= full_overlap_sep:
        return 1.0 - depth

    # In ingress/egress transition, blend smoothly between depth and baseline.
    s = (x_sep - full_overlap_sep) / (contact_sep - full_overlap_sep)
    smoothstep = 3 * s**2 - 2 * s**3

    return 1.0 - depth * (1.0 - smoothstep)


class ExoplanetTransit(Scene):
    def construct(self):
        title = Text(
            "Exoplanet transit: geometry -> light curve", font_size=32)
        title.to_edge(UP)

        phase = ValueTracker(-1.15)

        star = Circle(
            radius=1.0,
            color="#FDB813",
            fill_color="#FDB813",
            fill_opacity=1.0,
            stroke_width=0,
        )
        star.shift(UP * 1.25 + LEFT * 2.5)
        star_label = Text("star", font_size=22).next_to(star, DOWN)

        planet = always_redraw(
            lambda: Circle(
                radius=0.22,
                color="#D1D5DB",
                fill_color="#111827",
                fill_opacity=1.0,
                stroke_width=1.2,
            ).move_to(star.get_center() + RIGHT * (PATH_SCALE * phase.get_value()))
        )
        planet_label = Text("planet", font_size=22).next_to(
            star, RIGHT, buff=1.15)

        axes = Axes(
            x_range=[-1.2, 1.2, 0.4],
            y_range=[0.965, 1.005, 0.01],
            x_length=6.4,
            y_length=2.5,
            tips=False,
            axis_config={"color": "#B0B8C4", "include_numbers": False},
        )
        axes.to_corner(DR).shift(LEFT * 0.2 + UP * 0.1)

        curve = axes.plot(
            relative_flux,
            x_range=[-1.15, 1.15, 0.01],
            color="#6EC6FF",
            stroke_width=4,
        )
        moving_point = always_redraw(
            lambda: Dot(
                point=axes.c2p(phase.get_value(),
                               relative_flux(phase.get_value())),
                radius=0.055,
                color="#FFFFFF",
            )
        )

        x_label = Text("orbital phase", font_size=20).next_to(axes, DOWN)
        y_label = Text("relative flux", font_size=20).rotate(90 * DEGREES)
        y_label.next_to(axes, LEFT)

        explanation = Text(
            "When the planet overlaps the stellar disk,\nwe draw the same dip on the plot.",
            font_size=23,
            line_spacing=0.9,
        )
        explanation.to_corner(DL)

        self.play(Write(title))
        self.play(FadeIn(star), FadeIn(star_label), FadeIn(planet_label))
        self.play(Create(axes), Write(x_label), Write(y_label), Create(curve))
        self.add(planet, moving_point)
        self.play(phase.animate.set_value(1.15), run_time=6, rate_func=linear)
        self.play(FadeIn(explanation, shift=UP * 0.2))
        self.wait()
