from manim import *
from numpy import genfromtxt

rad = 0.02
ratio = 1/8
repeat = 4

all_point = set()


def lerp(v1, v2, d):
    r1 = v1[0] * (1 - d) + v2[0] * d
    r2 = v1[1] * (1 - d) + v2[1] * d
    r3 = v1[2] * (1 - d) + v2[2] * d
    return (r1, r2, r3)


class ChaosGame(Scene):
    def construct(self):
        self.wait()

        # init point
        init_point = genfromtxt('init point.csv', delimiter=',')
        for i in init_point:
            dot = Dot(color=GREEN, radius=0.1).move_to(i)
            all_point.add(tuple(i))
            self.add(dot)

        self.wait()

        for i in range(repeat):
            temp = set()

            for d in all_point:
                for j in range(len(init_point)):
                    new_point = lerp(d, init_point[j], ratio)
                    temp.add(tuple(new_point))

            for count, m in enumerate(temp):
                if(count % 100 == 0):
                    print(i, " : ", count  , " : ", len(temp), end="\r")
                all_point.add(tuple(m))
                dot = Dot(radius=rad).move_to((m))
                self.add(dot)

            self.wait()

        self.wait()
