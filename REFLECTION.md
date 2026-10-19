# Part B: Reflection

### 1. How many tests did you write in Part A, and how many lines of production code? What is the ratio?

I wrote about 7 tests and 45 lines of code. The ratio is about 1 test for every 6.4 lines of code.

### 2. When was your bar red for the longest time, and why?

The multiplication test took the longest because I forgot to add the unit. I fixed it by using `grams(200)` instead of `Quantity(200)`.

### 3. Where did you use Fake It, Triangulate, and Obvious Implementation?

I used Fake It by returning 600. I used Triangulation by adding another test for 400. I used Obvious Implementation for unit conversion. All three methods helped me write the code step by step.

### 4. Which tasks remain on your test list?

I finished all the main tasks. Next, I would test invalid conversion rates and unknown units. I don't need extra features right now.

### 5. Would you have designed Quantity.reduce before coding?

Probably not. I didn't know I needed it until I started adding different units. TDD helped me find a better design.

### 6. How did Part 0 and Part A feel different?

Part 0 was easier because the code was already written. Part A was harder because I wrote tests first. The multiplication and unit conversion tests helped me design the code.