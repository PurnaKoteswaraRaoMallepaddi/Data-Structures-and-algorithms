import copy
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        refer = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        if len(digits) == 0:
            return []
        self.final = refer[digits[0]]
        
        if len(digits)==1:
            return self.final
        
        def combinations(digits,index):
            temp = []
            for val1 in self.final:
                for val2 in refer[digits[index]]:
                    temp.append(val1+val2)
            self.final = temp
            if len(digits) - 1 == index:
                return
            else:
               combinations(digits,index+1) 
        combinations(digits,1)
        return self.final
        