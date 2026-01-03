Here's a simple example of how you can create a circle using the Manim library:

```python
from manim import *

class Main(Scene):
    def construct(self):
        # Create a circle
        circle = Circle(radius=1, color=BLUE, fill_opacity=0.5)

        # Add the circle to the scene
        self.play(Create(circle))

        # Wait for 1 second
        self.wait(1)
```

In this example, a blue circle with a radius of 1 is created and added to the scene. The `Create` animation is used to animate the appearance of the circle. The scene waits for 1 second before ending.