"""
ask:
any given user if we want to grab the full social network of that user how do we do that?

ex:
Input Data set:
[	(1,2),
 	(1,3),
	(1,4),
	...
	]
Output: infinite degrees of separation, priority is speed

Req:
- We're given all the connections individually as they are created so we can preprocess this data and store into 
a dataset in order to be able to retreive the desired output as quickly as we can
- Return a dataset with full social network of given user

Dataset:
connections = {user: [host_user], 
               host_user: [user2, user3, user4, ...],
               ...}

Approach:

def Create_network(array):
- Initialize connections = {}, host_user1 = None, host_user2 = None

- If user1 in connections then determine host_user1
    - If len(connections[user1]) = 1 then connections[user1][0] is a potential host
        - potential_host = connections[user1][0]
        - Loop through each level until potential_host has > 1 connection or we loop back to user1
        - host_user1 = potential_host
    - Else: host_user1 = user1
- Repeat for user2 and host_user2

- Case #1: both users are already connected
    -continue
            
- Case #2: host_user1 = None and host_user2 = None:
    - add user1:[user2] and user2:[user1]

- Case #3: host_user1 and host_user2: 
    - Append host_user2 to host_user1 
    - Extend connection[host_user2] to connection[host_user1].
    - Connection[host_user2] = [host_user1]

- Case #4: host_user1 == None:
    - connections[host_user2].append(user1)
    - connections[user1] = [user2]

- Case #5: host_user2 == None:
    - connections[host_user1].append(user2)
    - connections[user2] = [user1]

-return connections

def find_network(user, connections):
- Initialize result = set()

- If user is connections then we determine if who is the host_user
    - If len(connections[user]) = 1 then connections[user][0] is a potential_host
        - potential_host = connections[user][0]
        - Loop through each level until potential_host has > 1 connection or we loop back to user
        - host_user = potential_host
    - Else: host_user = user

    - Add host_user to results
    - Add connections[host_user] to results
    
- Return result
"""
def create_network(array):
    connections = {}

    for (user1, user2) in array:
        host_user1, host_user2 = None, None

        if user1 in connections:
            if len(connections[user1]) == 1: 
                potential_host = connections[user1][0]
                while len(connections[potential_host]) == 1 and connections[potential_host][0] != user1: 
                    potential_host = connections[potential_host][0]
                host_user1 = potential_host
            else:
                host_user1 = user1

        if user2 in connections:
            if len(connections[user2]) == 1: 
                potential_host = connections[user2][0]
                while len(connections[potential_host]) == 1 and connections[potential_host][0] != user2: 
                    potential_host = connections[potential_host][0] 
                host_user2 = potential_host
            else:
                host_user2 = user2

        # print(f'host_user1 = {host_user1}, host_user2 = {host_user2}')
        
        if host_user1 != None and host_user2 != None and host_user1 == host_user2:
            continue
        
        elif host_user1 == None and host_user2 == None:
            connections[user1] = [user2]
            connections[user2] = [user1]

        elif host_user1 != None and host_user2 != None:
            if len(connections[host_user1]) > len(connections[host_user2]):
                primary = host_user1
                secondary = host_user2
            else:
                primary = host_user2
                secondary = host_user1
            connections[primary].append(secondary)
            connections[primary].extend(connections[secondary])
            connections[secondary] = [primary]

        elif host_user1 == None:
            connections[host_user2].append(user1)
            connections[user1] = [user2]

        elif host_user2 == None:
            connections[host_user1].append(user2)
            connections[user2] = [user1]
    
    return connections

def find_network(user, connections):
    result = set()

    if user in connections:
        if len(connections[user]) == 1: 
            potential_host = connections[user][0]
            while len(connections[potential_host]) == 1 and connections[potential_host][0] != user: 
                potential_host = connections[potential_host][0] 
            result.add(potential_host)
            result.update(set(connections[potential_host]))
        else:
            result.add(user)
            result.update(set(connections[user]))

    return result

# Testing:
if __name__ == "__main__":
    array = [(1,2),(2,3),(3,4),(3,1),(6,7),(6,8), (7,1)]
    network = create_network(array)
    print(network)
    print(find_network(7,network))

