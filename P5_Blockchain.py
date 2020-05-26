import hashlib
import time


class Block:

    def __init__(self, timestamp, data, previous_hash=None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()


class BlockChain:

    def __init__(self):
        self.head = None

    def add_block(self, timestamp, data):
        if self.head == None:
            self.head = Block(timestamp, data)
            return
        block = self.head
        while block.next:
            block = block.next
        block.next = Block(timestamp, data, previous_hash=block.hash)

    def get_block(self, data):
        if self.head == None:
            return False
        block = self.head
        while block:
            if block.data == data:
                return (block.data, block.timestamp, block.hash)
            else:
                return False
            block = block.next

    def __repr__(self):
        block = self.head
        if block == None:
            return "empty block chain"
        output = []
        while block:
            output.append((block.data, block.timestamp))
            block = block.next
        output = map(str, output)
        return '->'.join(output)


if __name__ == '__main__':
    blockchain = BlockChain()
    timestamp1 = time.time()

    print(blockchain)


    print('Block 1')
    print('==================================')
    blockchain.add_block(timestamp1, "block1")
    print(blockchain)

    print('Get Block 1')
    print('==================================')

    print(blockchain.get_block('block1'))
    print('Block 2')
    print('==================================')
    timestamp2 = time.time()
    blockchain.add_block(timestamp2, "block2")
    print(blockchain)
    print('Block 3')
    print('==================================')
    print(blockchain.get_block('block3'))  # should return false
