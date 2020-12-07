# define text in title crawl
header = ' Welcome...'
header1 = ' to...'
whiteSp = ''
title = ' ADVENTURE IN NINE ISLES'

# print lines and title crawl 
print(f'-{whiteSp:-^48}-')
print(f'-{header:<48}-')
print(f'-{header1:<48}-')

# loop for lines and main title
i = 0
while i < 4:
    print(f'-{whiteSp:-^48}-')
    i = i + 1

    if i == 2:
        print(f'-{title:<48}-')