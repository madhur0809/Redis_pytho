# Implementation of Redis

Redis ( https://en.wikipedia.org/wiki/Redis )
is a persistent key-value store which store some data, called a value, inside a key. The value can be retrieved
knowing the specific key .

## Objective

A working implementation of redis with some basic functionalities like

1. get ( https://redis.io/commands/get )
2. set ( https://redis.io/commands/set )
3. expire ( https://redis.io/commands/expire )
4. zadd ( https://redis.io/commands/zadd )
5. zrange ( https://redis.io/commands/zrange )
6. zrank  ( https://redis.io/commands/zrank )
7. decr ( https://redis.io/commands/decr )
8. incr ( https://redis.io/commands/incr ) 
9. decrby ( https://redis.io/commands/decrby )
10. incrby ( https://redis.io/commands/incrby )
11. getset ( https://redis.io/commands/getset )
12. getrange ( https://redis.io/commands/getrange )


### Prerequisites

Python  

SqliteDict : pip install -U sqlitedict

A lightweight wrapper around Python’s sqlite3 database with a simple, Pythonic dict-like interface and support for multi-thread access.

SortedContainers : pip install sortedcontainers

It is a collection of containers which allow us to insert and remove elements very efficiently while maintaining sorted order.

## Reason for Python chossing as language

=> Python provide SqliteDict  which gives key-value store in python for possibly 100-gb of data without client-server.

=> Python provide dictionaries which  are immensely flexible because they allow anything to be stored as a value, from primitive types     like strings and floats to more complicated types like objects and even other dictionaries.

=> Python provide sorted containers like sortedlist, sortedset, sorteddict.


## Running the test.py file


=> Run the test.py file using python test.py from terminal

=> Enter the command name with required inputs

=>eg. set saurabh 20

## Formats of important functions

1. expire(Value,expire start time ,time to live).

Note- While using set() start time and time to live is -1 and using expire() start time is current time of system ,time to live is given as input.

2. zadd(key,score,value)

3. zrange(key,start,end)

4. zrank(key,value)


## Further improvements that can be made to make it efficient

=> In current version of this project get,sets functions works for single value string as input.Further improvements can be done to accept multi value string. eg. "This is hello wworld" .

=> In zadd() it is possible to add or update a single member per call.Accepting multiple elements can be included.

=> In zrange() WITHSCORES parameter will be added.

=> To make persistent key value storage, SqliteDict is used.For more memory storage and to make more efficient ,database like            LevelDb can be used.


## Data Structres Used

=> Dictionary: Dictionaries are used to map a key to its associated value, where value can be a string, hash, set, sorted set or list.

=> Sorted set: Sorted sets are used to maintain ordered elements in zadd().Sorted sets provides fast inserting, removing, or getting ranges from the the middle of the list.

=> Tuple: Tuples are used to store score and member and they help in making sorted set of tuple.

=> Strings: string is a good idea in all the obvious scenarios where you want to store an HTML page, but also when you want to avoid converting your already encoded data. So for instance, if you have JSON or MessagePack you may just store objects as strings.  Strings is used as random access vectors with GETRANGE and SETRANGE.

## Threading

This implementation of redis is single threaded and SqliteDict supports multi-thred access.
