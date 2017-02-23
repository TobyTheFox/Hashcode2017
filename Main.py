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

def evaluation(requests):
    for request in requests:
        endpoint = requests[1]
        connectedCaches=[]
        for item in range (2,len(endpoints[endpoint])):
             connectedCaches.append(item)
                           
        for item in connectedCaches:
            
            videosStored = caches[item[1]]
            if request[1] in videosStored:
                timeSave = (endpoints[endpoint[0]]-item[1]) * request[3]
                return timeSave


            
random.seed()

data = readFile(NAME)
evaluation(requests)
