## Leo Chases Guffy

* Add Leo the Lion
* Chase algorithm
* Add food 
* Change Guffy speed based on food

![](img/lesson04.png)

### Add Leo

Above while loop

    leo = pygame.image.load('img/leo-90.png')

In while loop

    DISPLAY.blit(leo, leor)

### Leo Chases Guffy

This is the x direction.

    if giraffe_rect.centerx < leor.centerx:
        leor.centerx -= 1
    elif giraffe_rect.centerx > leor.centerx:
        leor.centerx += 1

Set up the y direction


### Add food

Above while loop

    icecream = pygame.image.load('img/ice-cream.png')
    icecreamr = pygame.Rect(134, 300, 64, 64)


In while loop

    DISPLAY.blit(icecream, icecreamr)

### Change Guffy's Speed Based on Food Choices

Based on Guffy's dietary choices, his speed will change.
If he eats a dessert, he will slow down.

    if giraffe_rect.colliderect(cupcaker):
        speed = 1

If Guffy eats a fruit or vegetable, his speed increases.

    if giraffe_rect.colliderect(pear):
        speed = 5

## Answer

Full code example in the [answers](answers.md) section.