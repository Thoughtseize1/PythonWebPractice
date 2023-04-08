"""The platform module lets you access the underlying platform's data, i.e., hardware, operating system, and interpreter version information.

There is a function that can show you all the underlying layers in one glance, named platform, too. It just returns a string describing the environment; thus, its output is rather addressed to humans than to automated processing (you'll see it soon).

This is how you can invoke it:"""

from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))

"""Sometimes, you may just want to know the generic name of the processor which runs your OS together with Python and your code - a function named machine() will tell you that. As previously, the function returns a string."""

from platform import machine

print(machine())


"""The processor() function returns a string filled with the real processor name (if possible).

Once again, we ran the sample program:"""
from platform import processor

print(processor())

"""The system function
A function named system() returns the generic OS name as a string."""
from platform import system

print(system())

"""If you need to know what version of Python is running your code, you can check it using a number of dedicated functions - here are two of them:

python_implementation() → returns a string denoting the Python implementation (expect CPython here, unless you decide to use any non-canonical Python branch)
python_version_tuple() → returns a three-element tuple filled with:
the major part of Python's version;
the minor part;
the patch level number."""
from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)

import platform

print(len(platform.python_version_tuple()))
