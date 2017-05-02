from GoogleHash.read_input import read_google

def constraints(s):
    for i in range(len(s)):
        if sum(s[i]) <= data["cache_size"]:
             return "Is feasible"
        else:
             return -1

def scoring(solution,data):
    total_requests=0
    gain = 0
    score = 0
    l=0

    cache_contents={}
    for file in data["video_ed_request"]:
        for ep in data["video_ed_request"][file]:
            number_of_requests = data["video_ed_request"][file][ep][0]
            connected_endpoints = data["ed_cache_list"][ep]
            datacenter_latency = data["ep_to_dc_latency"][ep]
            caches=[datacenter_latency,]
            for cache in connected_endpoints:

                if solution[cache][file] == 1:
                    l += 1
                    caches.append(data["ep_to_cache_latency"][ep][cache])

            min_latency= data["video_ed_request"][file][ep][1]
            min_cache= min(caches)
            if min_cache < min_latency:
                data["video_ed_request"][file][ep][1] = min_cache

            total_requests += number_of_requests
            gain =(number_of_requests*(datacenter_latency-min_cache))
            score = (gain*1000)

    return score,caches,gain,min_cache,connected_endpoints,l

def move_validity(sol, cache, video, cache_contents, data):
    if sol[cache][video] == 1:
        return False
    return (cache_contents[cache] + data["video_size_desc"][video] <= data["cache_size"])

# def hill_climber(solution,data,cache_in):
#     valid_move=True
#
#     while valid_move:
#         valid_move = False
#         best_score = 0
#         best_move = []
#
#         for row in range(len(solution)):
#             for column in range (len(solution[row])):
#                 if move_validity(solution, row, column, cache_in, data):
#








data = read_google("input/test.in")
#solution=[[0 for i in range(data["number_of_videos"])] for j in range(data["number_of_caches"])]
solution = [[0, 0, 1, 0, 0],[0, 1, 0, 1, 0],[1, 1, 0, 0, 0]]
print("test solution:",solution)
print(constraints(solution))
if constraints(solution):
    print("final score",scoring(solution,data))
else:
    print("nope")
