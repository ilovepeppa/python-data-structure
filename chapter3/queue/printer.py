import random
from myQueue import Queue


class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        return self.current_task is not None

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() / self.page_rate * 60


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


def new_print_task():
    return random.randrange(1, 91) == 90


def simulation(num_seconds, pages_per_minute):
    printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if not printer.busy() and not print_queue.is_empty():
            task = print_queue.dequeue()
            waiting_times.append(task.wait_time(current_second))
            printer.start_next(task)

        printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print('Average wait %6.2f secs %3d tasks remaining.' % (average_wait, print_queue.size()))


for i in range(10):
    simulation(3600, 10)
