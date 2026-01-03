Here's a simple Manim example of creating a circle:

```python
from manim import *

class Main(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        self.play(Create(circle))
        self.wait(1)
```

In this example, a blue circle with a radius of 1 is created and then displayed on the screen. The `Create` function is used to animate the circle's appearance, and `wait(1)` pauses the animation for 1 second.