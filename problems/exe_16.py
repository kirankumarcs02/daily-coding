# This problem was asked by Twitter.
#
# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
#
# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log.
# i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible


class Order:
    def __init__(self, size):
        self.log = list()
        self.size = size

    def __repr__(self):
        return str(self.log)

    def record(self, order_id):
        self.log.append(order_id)
        if len(self.log) > self.size:
            self.log = self.log[1:]

    def get_last(self, i):
        return self.log[-i]

if __name__ == "__main__":
    logs = Order(5)
    logs.record(1)
    logs.record(2)
    print(logs.log)