class Queue(object):

    def __init__(self):
        self.queue = []
        pass

    def insert(self, elem):
        self.queue.append(elem)
        pass

    def catch(self):
        if(self.hasItem):
            return self.queue.pop(0)
        pass

    def execute(self):
        pass

    @property
    def length(self):
        return len(self.queue)
    
    @property
    def hasItem(self):
        return len(self.queue) > 0
    
    @property
    def values(self):
        return self.queue