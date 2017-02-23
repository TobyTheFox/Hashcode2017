import random
from operator import itemgetter
NAME = "me_at_the_zoo"

videoCount = 0
endpointCount = 0
reqDescCount = 0
cacheServerCount = 0
capacity = 0




def getPopularVideosInEndpoint(endpointID,requests):
    '''returns sorted list of video ids'''
    popularVideos = []
    #[vidid, requests]
    for request in requests:
        if request[1] == endpointID:
            popularVideos.append([request[0],request[2]])
    popularVideos= sorted(popularVideos, key=itemgetter(1))
    popularVideos.reverse()
    return popularVideos

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
        request = f.readline()[:-1].split(" ")
        for itemIndex in range(len(request)):
            request[itemIndex] = int(request[itemIndex])
        requests.append(request)
        

    return [videos, endpoints, requests]


random.seed()

data = readFile(NAME)
print(getPopularVideosInEndpoint(0,data[2]))
