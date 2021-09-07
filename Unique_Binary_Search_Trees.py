class Solution:
    def numTrees(self, n: int) -> int:
        self.index = {}
        def count(list_: List):
            if len(list_)==2:
                return 2
            elif len(list_) == 1:
                return 1
            elif len(list_) in self.index.keys():
                return self.index[len(list_)]
                
            total = 0
            for i,val in enumerate(list_):
                if i == 0 or i == len(list_)-1:
                    total += count(list_[1:])
                else:
                    total += count(list_[:i])*count(list_[i+1:])
            self.index[len(list_)] = total
            return total
        list_ = [val for val in range(n)]
        val = count(list_)
        return val