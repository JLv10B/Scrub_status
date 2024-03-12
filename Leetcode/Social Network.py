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

Social network retrieval

This script creates a dictionary that stores full social networks and allows retrieval of the social network
in O(1) time.

Functions:
----------
create_social_network_dict - returns social_network_dict
find_update_root - helper function to find and update roots in social_network_dict
retrieve_social_network - retrieves social network for given user


Input = [(1,2),
         (1,3),
         (1,4),
         ...]

Dataset:
user_network = {user: [host_user, (connections)], 
               1:[1,(2,3)],
               2:[1,()],
               3:[1,()],
               ...}

Approach:
- always merge to the left
- always merge into the final root
- determine root during runtime rather than pre-processing*

def Create_network(user_connection_data):
- Input = [(1,2),
           (1,3),
           (1,4),
           ...]

- Output ={1:[1,(2,3)],
           2:[1,()],
           3:[1,()],
           ...}


- Initialize user_network = {}

- Iterate through user_connection_data 
    - 
    - If either user is not in user_network then intialize user:[root_user,(connections)]

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
def create_social_network_dict(user_connection_data):
    """
    This function creates social_network_dict which stores the social network for all users.

    Parameters:
    -----------
    user_connection_data = [(1,2),
                            (2,3),
                            (3,4),
                            ...]

    Returns:
    --------
    social_network_dict = {1:[1,(2,3,4)],
                           2:[1,()],
                           3:[1,()],
                           4:[3,()],
                           ...}
    """
    social_network_dict = {}

    for (user1, user2) in user_connection_data:
        host_user1, host_user2 = None, None

        # print(f'host_user1 = {host_user1}, host_user2 = {host_user2}')
        
        if host_user1 != None and host_user2 != None and host_user1 == host_user2:
            continue
        
        elif host_user1 == None and host_user2 == None:
            social_network_dict[user1] = [user2]
            social_network_dict[user2] = [user1]

        elif host_user1 != None and host_user2 != None:
            if len(social_network_dict[host_user1]) > len(social_network_dict[host_user2]):
                primary = host_user1
                secondary = host_user2
            else:
                primary = host_user2
                secondary = host_user1
            social_network_dict[primary].append(secondary)
            social_network_dict[primary].extend(social_network_dict[secondary])
            social_network_dict[secondary] = [primary]

        elif host_user1 == None:
            social_network_dict[host_user2].append(user1)
            social_network_dict[user1] = [user2]

        elif host_user2 == None:
            social_network_dict[host_user1].append(user2)
            social_network_dict[user2] = [user1]
    
    return social_network_dict

def find_update_root():
    pass

def retrieve_social_network(user, connections):
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
