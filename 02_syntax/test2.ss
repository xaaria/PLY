range _windowstart = range OUTDATA'A1..OUTDATA'A8 ... Range defining where averaging window starts ...

print_scalar !2 hours (7200)! To_seconds[ 2.0, 0.0 ]

scalar variable = 0.0 + 2334.3
print_scalar !Hello world! variable


... min & max in sheet ...

range _windowstart = range OUTDATA'A1..OUTDATA'A8 ... Range defining where averaging window starts ...
range _windowend = _windowstart[0,2] ... Window ends 2 rows below the start ...
range _avgresult = _windowstart[1,1]  ... Calculate results to the right of the middle of input data ...
range _window

OUTDATA := INDATA

print_scalar !1 hour 3 minutes (3780)! To_seconds[1.0,3.0]
print_scalar !2 hours (7200)! To_seconds[ 2.0, 0.0 ]
print_scalar !zero (0)! To_seconds[0.0, 0.0 ]

... min & max in sheet ...

return 4.0
print_scalar 3.0
