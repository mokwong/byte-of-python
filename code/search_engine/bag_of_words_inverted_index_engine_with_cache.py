# 需要安装这个包
import pylru

import bag_of_words_inverted_index_engine
import search_engine_base


class LRUCache(object):
    def __init__(self, size=32):
        self.cache = pylru.lrucache(size)

    def has(self, key):
        return key in self.cache

    def get(self, key):
        return self.cache[key]

    def set(self, key, value):
        self.cache[key] = value


class BOWInvertedIndexEngineWithCache(bag_of_words_inverted_index_engine.BOWInvertedIndexEngine, LRUCache):
    """
    倒排索引，加缓存

    word -> text_id_list
    """

    def __init__(self):
        # 直接初始化该类的第一个父类，不过使用这种方法时，要求继承链的最顶层父类必须要继承 object；
        super(BOWInvertedIndexEngineWithCache, self).__init__()
        # 对于多重继承，如果有多个构造函数需要调用， 我们就必须用传统的方法LRUCache.__init__(self) 。
        LRUCache.__init__(self)

    def search(self, query):
        if self.has(query):
            print('cache hit!')
            return self.get(query)

        result = super(BOWInvertedIndexEngineWithCache, self).search(query)
        self.set(query, result)

        return result


search_engine = BOWInvertedIndexEngineWithCache()
search_engine_base.main(search_engine)
