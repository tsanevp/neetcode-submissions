class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        preMap = {i: [] for i in range(numCourses)}
        for course, preReq in prerequisites:
            preMap[course].append(preReq)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if not preMap[course]:
                return True
            
            visited.add(course)
            for crs in preMap[course]:
                if not dfs(crs):
                    return False
            
            visited.remove(course)
            preMap[course] = []
            return True
        
        for course in preMap:
            if not dfs(course):
                return False
        
        return True


        

        
