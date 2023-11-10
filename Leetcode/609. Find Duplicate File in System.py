class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        mapping = {}
        for path in paths:
            tmp = path.split()
            directory, files = tmp[0], tmp[1:]
            for f in files:
                name, content = f.rstrip(')').split('(')
                mapping.setdefault(content, [])
                mapping[content].append(directory + '/' + name)
        result = []
        for k, v in mapping.items():
            if len(v) > 1:
                result.append(v)
        return result
