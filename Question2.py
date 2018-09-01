import webbrowser

watch = input('Enter (Y/N) to watch a video recommended by me: ')
if watch is 'Y':
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=GBejmOUoG_I')
    print('\t\tThank You For Watching the Video.')
elif watch is 'N':
    print('\t\tSome other time then.')
else:
    print('\t\tERROR!! Invalid Input')
