# timer

---

## Challenge

Print number of milliseconds elapsed since game started

![](img/milli.png)

  
* Use `pygame.time.get_ticks()` 
* use Python `print` statement in while loop

---

## Answer on next slide

---



	    import pygame
	    pygame.init()

	    while True:
		    print(pygame.time.get_ticks())


---

## Challenge

Convert from millisecond to seconds

![](img/seconds_float.png)

---

## Answer on next slide

---


	    import pygame
	    pygame.init()

	    while True:
		    print(pygame.time.get_ticks()/1000)
 

---


## Challenge

Reduce floating point number to one decimal place.

![](img/one_decimal.png)

---

## Answer on next slide

---

<code>

    import pygame
    pygame.init()

    while True:
        timer_number = pygame.time.get_ticks() / 1000.0
        timer_one_decimal = round(timer_number, 1)
        print(timer_one_decimal)
		    
</code>

---







