### Random Poem Generator

Python 3.8 application that parses a set of grammatical rules from a text file and generates a random poem given the inputs. 

##### Usage:

Simply run the mainfile with ```python3 main.py```. There are no dependencies outside of the Python 3.8 std libraries. 
The script can be adjusted to write poems to a file or to the console.

##### Notes:

* Input data must be in .txt format under the /src/data dir. A sample file is included.

##### Future Implementation:

* A new "Word" wrapper class should abstract re-implemented funcs common to sentence elements.
* Though one of the design goals pursued here was to use an object-oriented approach, this generator could be replaced
with a regex script (expanded on the mainfile)
