sheet INDATA = { 2.0, 34.3 }
range _windowstart = range OUTDATA'A1..OUTDATA'A8 ... Range defining where averaging window starts ...
range _windowend = _windowstart[0,2] ... Window ends 2 rows below the start ...
range _avgresult = _windowstart[1,1]  ... Calculate results to the right of the middle of input data ...
range _window

OUTDATA := INDATA
print_sheet OUTDATA


OUTDATA := INDATA
print_sheet OUTDATA
print_sheet OUTDATA

