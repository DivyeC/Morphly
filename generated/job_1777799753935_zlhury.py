from manim import *

class Main(Scene):
    def construct(self):
        cat = ImageMobject("cat.png")
        cat.scale(0.5)
        self.play(Create(cat))
```

Replace "cat.png" with the path to your cat image file.