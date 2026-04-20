from environment import Environment

env = Environment(0, 0)
print("temp at alt 0 should be 288.15: ")
print(env.get_temperature(0))
print("temp at alt 11000 should be 216.65: ")
print(env.get_temperature(11000))
print("temp at alt 20000 should be 216.65: ")
print(env.get_temperature(20000))
print("temp at alt 32000 should be 228.65: ")
print(env.get_temperature(32000))
print("temp at alt 47000 should be 270.65: ")
print(env.get_temperature(47000))
print("temp at alt 51000 should be 270.65: ")
print(env.get_temperature(51000))
print("temp at alt 71000 should be 214.65: ")
print(env.get_temperature(71000))
print("temp at alt 84852 should be 186.95: ")
print(env.get_temperature(84852))


print(env.get_temperature(0)  )    # should be 288.15
print(env.get_temperature(11000))  # should be 216.65
print(env.get_pressure(0) )        # should be 101325
print(env.get_pressure(11000))     # should be ~22632
print(env.get_air_density(0)   )   # should be ~1.225