"""StellarParallax: apparent motion of a nearby star against distant stars.

Render with:
    manim -pql stellar_parallax.py StellarParallax

This is a qualitative outreach visualization, not an astrometric model.
"""

from manim import VGroup, Scene, Dot, Line, ValueTracker, always_redraw, config
from manim import UL, RIGHT, DOWN, LEFT, UP, linear
import numpy as np
import random

config.background_color = "#0B1020"


class StellarParallax(Scene):
    def construct(self):
        random.seed(3)
        timer = ValueTracker(0)
        stars = VGroup()
        inc = ValueTracker(0)

        # add angle indicator
        corner = Dot().to_corner(UL).shift(RIGHT * 0.7 + DOWN * 0.7).get_center()
        length = 0.5
        line1 = Line(corner, corner + length * RIGHT)
        line2 = always_redraw(lambda: Line(
            corner, corner + length * (np.cos(inc.get_value()) * RIGHT + np.sin(inc.get_value()) * UP)))
        self.add(line1, line2)

        for _ in range(120):
            # Random starting position
            x = random.uniform(-7, 7)
            y = random.uniform(-4, 4)

            # Random "depth": small = far, large = near
            depth = random.uniform(0.1, 0.5)
            star = Dot(point=[x, y, 0], radius=0.015 + 0.025 * depth)
            start = star.get_center()

            # Each star follows the same tracker, but nearby stars move more.
            star.add_updater(
                lambda mob, start=start, depth=depth: mob.move_to(
                    start + depth * LEFT * np.sin(timer.get_value()) +
                    depth * np.sin(inc.get_value()) * UP *
                    np.cos(timer.get_value())
                )
            )
            stars.add(star)

        self.add(stars)

        self.play(
            timer.animate.set_value(20 * np.pi),
            inc.animate.set_value(np.deg2rad(90)),
            run_time=12,
            rate_func=linear
        )

        self.wait()
