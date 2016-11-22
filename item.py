class Item:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def combine(self,item):
        return Item(self.name + item.name)

if __name__ == "__main__":
    item = Item("name")
    print('my name is {}'.format(item.name))


