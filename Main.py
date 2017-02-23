import random
NAME = "me_at_the_zoo"

videoCount = 0
endpointCount = 0
reqDescCount = 0
cacheServerCount = 0
capacity = 0

def readFile(filename):
    global videoCount
    global endpointCount
    global reqDescCount
    global cacheServerCount
    global capacity
    
    f = open(filename+".in", 'r')
    params = f.readline()
    paramlist = params.split(" ")
    videoCount = int(paramlist[0])
    endpointCount = int(paramlist[1])
    reqDescCount = int(paramlist[2])
    cacheServerCount = int(paramlist[3])
    capacity = int(paramlist[4])

    videos = []
    #[size]
    endpoints = []
    #[latency, connected cache, [conncection1 id, connection1 latency] [connection2...]]
    requests = []
    #[video id, endpoint id, number of requests]
    
    videos = f.readline()[:-1].split(" ")

    for endpointIndex in range(endpointCount):
        endpoint = f.readline()[:-1].split(" ")
        for endIndex in range(len(endpoint)):
            endpoint[endIndex] = int(endpoint[endIndex])
        
        for connection in range(endpoint[-1]):
            endpoint.append(f.readline()[:-1].split(" "))
            for elementIndex in range(len(endpoint[-1])):
                endpoint[-1][elementIndex] = int(endpoint[-1][elementIndex])
        
        endpoints.append(endpoint)
                   
    for request in range(reqDescCount):
        requests.append(f.readline()[:-1].split(" "))

    return [videos, endpoints, requests]

##def evaluation(requests):
##    endpoints = data[1]
##    requests = data[2]
##    caches = [[1],[1],[1]]
##    for request in requests:
##        endpoint = request[1]
##        connectedCaches=[]
##        for item in range (2,len(endpoints[int(endpoint)])):
##             connectedCaches.append(item)
##                           
##        for item in connectedCaches:
##            
##            videosStored = caches[item[0]]
##            if request[1] in videosStored:
##                timeSave = (endpoints[endpoint[0]]-item[1]) * request[3]
##                return timeSave
def connectedCaches(endpoint):
    endpoints = data[1]
    currentEndpoint = endpoints[endpoint]
    connectedCaches = []
    count = 0
    for item in currentEndpoint:
        if count == (0 or 1):
            count += 1
        else:
            connectedCaches.append(item)
    return connectedCaches        


def cachetime(videoID,endpoint):
    endpoints = data[1]
    endpoint = endpoints[endpoint]
    connectedCaches = connectedCaches(endpoint)
    
    lat = endpoint[0]
    
    for cache in connectedCaches:
        cacheID = cache[0]
        if videoID in solution[cacheID]:
            if lat >= cache[1]:
                
                lat = cache[1]
    return endpoint[0] - lat


def evaluation(requests):
    
    for request in requests:
        
        videoID = request[0]
        endpoint = request[1]
        conCache = connectedCaches(endpoint)
        cacheTime = cachetime(videoID,endpoint)
        timeSaved += cacheTime*request[2]       
    return timeSaved * 1000
            
random.seed()
requests = [[1,1,100]]
data = readFile(NAME)

