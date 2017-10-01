# This will hold the Caching Class
"""
Author: Kyle Kubis
Created: 9/30/2017
Problem 2: Implement an LRU Cache
LRU caches are used to implement caches which do not grow indefinitely (the cache has a max size). When a new key is inserted that would overrun the size limit, the key which has not been accessed for the longest time is removed to make space.
The cache should support the following operations:

get(key): get the value of the key if it exists in the cache. Feel free to implement what happens when get(key) is called when key is not in the cache however you'd like.
put(key, value): update or insert the value if the key is not already present. If the insert would push the capacity over its max size, invalidate the least recently used item before inserting the new item.

Example:
cache = LRUCache(2) // max_size is 2
cache.put(1, "1")
cache.put(2, "2")
cache.get(1)            // returns 1
cache.put(3, "3")     // evicts key 2
cache.get(2)           // returns null because 2 was evicted
cache.put(4, "4")     // evicts key 1
cache.get(1)            // returns null
cache.get(3)           // returns "3"
cache.get(4)           // returns "4"



Preface, I will code this in a more efficient way and a pythonic way. and Time them. 
"""
class LRUCache(object):
	def __init__(self,max_size):
		"""
		The reason that I have a current_size variable instead of just 
		taking len(__keys), is this will be more efficient when you constantly have to 
		check for the length of the current cache #list/array
		Storying the values in a hash/dictionary.
		"""
		self.max_size = max_size
		self.current_size = 0
		self.__cache = {} # my hash
		self.__keys = [] # my queue

	def get(self,key):
		"""
		params: key
		if the key is in the list, then I pop it and insert it to the
		front
		else 
		return None
		"""
		if key in self.__keys:
			self.__keys.remove(key)
			self.__keys.insert(0,key)
		value = self.__cache.get(key,None)
		return value

	def put(self,key,value):
		"""
		params: key, value
		if the key is not in the list add it, verifying you have space.
		If no space, pop the last value in the list as well as removing it 
		from the hash
		else
		replace value in the list, pop and insert to front of list.
		"""
		if key not in self.__keys:
			if self.current_size < self.max_size:
				self.__keys.insert(0,key)
				self.__cache[key] = value
				self.current_size += 1
			else:
				del self.__cache[self.__keys.pop()]  # Here i pop and remove value from hash.
				self.__keys.insert(0,key)
				self.__cache[key] = value
		else:
			self.__cache[key] = value
			self.__keys.remove(key)
			self.__keys.insert(0,key)


def main():
	cache = LRUCache(2)  # max_size is 2
	print vars(cache)
	cache.put(1, "1")
	cache.put(2, "2")
	print cache.get(1)            # returns 1
	cache.put(3, "3")     # evicts key 2
	cache.get(2)           # returns null because 2 was evicted
	cache.put(4, "4")     # evicts key 1
	print cache.get(1)            # returns null
	print cache.get(3)           # returns "3"
	print cache.get(4)           # returns "4"
	print vars(cache)

if __name__ == '__main__':
	main()
