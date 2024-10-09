import sys
n, r, c = map(int, input().split())


width = pow(2, n)

answer = 0


def search(cx, cy, curWidth):
    global answer

    if curWidth==1:
        answer+=1

    if cx==r and cy==c and curWidth==1:
        print(answer-1)
        sys.exit()


    if curWidth%2==0:
        nextWidth = curWidth//2
        
        if cx<=r<cx+nextWidth and cy<=c<cy+nextWidth:
           
            search(cx, cy, nextWidth)
        
        sx, sy = cx, cy+nextWidth
        if sx<=r<sx+nextWidth and sy<=c<sy+nextWidth:
            
            answer+= (nextWidth * nextWidth)
            search(cx, cy+nextWidth, nextWidth)
        
        sx, sy = cx+nextWidth, cy

        if sx<=r<sx+nextWidth and sy<=c<sy+nextWidth:
            
            answer+= (nextWidth * nextWidth) *2
            search(cx+nextWidth, cy, nextWidth)
        
        sx, sy = cx+nextWidth, cy+nextWidth
        if sx<=r<sx+nextWidth and sy<=c<sy+nextWidth:
            
            answer+= (nextWidth * nextWidth) *3
            search(cx+nextWidth, cy+nextWidth, nextWidth)

    
search(0, 0, width)