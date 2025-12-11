# geek
Real wrlld application of math concepts 
#FINDING HOW MANY UNIT YOU NEED GIVEN ALL THE AVAILABLE RESOURCES
Let's say a company produces products N1, N2 from resources R1, R2. To produce a unit of product x1 and x2 and the available resources are b1 = 8 and b2 = 11

Resource consumption matrix

                      N1                 N2
R1                    2                  1
R2                    1                  3

Available resources:
b1 = 8
b2 = 11

we can simply this using equations
  2(x1) + x2 = 8
   x1 + 3(x2) = 11

we can use matrices to solve this problem. They come in handy especially when the extremely big and bulky. This will just show how to handle such instances.

we know that to solve for the units x1,x2 we will have to multiply the inverse of the consumption matrix and the available resources
