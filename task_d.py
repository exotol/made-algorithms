class Queue:
    
    def __init__(self):
        self.container = []
        self.head = 0
        
    def push(self, elem):
        self.container.append(elem)
        
    def pop_head(self):
        elem = self.container[self.head]
        self.head += 1
        return elem
    
    def pop_tail(self):
        return self.container.pop()
    
    def is_empty(self):
        return len(self.container) - self.head
    
    def clear(self):
        self.head = 0
        self.container[:] = []
    
    def front(self):
        return self.container[self.head]
    
    def size(self):
        return len(self.container) - self.head
    
    def before(self, num):
        return self.container.index(num) - self.head


def process_data(queue, raw_data):

    if len(raw_data) == 2:
        num_event, num = map(int, raw_data)
        if num_event == 1:
            queue.push(num)
        else:
            print(queue.before(num))
    else:
        num_event = int(raw_data[0])
        if num_event == 2:
            queue.pop_head()
        elif num_event == 3:
            queue.pop_tail()
        else:
            print(queue.front())
    

def solve():
    n_events = int(input())
    queue = Queue()
    for _ in range(n_events):
        raw_data = input().split()
        process_data(queue, raw_data)
        


if __name__ == "__main__":
    solve()