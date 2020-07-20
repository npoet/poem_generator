### Random Poem Generator

Python 3.8 application that parses a set of grammatical rules from a text file and generates a random poem given the inputs. 

##### Usage:

Simply run the mainfile with ```python3 main.py```. There are no dependencies outside of the Python 3.8 std libraries. 
The script can be adjusted to write poems to a file or to the console.

##### Notes:

* Input data must be in .txt format under the /src/data dir. A sample file is included.
* This implementation may seem somewhat convoluted (because it is in some ways), as I was attemping to simultaneously demonstrate several applicable python skills while keeping with an OOP structure similar to approaches in Java or C#.

##### Future Implementation:

* Though one of the design goals pursued here was to use an object-oriented approach, this generator could be replaced
with a slightly more complicated recursive regex script (expanded on the mainfile).
