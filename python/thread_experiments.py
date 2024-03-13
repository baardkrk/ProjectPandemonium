"""
Some experiments exploring threading in python
"""

import threading
import time
from dataclasses import dataclass, field

"""                          
Experiment 1
Normal callbacks
=======================================================================
"""

@dataclass
class Foo:
    name: str
    age: int
    lock: threading.Lock = field(init=False, default_factory=threading.Lock)    


def my_callback_a(a: Foo):
    a.lock.acquire()
    print(a.name, a.age)
    a.lock.release()


def my_callback_b(b: Foo, new_name: str, sleep_time: int=2):
    print('updating name!')
    b.lock.acquire()
    time.sleep(sleep_time)
    b.name = new_name
    print(f'updated name to {new_name}')
    b.lock.release()


def experiment_1():
    foo = Foo("John", 32)
    a = threading.Thread(target=my_callback_a, args=[foo])
    b = threading.Thread(target=my_callback_b, args=[foo, "Doe"])
    c = threading.Thread(target=my_callback_a, args=[foo])
    d = threading.Thread(target=my_callback_b, args=[foo, "JANE", 1])
    e = threading.Thread(target=my_callback_a, args=[foo])
    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    time.sleep(2)
    my_callback_a(foo)
    print('Hello!')
    # Am allowed to read a locked object
    # [False, True, True, False, False]
    # [0, 1, 1, 0, 0] -> 

"""                          
Experiment 2
Failing threads
=======================================================================
"""

def a_function():
    print('Hello')
    time.sleep(2)
    print('Goodbye!')
    

def failing_function():
    raise Exception('Ooops!')


def experiment_2():
    """What if a thread fails?"""
    thread_a = threading.Thread(target=a_function)
    thread_b = threading.Thread(target=failing_function)

    print(f'Is thread_b running? {thread_b.is_alive()}')
    thread_a.start()
    thread_b.start()
    print(f'Is thread_b running? {thread_b.is_alive()}') 
    while thread_b.is_alive():
        print(f'Is thread_b running? {thread_b.is_alive()}')

    print(f'Is thread_b running? {thread_b.is_alive()}')
    thread_a.join()
    thread_b.join()

    print(f'Is thread_b running? {thread_b.is_alive()}')
    print('Done!')


"""                          
Experiment 3
Many threads
=======================================================================
"""

def foo(t: int = 0, a: str = 'a'):
    print(f'Foo ({t}, {a}) is running...')
    time.sleep(1)
    print(f'Foo ({t}, {a}) is done!')

def bar():
    print('Bar is running...')
    time.sleep(2)
    print('Bar is done!')


def check_alive(t: threading.Thread, n: str=None):
    name = n if n is not None else t
    if t.is_alive():
        print(f'{name} was alive!')
    else:
        print(f'{name} is dead.')


def experiment_3():
    foo_thread = threading.Thread(target=foo)
    bar_thread = threading.Thread(target=bar)

    check_alive(bar_thread, 'bar')
    start = time.time()
    foo_thread.start()
    bar_thread.start()
    while bar_thread.is_alive():
        check_alive(bar_thread, 'bar')
        # foo_thread.join()
        time.sleep(0.3)
    # foo_thread.join()
    # bar_thread.join()
    check_alive(bar_thread, 'bar')
    end = time.time()
    print(f'Finished, took {end-start} seconds.')

    # Testing many threads
    ts = range(0, 26)
    threads = [ threading.Thread(target=foo, args=[i, chr(ord('a')+i)]) for i in ts ]
    [ t.start() for t in threads ]
    [ t.join() for t in threads ]
    print('All threads finished!')

    
if __name__ == '__main__':
    experiment_1()
    experiment_2()
    experiment_3()
