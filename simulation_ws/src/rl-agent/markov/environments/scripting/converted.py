X = '''
1394.00,793.67 1216.73,869.56 1177.00,888.00
1141.50,905.04 1040.83,950.50 1018.00,1009.00
999.83,1051.00 951.00,1058.33 927.67,1038.00
904.33,1017.67 859.00,964.00 813.00,945.50
767.00,930.00 577.50,905.50 492.00,894.00
429.00,890.00 345.50,886.00 266.00,891.50
'''
origin = (1483, 791)
unitToPixel = 28
 
points = [((1474.83 - origin[0]) / unitToPixel, (793.58 - origin[1]) / unitToPixel)]
specials = []
x = X.splitlines()
x = x[1:]
for y in x:
    temp = y.split(' ')
    counter = 0
    for z in temp:
        b = z.split(',')
        newX = (float(b[0]) - origin[0]) / unitToPixel
        newY = - (float(b[1]) - origin[1]) / unitToPixel
        counter += 1
        points.append((newX, newY))
        if counter == 3:
            specials.append((newX, newY))
 
 
print(points)
print(specials)