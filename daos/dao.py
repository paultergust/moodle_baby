from abc import ABC
import pickle

class DAO(ABC):
    def __init__(self, source):
        self.__source = source
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()
    
    def __load(self):
        self.__cache = pickle.load(self.__cache, 'rb')

    def __dump(self):
        pickle.dump(self.__cache, open(self.__source, 'wb'))

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()
    
    def delete(self, key):
        self.__cache.pop(key, None)
        self.__dump()
    
    def get(self, key):
        return self.__cache.get(key, None)
    
    def get_all(self):
        return self.__cache.values()