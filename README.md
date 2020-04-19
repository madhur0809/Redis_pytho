# Implementation of Redis

Redis ( https://en.wikipedia.org/wiki/Redis )
is a persistent key-value store which store some data, called a value, inside a key. The value can be retrieved
knowing the specific key .

## Objective

A working implementation of redis with some basic functionalities like

1. get ( https://redis.io/commands/get )
2. set ( https://redis.io/commands/set )
3. expire ( https://redis.io/commands/expire )
4. decr (https://redis.io/commands/decr)
4. incr ( https://redis.io/commands/incr)
5. decrby ( https://redis.io/commands/decrby)
6. incrby ( https://redis.io/commands/incrby)
7. getset ( https://redis.io/commands/getset)
8. getrange ( https://redis.io/commands/getrange)


### Prerequisites

Python  

SqliteDict : pip install -U sqlitedict

A lightweight wrapper around Python’s sqlite3 database with a simple, Pythonic dict-like interface and support for multi-thread access:

## Reason for Python chossing as language

=> Python provide SqliteDict  which gives key-value store in python for possibly 100-gb of data without client-server.

=> Python provide dictionaries which  are immensely flexible because they allow anything to be stored as a value, from primitive types     like strings and floats to more complicated types like objects and even other dictionaries.

=> Python provide sorted containers like sortedlist, sortedset, sorteddict.


## Running the test.py file


=> Run the test.py file using python test.py from terminal

=> Enter the command name with required inputs

=>eg. set saurabh 20


## Further improvements that can be made to make it efficient

=> In current version of this project get,sets functions works for single value string as input.Further improvements can be done to accept multi value string. eg. "This is hello wworld" .

=> In zadd() it is possible to add or update a single member per call.Accepting multiple elements can be included.

=>


## Data Structres Used

# Dictionary

# sorted set

