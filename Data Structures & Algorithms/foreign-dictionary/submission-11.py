class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]

        adj = {c: set() for w in words for c in w}
        indeg = {c: 0 for c in adj}
        for i in range(1, len(words)):
            w1 = words[i-1]
            w2 = words[i]

            min_len = min(len(w1), len(w2))
            # invalid state, prefix of a word can't come later in lexographic order
            if len(w2) < len(w1) and w1[:min_len] == w2:
                return ""
            
            for j in range(min_len):
                # add to the adj list at the first differing character
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indeg[w2[j]] += 1
                    break
        
        print(adj, indeg)
        bfs = deque([n for n in indeg if indeg[n] == 0])
        res = ""
        visited = set()
        processed = 0

        while bfs:
            c = bfs.popleft()
            processed += 1
            res += c

            nei = adj[c]

            for n in nei:
                print(c, nei, indeg[n])
                indeg[n] -= 1
                if indeg[n] == 0:
                    bfs.append(n)
        
        print(res, processed)
        if processed != len(adj):
            return ""

        return res