def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# here we can flip the order of the arguments and it will still work
print_kwargs(power="lazer", name="shaktiman")
print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer", enemy = "Dr. Jackaal")