def longestCommonPrefix(strs: [str]) -> str:
    prefix = strs[0]
    for s in strs[1:]:
        for i in range(len(prefix)):
            if not prefix:
                return prefix
            if i > len(s) - 1:
                prefix = prefix[:i]
                break
            if prefix[i] != s[i]:
                prefix = prefix[:i]
                break

    return prefix