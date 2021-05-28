class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        self.final_str = ""
        def count_and_say(curr_str,curr_itr,n):
            if curr_itr == n:
                self.final_str =  curr_str
                return
            
            new_str = ""
            temp_char = curr_str[0]
            count = 0
            for char in (curr_str):
                print(char,temp_char)
                if char == temp_char:
                    count += 1
                else:
                    
                    new_str += str(count) + temp_char
                    count = 1
                    temp_char = char
                    
            new_str += str(count) + temp_char
            
            curr_itr += 1
            count_and_say(new_str,curr_itr,n)
                
        count_and_say("1",1,n)
        return self.final_str