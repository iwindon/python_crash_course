from time import monotonic


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
last_owned = motorcycles.pop()
first_owned = motorcycles.pop(0)
print(f"The last motocycle I owned was a {last_owned.title()}")
print(f"The first motocycle I owned was a {first_owned.title()}")

