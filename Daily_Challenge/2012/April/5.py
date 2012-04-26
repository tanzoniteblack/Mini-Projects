# 0 means locker is closed, 1 means locker is open
lockers = [-1 for x in range(1, 1001)]
print(lockers)

for student in range(1, 1001):
    for locker in range(0, 1000, student):
        lockers[locker] *= -1

opened_count = 0
opened_pos = []
for pos, locker in enumerate(lockers):
    if locker == 1:
        opened_count += 1
        opened_pos.append(pos)

print(opened_count)
print(opened_pos)
