INPUT = 4734
KEY_PAD_MAPPING = {
    '2': "ABC",
    '5': "JKL",
    '8': "TUV",
    '3': "DEF",
    '6': "MNO",
    '9': "WXY",
    '4': "GHI",
    '7': "PRS"
    }

result = ['']
for c in str(INPUT):
    if c not in KEY_PAD_MAPPING:
        raise RuntimeError("Number " + c + " not found in key pad mapping.")
    lookupLetters = KEY_PAD_MAPPING[c]
    print("result=", result)
    print("lookupLetters=", lookupLetters)
    result = result * 3 # duplicate 3 times
    resultLen = len(result)
    cur = 0 # current set position
    for l in lookupLetters:
        for i in range(resultLen // 3):
            result[cur] = result[cur] + l # Use char list could be more efficient
	    print("i=", i, " l=", l, " cur=", cur, " result=", result)
            cur += 1

result.sort()
print(result)
