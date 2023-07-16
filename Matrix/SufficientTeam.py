from typing import List


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skills = set
        skiller_pepole = [[] for i in range(len(people))]

        for i in range(len(people)):
            skills = set(people[i])
            skiller_pepole[i].append(i)
            for j in range(len(people)):
                sk_set = set(people[j])
                if len(skills) < len((skills | sk_set)):
                    skills = skills | sk_set
                    skiller_pepole[i].append(j)
                if skills == req_skills:
                    skiller_pepole[i].append(j)

        return skiller_pepole[min(map(len, skiller_pepole))]

if __name__ == '__main__':

    s = Solution()
    print(s.smallestSufficientTeam(["java","nodejs","reactjs"], [["java"],["nodejs"],["nodejs","reactjs"]]))
    print(s.smallestSufficientTeam(["algorithms","math","java","reactjs","csharp","aws"], [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]))
    print(s.smallestSufficientTeam(["algorithms","math","java","reactjs","csharp","aws"], [["algorithms"],["math"],["java"],["reactjs"],["csharp"],["aws"],["reactjs","csharp"],["reactjs","java"],["csharp","math"],["aws","java"]]))






    # def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
    #     skills = {}
    #     for i in range(len(req_skills)):
    #         skills[req_skills[i]] = i
    #     people_skills = []
    #     for i in range(len(people)):
    #         people_skills.append([])
    #         for j in range(len(people[i])):
    #             people_skills[i].append(skills[people[i][j]])
    #     people_skills.sort(key=lambda x: len(x))
    #     result = []
    #     for i in range(len(people_skills)):
    #         if self.check(people_skills, i, result):
    #             result.append(i)
    #     return result
    #
    # def check(self, people_skills, i, result):
    #     if i in result:
    #         return True
    #     for j in range(len(people_skills[i])):
    #         if not self.check(people_skills, people_skills[i][j], result):
    #             return False
    #     return True