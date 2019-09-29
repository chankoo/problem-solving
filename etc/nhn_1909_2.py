# 19.09.29
# 빈도수 우선 큐

import sys
from collections import deque

class FreqPriorityQueue(object):
    def __init__(self):
        self.q = deque()
        self.fq_dict = {}
        self.output = []
    
    def print_q(self):
        for num in self.output:
            print(num, end=' ')

    def enqueue(self, num):
        self.q.append(num)
        
        if num not in self.fq_dict:
            self.fq_dict[num] = 1
        else:
            self.fq_dict[num] += 1

    def get_sorted_freq_list(self):
        return sorted(self.fq_dict.items(), key=lambda kv:kv[1], reverse=True)

    def is_q_empty(self):
        return len(self.q) == 0

    def dequeue(self):
        if self.is_q_empty():
            return -1
            
        sorted_by_freq = self.get_sorted_freq_list()
        most_freq_val = sorted_by_freq[0][1]
        most_freq_keys = [sorted_by_freq[0][0], ]
            
        for key, val in sorted_by_freq[1:]:
            if val == most_freq_val:
                most_freq_keys.append(key)
                continue
            break

        if len(most_freq_keys) == 1:
            key_to_rm = most_freq_keys[0]
            self.q.remove(key_to_rm)

        else:
            key_to_rm = None
            for key in self.q:
                if key in most_freq_keys:
                    key_to_rm = key
                    break
            self.q.remove(key_to_rm)

        self.fq_dict[key_to_rm] -= 1
        self.output.append(key_to_rm)


def main():
    N = int(sys.stdin.readline())
    fq = FreqPriorityQueue()
    
    for _ in range(N):
        line = sys.stdin.readline().split()
        
        # enqueue
        if line[0] == 'enqueue':
            num = int(line[1])
            fq.enqueue(num)
        
        # dequeue
        else:
            fq.dequeue()

    fq.print_q()


if __name__ == "__main__":
    main()
    