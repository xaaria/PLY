... Create a sheet and add a sliding average ...

sheet INDATA = { 1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0 10.0 } ... Heehee, nice way to create a row vector in our syntax! ...
sheet OUTDATA = 10 * 2

function Average[_rng : range] return scalar is
  scalar avgtmp = 0.0
  for _rng do
    avgtmp := avgtmp + $
  done
  return avgtmp / #_rng ... # gives the size of a range ...
end

range _windowstart = range DATA'A1..DATA'A7 ... Range defining where averaging window starts ...
range _windowend = _windowstart[2,0] ... Window ends 2 columns to the left of start ...
range _avgresult = _windowend[0,1]  ... Calculate results one row below input data ...
range _window

OUTDATA := INDATA

for _windowstart,_windowend,_avgresult do
  _window := range $:_windowstart .. $:_windowend ... Averaging window is from start to end ...
  $:_avgresult := Average[_window]
done

print_sheet DATA