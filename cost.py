import revenue, math

# Determines the cost due to technicians each year where one can make 840000 devices per year and is paid 36,000 USD
techs = []
for x in range(0,5):
  techs.append(36000*math.ceil(revenue.total_sales/840000))

# Determines the cost of production each year where unit production cost is 2 USD
material = []
for x in range(0,5):
  material.append(2*revenue.total_sales)

# Determines the cost due to sales representatives each year where each is paid 36,000 USD
sales = [0,1,2,4,5]
for x in range(0,5):
  sales[x] = sales[x]*2

# Finds the total cost each year
total_cost = []
for x in range(0,5):
  total_cost.append(techs[x]+material[x]+sales[x])
