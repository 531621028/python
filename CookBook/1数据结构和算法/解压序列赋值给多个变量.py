data = ['ACME',50,91.1,(2012,12,21)]
name, shares, price, date = data
print(date)
name,shares,price,(year,mom,day) = data
print(year)
#有时候，你可能只想解压一部分，丢弃其他的值。对于这种情况Python并没有提供特殊的语法。 
#但是你可以使用任意变量名去占位，到时候丢掉这些变量就行了。
_,shares,price,_ = data
print(shares)