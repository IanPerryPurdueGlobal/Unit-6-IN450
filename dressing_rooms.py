import threading as t
import time

class DressingRoom:
     
    def __init__(self, num_of_rooms = 3):

        self.num_of_rooms = num_of_rooms
        
        self.semaphore = t.Semaphore(num_of_rooms)
        
        self.lock = t.Lock()
        
        self.wait_times = []


    def requestRoom(self):

        start_time = time.time()
        
        # blocks room from other customers until its available
        self.semaphore.acquire()
        wait_time = (time.time() - start_time)
        
        # records wait time safely
        with self.lock:
            self.wait_times.append(wait_time)
            print(self.wait_times)
        
        return wait_time
    

    def releaseRoom(self):
        # relases room to be used by other customers
        self.semaphore.release()


