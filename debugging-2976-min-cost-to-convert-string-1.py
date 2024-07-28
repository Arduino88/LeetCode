class Solution:
    def minimumCost(self, source: str, target: str, original, changed, cost) -> int:
        def printDict(dictionary):
            for x in dictionary:
                print(x, ':', dictionary[x])


        temp = sorted(list(set(original + changed)))

        d = {x: {y:float('inf') if y != x else 0 for y in temp} for x in temp}

        for i in range(len(cost)):
            d[original[i]][changed[i]] = cost[i]

        for k in temp:
            for i in temp:
                for j in temp:
                    if i == j:
                        continue

                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

        printDict(d)

        total = 0
        for i in range(len(source)):
            '''print(f"Checking key '{source[i]}': {source[i] in d}")
            print(f"Dictionary entry for '{source[i]}': {d.get(source[i])}")

            # Explicitly printing the type and repr of the key 'b'
            print(f"Type of key 'b': {type('b')}")
            print(f"Repr of key 'b': {repr('b')}")
            print(f"Keys in dictionary: {list(d.keys())}")
            
            print(f"Checking key 'b' with get: {d.get('b')}")
            try:
                print(f"Checking key 'b' with direct access: {d['b']}")
            except KeyError as e:
                print(f"KeyError: {e}")
                return -1'''

            total += d[source[i]][target[i]]

        if total == float('inf'):
            return -1

        return total
    
# Example usage:
sol = Solution()
source = "abcd"
target = "acbe"
original = ["a","b","c","c","e","d"]
changed = ["b","c","b","e","b","e"]
cost = [2,5,5,1,2,20]
print(sol.minimumCost(source, target, original, changed, cost))