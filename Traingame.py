#### stationsData lists the coordinates for station as well as which number the station is along R,B and G lines
stationsData = (     ### X , Y , R , B, G
                [30,100, 0,1,0],
                [130,100,0,2,0],
                [230,180,0,3,0],
                [330,180,0,4,0],
                [420,180,0,5,0],
                [510,240,0,6,0],
                [620,240,0,7,0],
                [710,240,0,8,0]
                )

def setup():
    size(800,500)
    

def draw():
    background(255)
    stroke(0,0,255)
    strokeWeight(5)
    
    println(len(stationsData))
    println(stationsData[1][0])
    
    for i in range (len(stationsData)):
        stroke(0,0,255)
        ellipse(stationsData[i][0],stationsData[i][1],10,10)
        if i < len(stationsData)-1 :
            line(stationsData[i][0],stationsData[i][1],stationsData[i+1][0],stationsData[i+1][1])
    
    
