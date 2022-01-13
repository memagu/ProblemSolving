#
# sentence = input()
#
# sentence_list = ["_"]
#
# for char in sentence:
#     if char != "":
#         sentence_list += char
#
# count = 0
#
# for index in range(len(sentence_list) - 1):
#     if sentence_list[index:index + 2] == ["a", "e"]:
#         count += 1
#
# if count / len(sentence.split()) >= 0.4:
#     print("dae ae ju traeligt va")
# else:
#     print("haer talar vi rikssvenska")

# Normal

# sentence = input().split()
# count = 0
#
# for index in range(len(sentence)):
#     chars = []
#     for char in sentence[index]:
#         chars += char
#     for index_chars in range(len(chars) - 1):
#         if chars[index_chars:index_chars + 2] == ["a", "e"]:
#             count += 1
#             break
#
# if count / len(sentence) >= 0.4:
#     print("dae ae ju traeligt va")
# else:
#     print("haer talar vi rikssvenska")

# Obfuscated

s = input().split()
ct = 0

for i in range(len(s)):
    cs = []
    for c in s[i]:
        cs += c
    for i_cs in range(len(cs) - 1):
        if cs[i_cs:i_cs + 2] == ["a", "e"]:
            ct += 1
            break

if ct / len(s) >= 0.4:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")