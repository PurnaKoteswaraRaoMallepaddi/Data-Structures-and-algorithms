class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        for w in sorted(strs):
            key = ''.join(sorted(w))
            d[key] = d.get(key,[]) + [w]
        return d.values()
    
#     def is_same(self,word,key):
#         word = ''.join(sorted(word))
#         key = ''.join(sorted(key))
#         if key == word:
#             return True

        
#         return False
        
                    
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         if len(strs) == 1:
#             return [strs]
#         dict_ = {}
#         for word in strs:
#             check = False
#             for key in dict_.keys():
#                 if self.is_same(word,key):
#                     dict_[key].append(word)
#                     check = True
#                     break
#             if not check:
#                 dict_[word] = [word]
        
#         return [val for val in dict_.values()]
                    
#len(list(([char for char in key]) - ([char for char in word]))) == 0 and len(list(([char for char in word]) - ([char for char in key]))) == 0
            
        