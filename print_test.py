'''
    given any input, print a frame around it
'''
INPUT_STR = "He's a naught boy!"
SCREEN_WIDTH = 80
TEXT_WIDTH = len(INPUT_STR)
BOX_WIDTH = TEXT_WIDTH + 6
LEFT_MARGIN = (SCREEN_WIDTH - BOX_WIDTH) // 2

print
print ' ' * LEFT_MARGIN + "+" + "-" * (BOX_WIDTH - 4) + "+"
print ' ' * LEFT_MARGIN + '| ' + ' ' * TEXT_WIDTH + ' |'
print ' ' * LEFT_MARGIN + '| ' + INPUT_STR + ' |'
print ' ' * LEFT_MARGIN + '| ' + ' ' * TEXT_WIDTH + ' |'
print ' ' * LEFT_MARGIN + '+' + '-' * (BOX_WIDTH - 4) + '+'
print


