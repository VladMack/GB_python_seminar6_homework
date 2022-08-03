def same_by(characteristic, object):
    for i in object:
        for j in object:
            if characteristic(i) != characteristic(j):
                return False
    return True


values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
