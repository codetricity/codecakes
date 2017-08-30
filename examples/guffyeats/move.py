def onePixel(screen, direction, rect):
    # if checkBounds(screen, direction, rect):
    screen_rect = screen.get_rect()
    if direction == "right":
        if rect.right < screen_rect.right:
            rect.centerx = rect.centerx + 1
    elif direction == "left":
        if rect.left > 0:
            rect.centerx = rect.centerx - 1
    elif direction == "up":
        if rect.top > 0:
            rect.centery = rect.centery - 1
    elif direction == "down":
        if rect.bottom < screen_rect.bottom:
            rect.centery = rect.centery + 1
    return rect
