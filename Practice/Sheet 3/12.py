class Node:
    def __init__(self, elem, nxt):
        self.elem = elem
        self.next = nxt


class Queue:
    def __init__(self):
        self.front = None
        self.back = self.front

    def enqueue(self, obj):
        if self.front is None:
            node = Node(obj, None)
            self.front = node
            self.back = self.front
        else:
            node = Node(obj, None)
            self.back.next = node
            self.back = self.back.next

    def dequeue(self):
        if self.front is None:
            print("Underflow!!")
        else:
            dequeued = self.front.elem
            self.front = self.front.next
            return dequeued

    def peek(self):
        if self.front is None:
            print("Underflow!!")
        else:
            return self.front.elem

    def is_empty(self):
        return self.front is None


# def time_line(line, k):
#     """
#     1. Initialize time taken
#     2. Initialize que and fill it up with the line
#     3. Until the kth positions time is zero we iterate and go through the counter
#     :param line: A list of tickets that people wants to but
#     :param k: an int which denotes the position of the guy we want to calculate the time
#     :return: Time taken to buy the tickets of kth positions guy
#     """
#     time_taken = 0
#     que = Queue()
#     for person in line:
#         que.enqueue(person)
#     count = 0
#     k_th_time = line[k]
#     len_line = len(line)
#     while k_th_time > 0:
#         dequeued = que.dequeue()
#         if dequeued > 0:
#             dequeued -= 1
#             time_taken += 1
#             if count == k:
#                 k_th_time -= 1
#         que.enqueue(dequeued)
#         count = (count + 1) % len_line
#
#     return time_taken
#
#
# print(time_line([1, 2, 3], 1))


def time_line(line, k):
    """
    Calculate the time taken to buy the tickets of the k-th person in the line.

    Args:
        line (list): A list of tickets that people want to buy.
        k (int): The position of the person whose time is to be calculated.

    Returns:
        int: Time taken to buy the tickets of the k-th person.

    """
    time_taken = 0
    que = Queue()

    # Fill up the queue with people in the line
    for person in line:
        que.enqueue(person)

    count = 0
    k_th_time = line[k]
    len_line = len(line)

    # Continue processing until the k-th person's time becomes zero
    while k_th_time > 0:
        dequeued = que.dequeue()

        if dequeued > 0:
            dequeued -= 1
            time_taken += 1

            # If the current person being processed is the k-th person, decrement its time
            if count == k:
                k_th_time -= 1

        que.enqueue(dequeued)
        count = (count + 1) % len_line

    return time_taken


print(time_line([1, 2, 3], 1))
