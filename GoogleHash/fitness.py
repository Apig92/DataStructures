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
    for video in data["video_ed_request"]:
        for ep in data["video_ed_request"][video]:
            number_of_requests = data["video_ed_request"][video][ep][0]
            datacenter_latency = data["ep_to_dc_latency"][ep]
            connected_endpoints =  data["ed_cache_list"][ep]
            caches = [datacenter_latency,]
            for cache in connected_endpoints:
                if solution[cache][video] == 1:
                    caches.append(data["ep_to_cache_latency"][ep][cache])

            smallest_latency = data["video_ed_request"][video][ep][1]
            min_cache = min(caches)
            if min_cache < smallest_latency:
                data["video_ed_request"][video][ep][1] = min_cache

            total_requests += number_of_requests
            gain += (number_of_requests*(datacenter_latency-min_cache))
    score = (gain*1000)

    return score

def move_validity(sol, cache, video, cache_contents, data):
    if sol[cache][video] == 1:
        return False
    return (cache_contents[cache] + data["video_size_desc"][video] <= data["cache_size"])


def change_score(cache,video,data):
    gain=0
    for ep in data["video_ed_request"][video]:
        number_of_requests = data["video_ed_request"][video][ep][0]
        connected_endpoints = data["ed_cache_list"][ep]

    if cache in connected_endpoints:
        smallest = data["video_ed_request"][video][ep][1]
        cache_latency = data["ep_to_cache_latency"][ep][cache]

        if cache_latency < smallest:
            gain+=(number_of_requests*(smallest-cache_latency))

    return gain


def hill_climb(solution,data,cache_in):
    valid_move=True

    while valid_move:
        valid_move = False
        best_score = 0
        best_move = []

        for row in range(len(solution)):
            for column in range (len(solution[row])):
                if move_validity(solution, row, column, cache_in, data):
                    currentscore = change_score(row,column,data)
                    if currentscore > best_score:
                        best_score =currentscore
                        best_move=[row,column]
                        move_found= True
                    elif currentscore == best_score and currentscore > 0:
                        print("test")


        if move_found:
            print("So far the best move is", best_move)
            print("The best score is:", best_score)
            cache, file = best_move[0], best_move[1]
            solution[cache][file] = 1
            cache_in[cache] += data["video_size_desc"][file]
        else:
            print("There are no better options")














data = read_google("input/test.in")
# #solution=[[0 for i in range(data["number_of_videos"])] for j in range(data["number_of_caches"])]
solution = [[0, 0, 1, 0, 0],[0, 1, 0, 1, 0],[1, 1, 0, 0, 0]]
# print(data["ep_to_cache_latency"])
# print("test solution:",solution)
# print(constraints(solution))
if constraints(solution):
    print("final score",scoring(solution,data))
else:
    print("nope")


