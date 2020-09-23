... min & max in sheet ...

sheet S = {
    -9.0 3.0 3.0 1.0 9.0 3.0 5.0 -4.0 8.0 7.0 6.0 6.0
}

scalar min = 999.0
scalar max = -999.0

for range S'A1..S'A12
do
  if $ < min then
    min := num
  else if $ > max then
    max := num
       endif
  endif
done

print_scalar !Min! min
print_scalar !Max! max