"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You 
are given an array prerequisites where prerequisites = [a, b] indicates that you must take 
course b first if you want to take course a.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Input: numCourses = int, prerequisits = array of 2 element arrays [[course, prereq]]
Output: True if you can finish all courses


Break down the problem:
1. Focus on the requirements. Figure out the BigO time/space requirements.

Requirements:
-We can take all the courses if prerequisites overlap with the course
-In other words there cannot be a loop in prerequisites
-Prerequisites is an array of 2 val arrays that we can plot into another datastructure to see if there is 
any loops
-Time:O(n)
-Space:O(n)

2. What cases do we actually need to handle? Check for edge cases. Come up with example data 
inputs to work through
Edge cases:
-no prereqs

Example:
numCourses = 5
prereq = [[1,0], [2,3], [0,2],[3,0],[0,3]] <-- loop
Output = False

{1:(0),
 2:(3),
 0:(2,3),
 3:(0),
}

ex.
1->0->2->1
{1:(0),
 0:(2),
 2:(1)}
Create the dict with prereqs and check if the course is a prereq of the prereq

3. What does data structure look like to satisfy all the above?

dict

4. Now we can code

"""

def build_prereq_dict(prereq):
    # Iterate through [prereq] to create {course_prereqs} with {course:(prereq)}
    course_prereqs = {}
    for pre in prereq:
        if pre[0] not in course_prereqs:
            course_prereqs[pre[0]] = [pre[1]]
        else:
            course_prereqs[pre[0]].append(pre[1])

    return course_prereqs

def course_schedule(numCourses, prereq):
    prereq_dict = build_prereq_dict(prereq)
    # print(prereq_dict)
    
    valid_prereq = [0] * numCourses
    for course in prereq_dict:
        if find_prereq_loop(course, prereq_dict, valid_prereq):
            return False
    return True

def find_prereq_loop(course, prereq_dict, valid_prereq):
    # Perform a depth first traversal to check if there are any loops
    if course not in prereq_dict:
        return False
    
    if valid_prereq[course-1] == 1:
        return False
    
    if valid_prereq[course-1] == -1:
        return True
    
    valid_prereq[course-1] = -1

    for pre in prereq_dict[course]:
        # print(pre)
        if find_prereq_loop(pre, prereq_dict, valid_prereq):
            return True
    
    valid_prereq[course-1] = 1
    return False

# Testing
if __name__ == "__main__":
    # prereq = [[1,0], [2,3]]
    prereq = [[1,0], [2,3], [0,2],[3,0],[0,3]]
    print(course_schedule(100, prereq))