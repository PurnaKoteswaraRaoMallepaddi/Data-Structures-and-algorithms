class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        https://www.youtube.com/watch?v=sz1qaKt0KGQ&t=589s
        """
        self.final = []
        def generate(openp,closep,gen):
            if openp == 0 and closep == 0:
                self.final.append(gen)
                return
            if openp == closep and openp != 0:
                gen += '('
                openp -= 1
                # print("equal case")
                generate(openp,closep,gen)
                
            if openp == 0 and closep != 0:
                gen += ')'*closep
                self.final.append(gen)
                return
            if openp < closep and openp != 0:
                generate(openp - 1,closep,gen + '(')
                generate(openp,closep - 1,gen + ')')
            
        generate(n,n,'')
        self.final = list(set(self.final))
                
        return self.final