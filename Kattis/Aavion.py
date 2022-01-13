# strings = [input(),input(),input(),input(),input()]
# blimps = []
# row = 0
#
# for string in strings:
#   row += 1
#   if "FBI" in string:
#     blimps.append(str(row))
#
# if len(blimps) > 0:
#   print(' '.join(blimps))
# else:
#   print("HE GOT AWAY!")

out = ""

for i in range(5):
  if "FBI" in input():
    out += str(i + 1) + " "

if out == "":
  print("HE GOT AWAY!")
else:
  print(out[:-1])
