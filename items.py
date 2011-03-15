import sys

_items = {}
_by_id = {}

class ItemInfo (object):
    def __init__(self, name, value, data=0, maxstack=64):
        self.name = str(name)
        self.value = int(value)
        self.data = int(data)
        self.maxstack = int(maxstack)

    def __str__ (self):
        return 'Item: %s, ID: %d, Data: %d, MaxStack: %d'%(
            self.name,
            self.value,
            self.data,
            self.maxstack)


def LoadItems(filename = 'items.db'):
    print 'Reading items database:', filename, '...'
    items = 0
    try:
        with file(filename) as f:
            items_txt = f.read()
    except Exception, e:
        print "Error reading items file: ", e;
    for line in items_txt.split("\n"):
        try:
            line = line.strip()
            if len(line) == 0: 
                continue
            if line[0] == "#": 
                continue; 

            value, name, data, maxstack = line.split(',')
            _items[name] = ItemInfo(name, value, data, maxstack)
            _by_id[int(value)] = ItemInfo(name, value, data, maxstack)
            items += 1
        except Exception, e:
            print "Error reading line:", e
            print "Line: ", line
    print 'Loaded', items, 'items.'


def byName (name):
        try:
            return _items[name]
        except:
            print 'Unknown item:', name
            sys.exit(1)


def byID (id):
        try:
            return _by_id[id]
        except:
            print 'Unknown item ID:', id
            sys.exit(1)
