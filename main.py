# import threading
#
#
# def func(a, b):
#     c = a + b
#     print(c)
#
#
# thread1 = threading.Thread(target=func, args=(3, 2))
# thread2 = threading.Thread(target=func, args=(10, 15))
#
#
# thread1.start()
# thread2.start()

############################################################

# import threading
#
#
# kirish = str(input("Enter matn -> "))
#
#
# def one():
#     l = []
#     for i in kirish:
#         if i.islower():
#             l.append(i)
#     print(*l)
#
#
# thread2 = threading.Thread(target=one)
#
# thread2.start()

############################################################

import threading
import time


def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Print Numbers: {i}")


def print_letters():
    for letter in "ABCDE":
        time.sleep(1)
        print(f"Print Letters: {letter}")


thread_numbers = threading.Thread(target=print_numbers())
thread_letters = threading.Thread(target=print_letters())


thread_numbers.start()
thread_letters.start()


# thread_numbers.join()
# thread_letters.join()

print("Barcha theardlar tugadi!")

