### A simple python binary calculator to use DMX Address Dip Switches
It can convert binary to decimal and vice versa.

A dip switch allows us to enter a DMX Address on our fixtures. Is a simple binary way to get any number. When a pin is ON it counts as a 1, when it is OFF it counts as a 0 (Activated or deactivated).
For DMX is common to find DipSwitches that have 9 pins to address and another one that activates "auto mode". 

Because each pin has a value when it is switch to ON position from 1 to 256 --> 1 2 4 8 16 32 64 128 256, we can get with these 9 pins 511 different addresses. Some brands use the 10th pin to set the number 512, but only when a channel can be used in that fixture, so it's no so common to find it in the wild.

###  How it works?
When the script runs, it asks us for what do you want to convert, from binary (positions of dipswitch pins) to decimal (number) or vice versa.

From binary to decimal it shows us the number. From decimal to binary it shows us the pins that we must active.

Position of the Dip switch is always from left to right (from 1 to 256, from pin 1 to pin 9.

'c' clear the screen on mac, ios, linux and android. This feature has sense using the for loop that allow us to get 50 addresses (useful when changing addresses on several fixtures at once).
windows users must change "clear" for "cls":
`os.system("cls")`
