_ends := _rangeIDENT[2,0]

sheet X = {
    1.0
    5.5
}

sheet DAT = {
    21.0, 99.0
    99.1, 11.1
    3.0, 6.0, 9.0, 0.0
    3.2, 6.0, 9.0, 0.0
}

range _starts
range _ends
range _sums
range _sumrange

print_sheet !Direct sums! DATA


... _starts := range DATA'A1..DATA'A3 ...




... The same with ranges ...




print_sheet !For sums! DATA