class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        queue=deque()
        m=len(image)
        n=len(image[0])
        temp=image[sr][sc]
        queue.append((sr,sc))
        image[sr][sc]=color
        while(queue):
            size=len(queue)
            for _ in range(size):
                x,y=queue.popleft()
                if(x+1)<m and image[x+1][y]==temp:
                    image[x+1][y]=color
                    queue.append((x+1,y))
                if (x-1)>=0 and image[x-1][y]==temp:
                    image[x-1][y]=color
                    queue.append((x-1,y))
                if y+1<n and image[x][y+1]==temp:
                    image[x][y+1]=color
                    queue.append((x,y+1))
                if y-1>=0 and image[x][y-1]==temp:
                    image[x][y-1]=color
                    queue.append((x,y-1))
        return image
