import time

# Write your code below 👇
def speed_calc_decorator(func):
  def wrapper():
      start_time = time.time()
      func()
      end_time = time.time()
      execution_time = end_time - start_time
      print(f"{func.__name__} run speed: {execution_time}s")
  return wrapper


@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        

@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i
    

current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

fast_function()
slow_function()
