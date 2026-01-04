Here's a simple example of how you can create a circle using the Manim library in Python:

```python
from manim import *

class Main(Scene):
    def construct(self):
        # Create a circle
        circle = Circle()

        # Add the circle to the scene
        self.play(Create(circle))

        # Wait for 1 second
        self.wait(1)
```

In this example, we first import the necessary modules from Manim. Then, we define a class `Main` that inherits from `Scene`. Inside the `construct` method, we create a `Circle` object and add it to the scene using the `Create` animation. Finally, we wait for 1 second using `self.wait(1)`.