import threading as t
from random import randint
from time import sleep

class Customer(t.Thread):
    
    def __init__(self,customer_id, num_of_items, dressing_rooms):
        t.Thread.__init__(self)
        self.customer_id = customer_id
        self.num_of_items = num_of_items
        self.dressing_rooms = dressing_rooms

        if num_of_items == 0:
            self.num_of_items = randint(1, 6)
        else:
            self.num_of_items = min(num_of_items, 6)
            
    
    def run(self):
        #request room
        wait_time = self.dressing_rooms.requestRoom()

        # try on items
        total_time = 0
        for i in range(self.num_of_items):
            try_time = randint(1, 3) * 60
            sleep(try_time / 60)
            total_time += try_time

        #store results
        self.wait_time = wait_time
        self.usage_time = (total_time /60)

        self.dressing_rooms.recordMetrics('wait_time', self.wait_time)
        self.dressing_rooms.recordMetrics('usage_time', self.usage_time)
        self.dressing_rooms.recordCustomerData(self.customer_id, metric_type =' wait_time', metric = (self.wait_time))
        self.dressing_rooms.recordCustomerData(self.customer_id, metric_type =' usage_time', metric = (self.usage_time))
        self.dressing_rooms.recordCustomerData(self.customer_id, metric_type =' items', metric = self.num_of_items)
        self.dressing_rooms.releaseRoom()
