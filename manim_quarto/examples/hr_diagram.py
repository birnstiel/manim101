"""HRDiagram: a simple animated Hertzsprung-Russell diagram.

Render with:
    manim -pql hr_diagram.py HRDiagram

This uses stylized data points rather than an observational catalog.
"""

from manim import *
import numpy as np

config.background_color = "#0B1020"


def star_color(x: float) -> str:
    """Approximate visual color by location on the temperature axis."""
    if x < -0.9:
        return "#8CCBFF"  # hot, blue-white
    if x < 0.6:
        return "#FFF0B3"  # Sun-like
    return "#FFB36B"  # cool, orange-red


class HRDiagram(Scene):
    def construct(self):
        title = Text("Hertzsprung-Russell diagram", font_size=34)
        title.to_edge(UP)

        axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-4.2, 4.2, 2],
            x_length=7.2,
            y_length=4.6,
            tips=False,
            axis_config={"color": "#B0B8C4", "include_numbers": False},
        )
        axes.shift(DOWN * 0.15)

        x_label = Text("surface temperature: hotter <-  -> cooler", font_size=20)
        x_label.next_to(axes, DOWN, buff=0.25)
        y_label = Text("log luminosity", font_size=20).rotate(90 * DEGREES)
        y_label.next_to(axes, LEFT)

        def dot_at(x: float, y: float, color: str, radius: float = 0.045) -> Dot:
            return Dot(point=axes.c2p(x, y), radius=radius, color=color)

        xs = np.linspace(-2.15, 2.15, 20)
        main_sequence = VGroup(
            *[
                dot_at(x, -1.15 * x + 0.15 + 0.20 * np.sin(3 * x), star_color(x))
                for x in xs
            ]
        )

        red_giants = VGroup(
            *[
                dot_at(x, y, "#FF8A4C", radius=0.07)
                for x, y in [(1.0, 2.2), (1.35, 2.8), (1.65, 3.25), (2.0, 3.0)]
            ]
        )
        white_dwarfs = VGroup(
            *[
                dot_at(x, y, "#D7E9FF", radius=0.052)
                for x, y in [(-1.95, -3.0), (-1.55, -3.45), (-1.15, -3.2), (-0.8, -3.7)]
            ]
        )
        sun = dot_at(0.20, 0.0, "#FDB813", radius=0.075)

        labels = VGroup(
            Text("main sequence", font_size=22, color="#FFF0B3").move_to(axes.c2p(-0.55, 1.35)),
            Text("red giants", font_size=22, color="#FF8A4C").move_to(axes.c2p(1.65, 3.65)),
            Text("white dwarfs", font_size=22, color="#D7E9FF").move_to(axes.c2p(-1.55, -2.45)),
            Text("Sun", font_size=20, color="#FDB813").next_to(sun, RIGHT, buff=0.12),
        )

        note = Text(
            "The same pattern works for real catalogs:\nload arrays, map data to axes, animate the story.",
            font_size=23,
            line_spacing=0.9,
        )
        note.to_corner(DL)

        self.play(Write(title), Create(axes), Write(x_label), Write(y_label))
        self.play(LaggedStart(*[FadeIn(d) for d in main_sequence], lag_ratio=0.05), run_time=2)
        self.play(FadeIn(red_giants), FadeIn(white_dwarfs))
        self.play(FadeIn(sun), Write(labels))
        self.play(Indicate(sun, color="#FDB813"))
        self.play(FadeIn(note, shift=UP * 0.2))
        self.wait()
