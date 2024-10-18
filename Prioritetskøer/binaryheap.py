

# class BinaryHeap:
#     def __init__(self):
#         self.heap = []
    
#     def bubble_up():
#         pass

#     def insert():
#         pass

#     def remove_min():
#         pass


class BinaryHeap:
    def __init__(self):
        self.heap = []
    
    def parent_of(self, index: int):
        return (index-1) // 2

    # setter inn elementet sist i listen og
    def insert(self, x: int):
        self.heap.append(x)
        i = len(self.heap)-1
        
        print(self.heap)
        
        while i > 0 and self.heap[i] < self.heap[self.parent_of(i)]:
                    
            # bytte om elementene
            tmp = self.heap[i]
            self.heap[i] = self.heap[self.parent_of(i)]
            self.heap[self.parent_of(i)] = tmp
            print(self.heap, "bytte")
            
            i = self.parent_of(i)

    # finner venstre barnenode
    def left_of(self, index):
        return (2 * index) + 1
    
    # finner høyre barnenode
    def right_of(self, index):
        return (2 * index) + 2

    # fjerner det minste elementet og "bobbler" ned det siste elementet
    def remove_min(self) -> int:
        out = self.heap[0]
        
        # en sjekk for å se om det er kun et element igjen
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
        else:
            out = self.heap.pop()
        
        i = 0
        n = len(self.heap)

        while self.right_of(i) < n - 1:
            # henter indexen j til den minste av venstre eller høyre barnenode
            if self.heap[self.left_of(i)] <= self.heap[self.right_of(i)]:
                j = self.left_of(i)
            else:
                j = self.right_of(i)
            
            # stopper opp med engang hvis barnenoden er større
            if self.heap[j] > self.heap[i]:
                break
            
            # bytter om elementene på i og j
            tmp = self.heap[i]
            self.heap[i] = self.heap[j]
            self.heap[j] = tmp
            
            i = j
        
        # en siste sjekk dersom det første elementet har kun 1 eller 2 barnenoder
        if self.left_of(i) < n and self.heap[self.left_of(i)] <= self.heap[i]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[self.left_of(i)]
            self.heap[self.left_of(i)] = tmp
            
        print(self.heap, out)
        return out

def main():
    heap = BinaryHeap()
    for i in [2,6,4,10,5,3,8]:
        heap.insert(i)
    
    for i in range(7):
        heap.remove_min()
    
main()
    