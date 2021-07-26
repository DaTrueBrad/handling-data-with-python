from matplotlib import pyplot as plt
invoice = open('CupcakeInvoices.csv')

choc_total = 0
van_total = 0
straw_total = 0


for line in invoice:
    line = line.rstrip('\n').split(',')
    if line[2] == 'Chocolate':
        choc_total += (round(float(line[3]) * float(line[4]), 2))
    elif line[2] == 'Vanilla':
        van_total += (round(float(line[3]) * float(line[4]), 2))
    elif line[2] == 'Strawberry':
        straw_total += (round(float(line[3]) * float(line[4]), 2))


line_x = ['Chocolate', 'Vanilla', 'Strawberry']
line_y = [round(choc_total), round(van_total), round(straw_total)]

plt.bar(line_x, line_y, color=['brown', 'tan', 'pink'])
plt.xlabel('Cupcakes')
plt.ylabel('Money Earned')
plt.title('Money earned from each Cupcake Type')

plt.show()