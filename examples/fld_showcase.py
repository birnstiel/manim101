from manim import *


class BetaToFLDEquation(Scene):
    def construct(self):
        # Optional: darker background for a more cinematic look
        self.camera.background_color = "#0b1020"

        title = Text("Flux-limited diffusion", font_size=34)
        title.to_edge(UP)
        title.set_color("#d7eaff")

        beta = MathTex(r"\beta", font_size=150)
        beta.set_color("#FDB813")

        equation = MathTex(
            r"\mathbf{F}",
            r"=",
            r"-",
            r"\frac{c\,\lambda}{\kappa_{\rm R}\rho}",
            r"\nabla E_{\rm rad}",
            font_size=54,
        )

        # Color individual pieces of the equation
        equation[0].set_color("#6EC6FF")   # flux
        equation[3].set_color("#8EF0D1")   # diffusion coefficient
        equation[4].set_color("#FDB813")   # radiation-energy gradient

        equation.move_to(ORIGIN)

        # Small explanatory labels
        flux_label = Text("radiative flux", font_size=20, color="#6EC6FF")
        flux_label.next_to(equation[0], DOWN, buff=0.45)

        limiter_label = Text("flux limiter", font_size=20, color="#8EF0D1")
        limiter_label.next_to(equation[3], UP, buff=0.35)

        gradient_label = Text("radiation energy gradient",
                              font_size=20, color="#FDB813")
        gradient_label.next_to(equation[4], DOWN, buff=0.45)

        labels = VGroup(flux_label, limiter_label, gradient_label)

        # Box around final equation
        box = SurroundingRectangle(
            equation,
            color="#6EC6FF",
            buff=0.28,
            corner_radius=0.12,
            stroke_width=3,
        )

        glow_box = SurroundingRectangle(
            equation,
            color="#6EC6FF",
            buff=0.34,
            corner_radius=0.15,
            stroke_width=10,
            stroke_opacity=0.18,
        )

        caption = Text(
            "A compact closure for radiation transport",
            font_size=24,
            color="#b8c7dd",
        )
        caption.next_to(box, DOWN, buff=0.65)

        # Animation sequence
        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.play(Write(beta), run_time=1.0)
        self.wait(0.4)

        # Transform beta into the equation
        self.play(
            Transform(beta, equation),
            run_time=1.6,
            rate_func=smooth,
        )

        # After Transform, beta now visually contains the equation.
        # Use equation itself from here on for easier highlighting.
        self.remove(beta)
        self.add(equation)

        self.play(
            LaggedStart(
                Indicate(equation[0], color="#6EC6FF", scale_factor=1.15),
                Indicate(equation[3], color="#8EF0D1", scale_factor=1.08),
                Indicate(equation[4], color="#FDB813", scale_factor=1.08),
                lag_ratio=0.25,
            ),
            run_time=2.0,
        )

        self.play(
            LaggedStart(
                FadeIn(flux_label, shift=UP * 0.15),
                FadeIn(limiter_label, shift=DOWN * 0.15),
                FadeIn(gradient_label, shift=UP * 0.15),
                lag_ratio=0.2,
            )
        )

        self.play(
            LaggedStart(
                FadeOut(flux_label, shift=DOWN * 0.15),
                FadeOut(limiter_label, shift=UP * 0.15),
                FadeOut(gradient_label, shift=DOWN * 0.15),
                lag_ratio=0.2,
            )
        )

        self.play(
            Create(glow_box),
            Create(box),
            run_time=1.0,
        )

        self.play(FadeIn(caption, shift=UP * 0.2))
        self.wait(2)
