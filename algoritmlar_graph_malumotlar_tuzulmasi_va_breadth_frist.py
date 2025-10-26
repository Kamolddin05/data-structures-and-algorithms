''' 15-16/10/2025'''


# from collections import deque

# def search(start_node, target = "elon musk"):
#     search_queue = deque()
#     search_queue += graph[start_node]
#     searched = set()

#     while search_queue:
#         person = search_queue.popleft()
#         if person not in searched:
#             if person == target:
#                 print(f"{target} ni topdik! ")

#                 return True
#             else:
#                 search_queue += graph[person]
#                 searched.add(person)
#     return False

# graph = {
#     "siz":["ali", "vali", "tohir"], 
#          "ali":["aziza", "olim"], 
#          "vali":["botir", "ziyoda"],
#          "tohir": ["elon musk", "mohir"], 
#          "olim": [], 
#          "aziza":[], 
#          "botir":[], 
#          "ziyoda":["aziza"],
#          "elon musk":[],  
#          "mohir":[]
#          }

# search("siz", "elon musk")




# from collections import deque

# def search(start_node, target="elon musk"):
#     queue = deque(graph[start_node])
#     searched = set()

#     while queue:
#         person = queue.popleft()
#         if person not in searched:
#             if person == target:
#                 print(f"{target} ni topdik")
#                 return True
#             else:
#                 queue += graph[person]
#                 searched.add(person)
#     return False




# graph = {
#     "siz":["ali", "vali", "tohir"], 
#          "ali":["aziza", "olim"], 
#          "vali":["botir", "ziyoda"],
#          "tohir": ["elon musk", "mohir"], 
#          "olim": [], 
#          "aziza":[], 
#          "botir":[], 
#          "ziyoda":["aziza"],
#          "elon musk":[],  
#          "mohir":[]
#          }

# search("siz", "elon musk")





''' 🧩 1-masala: Grafdagi barcha do‘stlarni BFS yordamida tekshirilgan tartibda ekranga chiqaring. '''

from collections import deque

def search(start_node, target=" "):
    queue = deque(graph[start_node])
    searched =  set()
    
    while queue:
        person = queue.popleft()
        if person not in searched:
            if person == target:
                print(f"{target.capitalize()} ni topdik!")
            else:
                queue += graph[person]
                searched.add(person)
    print("Afsus siz sorgan insondi topaolmdik!")
    return False


graph ={
    "kamoliddin":["yusufjon", "azimjon", "barkamol", "diyorbek", "azizbek", "sardor", "muhammadziyo"],
    "sardor":["azizbek", "diyorbek", "muhammadziyo", "tursunboy", "feruz"],
    "yusufjon":["azimjon", "barkamol", "hamroz", "jasur", "kamoliddin"],
    "barkamol":["kamoliddin", "yusufjon", "azimjon", "abbos", "nurbek"],
    "abbos":["nozli", "nurbek", "barkamol", "kamoliddin"],
    "nozli":["mashxura"],
    "mashxura":[],
    "azimjon": [],
    "diyorbek": [],
    "azizbek": [],
    "muhammadziyo": [],
    "tursunboy": [],
    "feruz": [],
    "hamroz": [],
    "jasur": [],
    "nurbek": []
}

search("kamoliddin", "izmir")



# m2

# graph = {
#     "start": ["a", "b"],
#     "a": ["c"],
#     "b": ["d"],
#     "c": [],
#     "d": ["e"],
#     "e": []
# }

# from collections import deque

# def search(start_node, target=""):

#     queue = deque(graph[start_node])
#     searched = set()
#     while queue:
#         person = queue.popleft()
#         if person not in searched:
#             if person == target:
#                 return True
#             else:
#                 queue += graph[person]
#                 searched.add(person)
#                 return False
#     return False

# print(search("start", "e"))
# print(search("start", "x"))



""" 🔁 3-masala (Eng qisqa yo‘lni topish) """



