class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue=deque()
        queue.append(entrance)
        rows=len(maze)
        cols=len(maze[0])
        dirc=[0,1,0,-1,0]
        visited={tuple(entrance)}
        counter=0
        while(queue):
            counter+=1
            for _ in range(len(queue)):
                x,y=queue.popleft()
                for i in range(4):
                    newX,newY=x+dirc[i],y+dirc[i+1]
                    if (newX,newY) not in visited:
                        if newX<0 or newX>=rows or newY<0 or newY>=cols:
                            if [x,y]!=entrance:
                                return counter-1
                        elif maze[newX][newY]=='.':
                            queue.append((newX,newY))
                            visited.add((newX,newY))
        return -1
