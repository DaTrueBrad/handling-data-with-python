invoice = open('CupcakeInvoices.csv')

for line in invoice:
    print(line)

invoice.close()


invoice = open('CupcakeInvoices.csv')

for line in invoice:
    line = line.rstrip('\n').split(',')
    print(line[2])

invoice.close()

invoice = open('CupcakeInvoices.csv')

total = 0
for line in invoice:
    line = line.rstrip('\n').split(',')
    total += (round(float(line[3]) * float(line[4]), 2))

print(f"Total is {round(float(total), 2)}")