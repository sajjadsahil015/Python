import decimal

with decimal.localcontext() as ctx:
    ctx.prec = 3
    print(decimal.Decimal(1)/decimal.Decimal(3))