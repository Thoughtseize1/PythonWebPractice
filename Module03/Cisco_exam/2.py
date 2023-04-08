from random import random, seed

"""The seed() function is able to directly set the generator's seed. We'll show you two of its variants:

🔶 seed() - sets the seed with the current time;
🔶 seed(int_value) - sets the seed with the integer value int_value.
We've modified the previous program - in effect, we've removed any trace of randomness from the code:"""

for i in range(5):
    print(random())
