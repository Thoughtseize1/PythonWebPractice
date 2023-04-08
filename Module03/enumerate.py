names = ["Bob", "Alice", "Guido"]

names_in_dict = {"EE": "Bob", "KEY1": "Pidor", "1212": "Suka"}

# for index, value in enumerate(names):
#     print(f"Index: {index}. Value: {value}")

for index, value in names_in_dict.items():
    print(f"Index: {index}. Value: {value}")

x = input()
y = int(input())

print(x * y)
