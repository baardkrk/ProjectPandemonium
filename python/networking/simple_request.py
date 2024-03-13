import threading
import time

import requests



def foo():
    print('Foo is running...')
    a = requests.get('http://localhost:8080')
    print(f'Foo got result: {a}!')


def bar():
    print('Bar is running...')
    try:
        a = requests.get('http://localhost:8080/exception', timeout=0.1)
        print(f'Bar got result: {a}!')
    except Exception as e:
        print(f'Exception occurred: {e}')
    

class MyCls:
    def __init__(self):
        self._my_thread = None

    def do_request(self):
        if self._my_thread is not None and self._my_thread.is_alive():
            print('Thread was running!')
        else:
            self._my_thread = threading.Thread(target=foo)
            self._my_thread.start()

    def do_exception_request(self):
        if self._my_thread is not None and self._my_thread.is_alive():
            print('Thread was running!')
        else:
            self._my_thread = threading.Thread(target=bar)
            self._my_thread.start()
            

    
if __name__ == '__main__':

    mc = MyCls()
    mc.do_request()
    
    while mc._my_thread.is_alive():
        mc.do_request()
        time.sleep(0.3)
        
    print('Starting bar!')
    mc.do_exception_request()
    while mc._my_thread.is_alive():
        print('bar is alive!')
        time.sleep(0.3)

    print('Starting foo!')
    mc.do_request()
    while mc._my_thread.is_alive():
        print('foo is alive!')
        time.sleep(0.3)        
    print('Finished')
