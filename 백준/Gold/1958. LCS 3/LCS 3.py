def findLCS(strings):
    str1, str2, str3 = strings
    LCS = [[[0 for _ in range(len(str3) + 1)] for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    length = 0
    for x in range(len(str1)):
        for y in range(len(str2)):
            for z in range(len(str3)):
                if str1[x] == str2[y] and str2[y] == str3[z]:
                    LCS[x + 1][y + 1][z + 1] = LCS[x][y][z] + 1
                    length = max(length, LCS[x + 1][y + 1][z + 1])
                else:
                    LCS[x + 1][y + 1][z + 1] = max(LCS[x][y + 1][z + 1], LCS[x + 1][y][z + 1], LCS[x + 1][y + 1][z])

    return length


def main(strings):
    print(findLCS(strings))


strings = []
for _ in range(3):
    strings.append(input())

main(strings)