import random

number_list = [random.randint(1, 10) for times in range(100)]

print(f"Total elements:", len(number_list))
print(f"Sum:", sum(number_list))
print(f"Average:", sum(number_list) / len(number_list))