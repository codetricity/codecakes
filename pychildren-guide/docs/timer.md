## Time

- calculate time elapsed since game started with `pygame.time.get_ticks()`. This must be in the main while loop
- Convert elapsed time from milliseconds to seconds by diving by 1000.0
- Make number shorter by using `round()`
- Convert number to string with `str()`

### Calculate Elaposed time
You can get the time elapsed since the game was started 
with `pygame.time.get_ticks()`

The example below does not bring up the the pygame window. It will only output text to the terminal. You must start your program from the terminal, not from the play button.


    import pygame
    pygame.init()

    while True:
        print(pygame.time.get_ticks())

Run the python program from the terminal.

![](img/timer/pythonTimer.png)

Do not press the play button.

![](img/timer/noPlay.png)

To stop the program, press CTRL-c.

> NOTE: if CTRL-C doesn't work, you may need run Python from a command prompt or bash shell

![](img/timer/milli.png)

### Convert from millisecond to seconds

`pygame.time.get_ticks()` will return 
a long number with a lot of digits. To covert 
the milliseconds to seconds, divide the
number by 1000.0

    timer_number = pygame.time.get_ticks() / 1000.0

**Example**

    import pygame
    pygame.init()

    while True:
        print(pygame.time.get_ticks()/1000.0)

This will display elapsed time with too many decimal places.

![](img/timer.png)

### Show only first decimal place

First, assign timer to a variable.

    import pygame
    pygame.init()

    while True:
        timer_number = pygame.time.get_ticks() / 1000.0
        print(timer_number)

![](img/timer/timer_number.png)

You now need to round it the time to only one decimal place. 
Use the new python command `round`*(number, decimal places)*.

    import pygame
    pygame.init()

    while True:
        timer_number = pygame.time.get_ticks() / 1000.0
        timer_one_decimal = round(timer_number, 1)
        print(timer_one_decimal)



![](img/timer/one_decimal.png)

### Convert Number to String

Before you can blit the time to the screen, you will need 
to convert the number into a string.

    timer_string = str(timer_one_decimal)

The complete code you need to get a string for the elapsed time with one 
decimal place is shown below.

    import pygame
    pygame.init()

    while True:
        timer_number = pygame.time.get_ticks() / 1000.0
        timer_one_decimal = round(timer_number, 1)
        timer_string = str(timer_one_decimal)
        print(timer_string)

### Display Timer

You can now combine the previous lesson that showed
you how to display text on the screen with the 
timer string code in this lesson.

    timer_surface = timer_font.render("Time : " + timer_string, True, YELLOW)
        
    DISPLAY.blit(timer_surface, (0,0))

Remember to blank out the screen each cycle before you blit elements.


![](img/timerDisplay.gif)
