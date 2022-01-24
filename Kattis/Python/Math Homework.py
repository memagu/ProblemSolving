# bird_legs, dog_legs, cat_legs, total_legs = map(int, input().split())
# results = []
#
# bird_amount = 0
# while bird_amount * bird_legs <= total_legs:
#     dog_amount = 0
#
#     while dog_amount * dog_legs + bird_amount * bird_legs <= total_legs:
#         cat_amount = 0
#
#         while dog_amount * dog_legs + bird_amount * bird_legs + cat_amount * cat_legs <= total_legs:
#             if bird_amount * bird_legs + dog_amount * dog_legs + cat_amount * cat_legs == total_legs:
#                 results.append((bird_amount, dog_amount, cat_amount))
#
#             cat_amount += 1
#
#         dog_amount += 1
#
#     bird_amount += 1
#
# if results:
#     for result in results:
#         print(" ".join(map(str, result)))
#
# else:
#     print("impossible")
#
#

b_legs, d_legs, c_legs, tot_legs = map(int, input().split())
results = []

bird_amt = 0
while bird_amt * b_legs <= tot_legs:
    dog_amt = 0

    while dog_amt * d_legs + bird_amt * b_legs <= tot_legs:
        cat_amt = 0

        while dog_amt * d_legs + bird_amt * b_legs + cat_amt * c_legs <= tot_legs:
            if bird_amt * b_legs + dog_amt * d_legs + cat_amt * c_legs == tot_legs:
                results.append((bird_amt, dog_amt, cat_amt))

            cat_amt += 1

        dog_amt += 1

    bird_amt += 1

if results:
    for result in results:
        print(" ".join(map(str, result)))

else:
    print("impossible")
