import threading as t
import time

class DressingRoom:
     
    def __init__(self, num_of_rooms = 3):

        self.num_of_rooms = num_of_rooms
        self.semaphore = t.Semaphore(num_of_rooms)
        self.lock = t.Lock()
        self.wait_times = []
        self.usage_times = []
        self.customer_record = {}

    def recordMetrics(self,metric_type,metric):
        with self.lock:
            if metric_type == 'wait_time':
                self.wait_times.append(metric)
            if metric_type == 'usage_time':
                self.usage_times.append(metric)
    
    def recordCustomerData(self,customer_id, metric_type, metric):
        with self.lock:
            if customer_id not in self.customer_record:
                self.customer_record[customer_id] = {}
            self.customer_record[customer_id][metric_type] = metric 

           

    def requestRoom(self):

        start_time = time.time()
        
        # blocks room from other customers until its available
        self.semaphore.acquire()
        wait_time = (time.time() - start_time)
        
        return wait_time
    

    def releaseRoom(self):
        # relases room to be used by other customers
        self.semaphore.release()


