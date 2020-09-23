sheet SS = 1*1


sheet SSS = { 2.0,
 3.4, 4.4--2.0
 }
 sheet BARN = {
... chickens, cows, spiders ...
      4.0+2.3,       2.0,     1.0
}

scalar variable = 0.0 + 2334.3
range _windowstart = range OUTDATA'A1..OUTDATA'A8
range _window

OUTDATA := INDATA




... min & max in sheet ...
print_sheet SS

print_scalar !Hello world! variable
print_scalar !2 hours (7200)! To_seconds[ 2.0, 0.0 ]
return 4.0
print_scalar !Min! min