


class Solution:
    word = []
    steps = []
    memo = {}
    keyboard = {
        'A': (0, 0),
        'B': (1, 0),
        'C': (2, 0),
        'D': (3, 0),
        'E': (4, 0),
        'F': (5, 0),
        
        'G': (0, 1),
        'H': (1, 1),
        'I': (2, 1),
        'J': (3, 1),
        'K': (4, 1),
        'L': (5, 1),
        
        'M': (0, 2),
        'N': (1, 2),
        'P': (3, 2),
        'O': (2, 2),
        'Q': (4, 2),
        'R': (5, 2),
        
        'S': (0, 3),
        'T': (1, 3),
        'U': (2, 3),
        'V': (3, 3),
        'W': (4, 3),
        'X': (5, 3),
        
        'Y': (0, 4),
        'Z': (1, 4)
    }
    
    def search(self, i: int, j: int, k: int, depth: int, memory = {}) -> dict:
                
        if k == len(self.word) or depth > 5: #base case
            memory['value'] = 0
            memory[depth] = (i, j)
            return memory
        
        move_i_cost = self.distance_between_chars(self.word[i], self.word[k])
        
        if j is None:
            move_j_cost = 0
        else:
            move_j_cost = self.distance_between_chars(self.word[j], self.word[k])

        
        
        a = move_i_cost + self.search(i=k, j=j, k=k+1, depth=depth+1).get('value')
        b = move_j_cost + self.search(i=i, j=k, k=k+1, depth=depth+1).get('value')
 
        print('k:', k, 'depth:', depth)
        memory['value'] = min(a, b)
        memory[depth] = (i, j)
        memory['finger1_pos'] = i
        memory['finger2_pos'] = j
        return(memory)
    
    
    def distance_between_chars(self, char1: str, char2: str) -> int:
        if self.memo.get((char1, char2)) is None:
            dx = abs(self.keyboard[char1][0] - self.keyboard[char2][0])
            dy = abs(self.keyboard[char1][1] - self.keyboard[char2][1])
            self.memo[(char1, char2)] = dx + dy
    
        return self.memo[(char1, char2)]
    

    def algorithm(self):
        loop = True
        finger1 = 0
        finger2 = None
        letter_index = 1
        
        
        
        # search both options
        while loop:
            choice_cost = self.distance_between_chars(self.word[0], self.word[1])
            dict1 = self.search(i=finger1, j=letter_index-1, k=letter_index, depth=0).copy()
            dict2 = self.search(i=letter_index-1, j=finger2, k=letter_index, depth=0).copy()
            
            if dict1['value'] < dict2['value']:
                self.steps.append(1)
                finger1 = letter_index - 1
                
            else:
                self.steps.append(2)
                finger2 = letter_index - 1
                pass
            
            letter_index += 1
            
            print(finger1, finger2)
            print(dict1, dict2, choice_cost)
            if letter_index == len(self.word):
                loop = False
        
        pass





    def minimumDistance(self, word: str) -> int:
        self.word = list(word)
        
        
        self.algorithm()
        
        


sol1 = Solution()

print(sol1.minimumDistance(word='CAKE'))