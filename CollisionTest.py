def TestCollision(sprite1, sprite2):
    if sprite1.rect.right+5 >= sprite2.rect.left and sprite1.rect.right <= sprite2.rect.left + 5:
        return "right"
    if sprite1.rect.left + 5 >= sprite2.rect.right and sprite1.rect.left <= sprite2.rect.right + 5:
        return "left"
    if sprite1.rect.top + 5 >= sprite2.rect.bottom and sprite1.rect.top <= sprite2.rect.bottom + 5:
        return "top"
    if sprite1.rect.bottom + 5 >= sprite2.rect.top and sprite1.rect.bottom <= sprite2.rect.top + 5:
        return "bottom"

    return "None"