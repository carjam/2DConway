#from https://stackoverflow.com/questions/3620943/measuring-elapsed-time-with-the-time-module
import time
import functools

class profile(object):
	def __init__(self, func):
		self.func = func
		self.cache = {}
		self.oInstance = object#Cls(*args,**kwargs)


	def __call__(self, *args, **kwargs):
		@functools.wraps(self.func)
		def with_profiling(*args, **kwargs):
			start_time = time.perf_counter() 

			ret = self.func(*args, **kwargs)

			elapsed_time = time.perf_counter() - start_time

			if self.func.__name__ not in self.cache:
				self.cache[self.func.__name__] = [0, []]
			self.cache[self.func.__name__][0] += 1
			self.cache[self.func.__name__][1].append(elapsed_time)

			self.print_prof_data()
			return ret

		return with_profiling(*args,**kwargs)

	def __get__(self, obj, objtype):
		'''Support instance methods.'''
		return functools.partial(self.__call__, obj)

	def print_prof_data(self):
		for fname, data in self.cache.items():
			max_time = max(data[1])
			avg_time = sum(data[1]) / len(data[1])
			#print("Function %s called %d times. " % (fname, data[0]))
			#print('Execution time max: %.5f, average: %.5f' % (max_time, avg_time))
			print("\n"+self.func.__name__+" Execution time: %.5f.\n" % (max_time))
			

	def clear_prof_data(self):
		self.cache
		self.cache = {}

@profile
def main():
	print('this is a test')
	time.sleep(0.7)
	print('finished')

if __name__ == "__main__":
	main()