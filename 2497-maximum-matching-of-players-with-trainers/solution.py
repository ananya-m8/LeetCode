class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        c,j=0,0
        m=len(trainers)
        n=len(players)
        i=0
        while i<n and j<m:
            if players[i]<=trainers[j]:
                c+=1
                i+=1
            j+=1
        return c
