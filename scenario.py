import time
import customer as c
import dressing_rooms as d



class Scenario:
    def __init__(self,num_of_rooms, num_of_customers, 
                 num_of_items):
        self.num_of_rooms = num_of_rooms
        self.num_of_customers = num_of_customers
        self.num_of_items = num_of_items
        self.dressing_rooms = d.DressingRoom(num_of_rooms)
        self.customers = []


    def run(self):
        start_time = time.time()

        for i in range(self.num_of_customers):
            customer = c.Customer(i, self.num_of_items, 
                                self.dressing_rooms)
            self.customers.append(customer)
            customer.start()

        # Waiting for all customers
        for customer in self.customers:
            customer.join()

        end_time = time.time()
        elapsed = end_time - start_time

        avg_items = sum(customer.num_of_items for customer in self.customers) / len(self.customers)
        avg_usage = sum(self.dressing_rooms.usage_times) / len(self.dressing_rooms.usage_times)
        avg_wait = sum(self.dressing_rooms.wait_times) / len(self.dressing_rooms.wait_times)
        utilization = (sum(self.dressing_rooms.usage_times) / (self.num_of_rooms * elapsed)) * 100
        throughput = (self.num_of_customers / elapsed) * 60
        efficiency = (avg_usage / (avg_usage + avg_wait) * 100)
        
        print('\nConfiguration:')
        print(f'Number of rooms: {self.num_of_rooms}')
        print(f'Nummber of customers: {self.num_of_customers}')
        print(f'Number of items: {"Random" if self.num_of_items == 0 else self.num_of_items}\n')
        self.display_results(elapsed, avg_items, avg_usage, avg_wait, utilization, throughput, efficiency)
        

    def display_results(self, elapsed, avg_items, avg_usage, avg_wait, utilization, throughput, efficiency):

        
        print('Filler Unit I firgure It Out')
        if utilization:
            print(f'Utilization: {utilization:.2f}%')
        if throughput:
            print(f'Throughput: {throughput:.1f} customers per minute')
        if efficiency:
            print(f'Efficiency: {efficiency:.2f}%\n')

        
        print('Metrics:')
        if elapsed:
            print(f'Elapsed Time: {elapsed:.1f} seconds')
        if avg_items:
            print(f'Avg Items: {avg_items:.1f} items per customer')
        if avg_usage:
            print(f'Avg Usage: {avg_usage:.1f} minutes')
        if avg_wait:
            print(f'Avg Wait Time: {avg_wait:.1f} minutes')

        print('*' * 50)
        