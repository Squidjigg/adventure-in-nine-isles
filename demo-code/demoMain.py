header = ' Welcome...'
header1 = ' to...'
whiteSp = ''
title = ' ADVENTURE IN NINE ISLE'
print(f'-{whiteSp:-^48}-')
print(f'-{header:<48}-')
print(f'-{header1:<48}-')

i = 0
while i < 4:
    print(f'-{whiteSp:-^48}-')
    i = i + 1

    if i == 2:
        print(f'-{title:<48}-')
        #print(f'-{title[0]:<48}-')

    #if i == 2:
     #    print(f'-{title[1]:<48}-')

    #if i == 3:
     #   print(f'-{title[2]:<48}-')

    #if i == 4:
     #   print(f'-{title[3]:<48}-')