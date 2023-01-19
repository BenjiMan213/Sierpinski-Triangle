# Sierpinsky-Triangle
Generating and visualizing a famous fractal called the Sierpinsky Triangle using pygame.

The Sierpinsky Triangle is a fractal that can be represented in the overall shape of an equilateral triangle. The area of this triangle sums to 0.
That is because there are an infinite number of "holes" in this triangle.
Imagine a triangle having 4 sub triangles inside it, with the center triangle's base being flipped relative to the others. The triangle is formed
by removing this central sub triangle and recursively removing every central sub triangle inside each of the remaining sub triangles.

In this demonstration of a Sierpinsky triangle, we create the fractal by starting with just the three corners of our largest triangle.
1) We then place a dot randomly inside the bounds of this triangle.
2) Then we place another dot at the midpoint of the dot we placed and a randomly selected corner of the triangle.
We then repeat step 2 using the dot that was placed last to find where to place our new dot.
If we repeat this process, placing many dots, the Sierpinsky Triangle emerges.

It is quite amazing to see order seemingly rise out of randomly placing dots.
