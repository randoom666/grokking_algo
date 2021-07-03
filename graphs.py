from collections import deque

graph = {}
graph['me'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'johnny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['johnny'] = []
print(graph)

def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print('It`s a mango seller here and his name is', person)
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search('me')


