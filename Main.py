import random
from operator import itemgetter
NAME = "trending_today"
RANDOM_FACTOR1 = 300
RANDOM_FACTOR2 = 3000

videoCount = 0
endpointCount = 0
reqDescCount = 0
cacheServerCount = 0
capacity = 0


def getEndpointsConnectedToCache(cacheID, endpoints):
    '''returns list of endpoints connected to a cache'''
    connectedEndpoints = []
    for endpointIndex in range(len(endpoints)):
        connections = endpoints[endpointIndex][2:]
        for connection in connections:
            if connection[0] == cacheID:
                connectedEndpoints.append(endpointIndex)
    return connectedEndpoints
    
def getPopularVideosForCache(cacheID, data):
    print("GET POPULAR VIDEOS FOR CACHE ",cacheID)
    connectedEndpoints = getEndpointsConnectedToCache(cacheID,data[1])
    connectedEndpointIDs = []
    allVideos = []
    for connectedEndpoint in connectedEndpoints:
        #allVideos += getPopularVideosInEndpoint(connectedEndpoint,data[2])
        connectedEndpointIDs.append(connectedEndpoint)

    for i in range(RANDOM_FACTOR1):
        allVideos += getPopularVideosInEndpoint(random.choice(connectedEndpointIDs),data[2])
    
    uniqueVideos = []
    for video in allVideos:
        for uniqueVideoIndex in range(len(uniqueVideos)):
            if uniqueVideos[uniqueVideoIndex][0] == video[0]:
                uniqueVideos[uniqueVideoIndex][1] += video[1]
                break
        else:
            uniqueVideos.append(video)
    popularVideos= sorted(uniqueVideos, key=itemgetter(1))
    popularVideos.reverse()
    return popularVideos

def getPopularVideosInEndpoint(endpointID,requests):
    '''returns sorted list of video ids'''
    #print("GET POPUAR VIDEOS IN ENDPOINT")
    popularVideos = []
    #[vidid, requests]
    #for request in requests:
    for i in range(RANDOM_FACTOR2):
        request = random.choice(requests)
        if request[1] == endpointID:
            popularVideos.append([request[0],request[2]])
    #print("POP",popularVideos)
    popularVideos= sorted(popularVideos, key=itemgetter(1))
    popularVideos.reverse()
    return popularVideos


def readFile():
    global videoCount
    global endpointCount
    global reqDescCount
    global cacheServerCount
    global capacity
    
    f = open(NAME+".in", 'r')
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

def allocateVideos(videosAndPopularity, data):
    '''returns list of videosIDs that can be added considering server capacity'''
    '''Input is sorted in order of preference'''
    allocatedVideos = []
    currentCapacity = capacity
    videoSizes = data[0]
    for videoPop in videosAndPopularity:
        #print(currentCapacity)
        currentVideoID = videoPop[0]
        if currentCapacity - videoSizes[currentVideoID] > 0:
            allocatedVideos.append(currentVideoID)
            currentCapacity -= videoSizes[currentVideoID]

    return allocatedVideos

    
def encode(solution):
    '''solution is list of videos on each cache'''
    f = open(NAME+".out", 'w')
    f.write(str(len(solution))+"\n")
    for serverIndex in range(len(solution)):
        f.write(str(serverIndex))
        for video in solution[serverIndex]:
              f.write(" " + str(video))
        f.write("\n")


    f.close()

def findBasicSolution(data):
    '''Finds most popular videos on each cache and allocates them'''
    allocatedVideosByCache = []
    for cacheIndex in range(cacheServerCount):
        cacheSolution = getPopularVideosForCache(cacheIndex,data)
        allocatedVideosByCache.append(allocateVideos(cacheSolution, data))

    return allocatedVideosByCache


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



data = readFile()

basicSolution = findBasicSolution(data)
encode(basicSolution)
