from manimlib.imports import *
class divide_adic_test(Scene):
    def construct(self):
        nines = TextMobject("$\\overline{...999999}$")
        minus = TextMobject("-")
        ones = TextMobject("$\\overline{...111111}$")
        line = Polygon(np.array([-0.75, -0,5], [0.75, -0,5]), color=WHITE)
        result = TextMobject("...888888")
        comment = TextMobject("tl;dr: cursed number")
        nines.shift(1*UP)
        minus.shift(0.5*UP, 1.5*LEFT)
        self.play(Write(nines), Write(minus), Write(ones), ShowCreation(line))
        self.play(Write(result))
        self.wait(2)
        self.play(ReplacementTransform(ones, comment), Uncreate(nines), Uncreate(minus), Uncreate(line), Uncreate(result))
