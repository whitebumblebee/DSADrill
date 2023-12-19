# Problem Link: https://leetcode.com/problems/destination-city/

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        curr_source_set = set()
        cities = set()
        for path in paths:
            cities.add(path[0])
            cities.add(path[1])
            if path[0] not in curr_source_set:
                curr_source_set.add(path[0])

        for city in cities:
            if city not in curr_source_set:
                return city
