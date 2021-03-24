# define direction inputs
dirShort = ['n','s','e','w']
dirLong = ['north','south','east','west']

# clear direction value
userDir = ' '

# continue until valid direction entered
while userDir != dirShort or dirLong:
    userDir = input('Which way do you want to go?: ')

    if userDir == dirShort[0] or userDir == dirShort[0].capitalize() or userDir == dirLong[0] or userDir == dirLong[0].capitalize():
        print('Go NORTH')
        navDir = 'N'
        break
    elif userDir == dirShort[1] or userDir == dirShort[1].capitalize() or userDir == dirLong[1] or userDir == dirLong[1].capitalize():
        print('Go SOUTH')
        navDir = 'S'
        break
    elif userDir == dirShort[2] or userDir == dirShort[2].capitalize() or userDir == dirLong[2] or userDir == dirLong[2].capitalize():
        print('Go EAST')
        navDir = 'E'
        break
    elif userDir == dirShort[3] or userDir == dirShort[3].capitalize() or userDir == dirLong[3] or userDir == dirLong[3].capitalize():
        print('Go WEST')
        navDir = 'W'
        break
    else:
        print('Not a valid direction, try again.')
