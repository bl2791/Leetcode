class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for word in strs:
            a = ''.join(sorted(word))
            if a in dic.keys():
                dic[a].append(word)
            else:
                dic[a] = [word]
        result = []
        for i in dic:
            result.append(dic[i])
        return result


# Another solution:
# Use collection.defaultdict(list)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = collections.defaultdict(list)
        for s in strs:
            m[''.join(sorted(s))].append(s)
        return list(m.values())