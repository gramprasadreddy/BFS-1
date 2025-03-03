# Course Schedule (https://leetcode.com/problems/course-schedule/)

# Time Complexity : O(V+E)
# Space Complexity : O(V+E)
# Did this code successfully run on GFG : YES
# Any problem you faced while coding this : NO


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True
        indegrees = [0] * (numCourses) # initiate indegrees list of len numCourses with 0
        hm ={}
        q = deque()
        
        n = len(prerequisites)

        for i in range (n): 
            ind = prerequisites[i][1]
            dep = prerequisites[i][0]

            indegrees[dep]+=1 #increment  the dependent value by 1 in the list
            if ind not in hm:
                hm[ind] = [] # creat a entry in hashmap and append the dep in it
            hm[ind].append(dep)

        count = 0
        for i in range (len(indegrees)): # pot all the independent courses in indegrees
            if indegrees[i] == 0:

                q.append(i)
                count+=1

        if count == numCourses: # if  the count = numcourses we can return true
            return True
        if not q: # if the q is empty then it means there is a cycle in graph ( kind of like a deadlock)
            return False # and no course can be finished
        
        while q: # BFS
            curr = q.popleft() # pop front

            children = hm.get(curr,[]) # get the children or dependents on the curr

            if not children: # no dependents then continue
                continue
            
            for child in children: # for the entries in children list
                indegrees[child]-=1 # decrement indegrees
                if(indegrees[child] == 0):
                    q.append(child) # if it has become independent put it in q
                    count+=1 # count increment
            
            if count == numCourses: # count reaches numcourses we can return true even before the q is empty
                return True
        
        return False


        