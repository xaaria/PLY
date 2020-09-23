sheet SS = 10 * 1 ... Sheet of size 10 columns and 1 row ...

subroutine Init[XX:sheet] is
  scalar ii = 1.0
  range _rng = range SS'A1..SS'J1
  for _rng
  do
    $ := ii
    ii := ii + 1.0
  done
end

Init[SS]
print_sheet !Numbers 1-10! SS