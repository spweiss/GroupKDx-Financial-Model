import rates, volumes, sales

# Sums sale volume for a particular test and clinic type over a five-year range
def SaleVolume(rate, volume, sale):
  resultlist = []
  result = 0
  clinics = 0
  for x in range(0,5):
    if sale[x] == 0:
      resultlist.append(0)
    else:
      for y in range(0,12):
        clinics += sale[x]
        result += volume*rate*clinics
      resultlist.append(result)
  return resultlist

# Finds sale volumes for each test-clinic combination

lft_hep = SaleVolume(rates.lft_hep, volumes.hep, sales.hep)
lft_prim = SaleVolume(rates.lft_prim, volumes.prim, sales.prim)
lft_gyn = SaleVolume(rates.lft_gyn, volumes.gyn, sales.gyn)
lft_urg = SaleVolume(rates.lft_urg, volumes.urg, sales.urg)

cmp_hep = SaleVolume(rates.cmp_hep, volumes.hep, sales.hep)
cmp_prim = SaleVolume(rates.cmp_prim, volumes.prim, sales.prim)
cmp_gyn = SaleVolume(rates.cmp_gyn, volumes.gyn, sales.gyn)
cmp_urg = SaleVolume(rates.cmp_urg, volumes.urg, sales.urg)

card_hep = SaleVolume(rates.card_hep, volumes.hep, sales.hep)
card_prim = SaleVolume(rates.card_prim, volumes.prim, sales.prim)
card_gyn = SaleVolume(rates.card_gyn, volumes.gyn, sales.gyn)
card_urg = SaleVolume(rates.card_urg, volumes.urg, sales.urg)

cbc_hep = SaleVolume(rates.cbc_hep, volumes.hep, sales.hep)
cbc_prim = SaleVolume(rates.cbc_prim, volumes.prim, sales.prim)
cbc_gyn = SaleVolume(rates.cbc_gyn, volumes.gyn, sales.gyn)
cbc_urg = SaleVolume(rates.cbc_gyn, volumes.gyn, sales.gyn)

lip_hep = SaleVolume(rates.lip_hep, volumes.hep, sales.hep)
lip_prim = SaleVolume(rates.lip_prim, volumes.prim, sales.prim)
lip_gyn = SaleVolume(rates.lip_gyn, volumes.gyn, sales.gyn)
lip_urg = SaleVolume(rates.lip_urg, volumes.urg, sales.urg)

gc_hep = SaleVolume(rates.gc_hep, volumes.hep, sales.hep)
gc_prim = SaleVolume(rates.gc_prim, volumes.prim, sales.prim)
gc_gyn = SaleVolume(rates.gc_gyn, volumes.gyn, sales.gyn)
gc_urg = SaleVolume(rates.gc_urg, volumes.urg, sales.urg)

# Sums the sales for each test across clinic types
def Compile(list1, list2, list3, list4):
  resultlist = []
  for x in range(0,4):
    resultlist.append(list1[x]+list2[x]+list3[x]+list4[x])
  return resultlist

# Finds the sale volumes for each test
lft_sales = Compile(lft_hep, lft_prim, lft_gyn, lft_urg)
cmp_sales = Compile(cmp_hep, cmp_prim, cmp_gyn, cmp_urg)
card_sales = Compile(card_hep, card_prim, card_gyn, card_urg)
lft_sales = Compile(lft_hep, lft_prim, lft_gyn, lft_urg)
lft_sales = Compile(lft_hep, lft_prim, lft_gyn, lft_urg)
lft_sales = Compile(lft_hep, lft_prim, lft_gyn, lft_urg)

# Finds the total sale volume for each year
total_sales = []
for x in range(0,5):
  total_sales.append(lft_sales[x]+cmp_sales[x]+card_sales[x]+cbc_sales[x]+lip_sales[x]+gc_sales[x])

# Finds the total revenue in each year using the 12 USD panel price
total_revenue = []
for x in range(0,5):
  total_revenue.append(total_sales[x]*12)
