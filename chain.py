class BlockChain:
    def __init__(self):
        self.chain = []

    def add_block(self, block):
        self.chain.append(block) 

    def show_chain(self):
        print(self.chain)

    def get_block(self, index):
        print('Block at index: ' + str(index) + str(self.chain[index]))
        print('Block Value: ', self.chain[index].value)


