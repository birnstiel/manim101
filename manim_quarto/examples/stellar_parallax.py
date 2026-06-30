"""StellarParallax: apparent motion of a nearby star against distant stars.

Render with:
    manim -pql stellar_parallax.py StellarParallax

This is a qualitative outreach visualization, not an astrometric model.
"""

from manim import *
import numpy as np

config.background_color = "#0B1020"


class StellarParallax(Scene):
    def construct(self):
        title = Text("Stellar parallax: nearby stars shift", font_size=34)
        title.to_edge(UP)

        rng = np.random.default_rng(4)
        background_stars = VGroup()
        for _ in range(95):
            x = rng.uniform(-6.3, 6.3)
            y = rng.uniform(-2.2, 2.7)
            r = rng.uniform(0.012, 0.032)
            opacity = rng.uniform(0.35, 0.9)
            background_stars.add(
                Dot(point=np.array([x, y, 0.0]), radius=r, color="#DDE7FF").set_opacity(opacity)
            )

        grid = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-3, 3, 1],
            background_line_style={
                "stroke_color": "#6C7A89",
                "stroke_width": 1,
                "stroke_opacity": 0.22,
            },
            axis_config={"stroke_opacity": 0},
        )
        grid.set_z_index(-2)

        theta = ValueTracker(0)
        base = np.array([0.0, 0.45, 0.0])

        def apparent_shift():
            return np.array(
                [0.72 * np.cos(theta.get_value()), 0.25 * np.sin(theta.get_value()), 0.0]
            )

        parallax_ellipse = Ellipse(width=1.44, height=0.50, color="#FDB813")
        parallax_ellipse.move_to(base).set_stroke(opacity=0.35, width=2)

        nearby_star = always_redraw(
            lambda: Dot(point=base + apparent_shift(), radius=0.09, color="#FDB813")
        )
        trail = TracedPath(nearby_star.get_center, stroke_color="#FDB813", stroke_width=3)

        earth_center = np.array([-3.5, -2.55, 0.0])
        earth_orbit = Ellipse(width=2.0, height=0.45, color="#6EC6FF")
        earth_orbit.move_to(earth_center).set_stroke(opacity=0.45, width=2)
        earth = always_redraw(
            lambda: Dot(
                point=earth_center
                + np.array(
                    [1.0 * np.cos(theta.get_value()), 0.225 * np.sin(theta.get_value()), 0.0]
                ),
                radius=0.07,
                color="#6EC6FF",
            )
        )

        labels = VGroup(
            Text("distant background", font_size=22).to_corner(UR),
            Text("nearby star", font_size=22, color="#FDB813").next_to(base, UP, buff=0.7),
            Text("Earth baseline", font_size=20, color="#6EC6FF").next_to(
                earth_orbit, DOWN
            ),
        )

        explanation = Text(
            "A tiny angular ellipse on the sky encodes distance.",
            font_size=24,
        )
        explanation.to_corner(DL)

        self.play(Write(title), FadeIn(grid), FadeIn(background_stars))
        self.play(FadeIn(parallax_ellipse), FadeIn(earth_orbit), FadeIn(labels))
        self.add(trail, nearby_star, earth)
        self.play(theta.animate.set_value(TAU), run_time=6, rate_func=linear)
        self.play(FadeIn(explanation, shift=UP * 0.2))
        self.wait()
