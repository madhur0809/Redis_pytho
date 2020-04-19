import time
from sortedcontainers import SortedList, SortedSet, SortedDict 
from sqlitedict import SqliteDict
mydict = SqliteDict('./my_db.sqlite', autocommit=True)

# print(time.time())

def get_key(key):
	if key in mydict:
		if mydict[key][2] != -1:
			if abs(int(time.time())-mydict[key][1]) > mydict[key][2]:
				del mydict[key]
				get_key(key)
			else:
				print(mydict[key][0])
		else:
			print(mydict[key][0])
	else:
		print("(nil)")

def set_key(key, value):
	print(key, value)
	mydict[key] = [value, -1,-1]

def expire_key(key, ttl):
	if key in mydict:
		mydict[key] = [mydict[key][0], int(time.time()), int(ttl)]
		print(1)
	else:
		print(0)

def zadd(key, score, value):
	if key not in mydict:
		mydict[key] = SortedDict({score: value})
	else:
		sd = mydict[key]
		sd[score] = value
		mydict[key] = sd

def zrange(key, start, end):
	if key in mydict:
		size = len(mydict[key])
		i = 0
		start = start%size
		end = end%size
		for k in mydict[key]:
			if i >= start and i<= end:
				print(k, " --> ", mydict[key][k])
			i = i + 1
	else:
		print("(nil)")

def zrank(key, rank):
	ans = "(nil)"
	if key not in mydict:
		print(ans)
	else:
		i = 1
		for k in mydict[key]:
			if mydict[key][k] == rank:
				ans = i
				break
			i = i + 1
		print(ans)

def decr_key(key):
	if key in mydict:
		mydict[key]=str(int(mydict[key])-1)
		print(mydict[key])
	else:
		mydict[key]=0

def incr_key(key):
	if key in mydict:
		mydict[key]=str(int(mydict[key])+1)
		print(mydict[key])
	else:
		mydict[key]=0

def incrby_key(key,value):
	if key in mydict:
		mydict[key]=str(int(mydict[key])+int(value))
		print(mydict[key])
	else:
		mydict[key]=0

def decrby_key(key,value):
	if key in mydict:
		mydict[key]=str(int(mydict[key])-int(value))
		print(mydict[key])
	else:
		mydict[key]=0

def getset_key(key,value):
	if key in mydict:
		print(mydict[key])
		mydict[key]=value
		
	else:
		print("(nil)")

def getrange(key,first,second):
	if key in mydict:
		s=mydict[key]
		print(s[int(first):int(second)+1])
	else:
		print("(nil)")

def main():
    while True:
        command1 = input("myredis> ")
        command = command1.split()
        command[0] = command[0].lower()
        if command[0] == "exit":
            break
        elif command[0] == "help":
            print("psh: a simple shell written in Python")
        elif command[0] == "get":
        	get_key(command[1])
        elif command[0] == "set":
        	set_key(command[1], command[2])
        elif command[0] == "expire":
        	expire_key(command[1], command[2])
        elif command[0] == "zadd":
        	zadd(command[1], command[2], command[3])
        elif command[0] == "zrange":
        	zrange(command[1], int(command[2]), int(command[3]))
        elif command[0] == "zrank":
        	zrank(command[1], command[2])
        elif command[0] == "decr":
        	decr_key(command[1])
        elif command[0] == "incr":
        	incr_key(command[1])
        elif command[0] == "incrby":
        	incrby_key(command[1],command[2])
        elif command[0] == "decrby":
        	decrby_key(command[1],command[2])
        elif command[0] == "getset":
        	getset_key(command[1],command[2])
        elif command[0] == "getrange":
        	getrange(command[1],command[2],command[3])
        else:
            print("Type commands which are given")

main()