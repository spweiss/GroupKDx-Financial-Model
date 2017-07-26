import rates, volumes, sales

# Sums sale volume for a particular test and clinic type over a five-year range based on _______
def SaleVolume(rate, volume, sale):
  resultlist = []
  result = 0
  clinics = 0
  for x in range(0,5):
    if sale[x] == 0:
      resultlist.append(0)
      print "zero year"
    else:
      for y in range(0,12):
        clinics += sale[x]
        result += volume*rate*clinics
      resultlist.append(result)
      print "year finished"
  return resultlist

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

cbc_hep = 0.90
cbc_prim = 0.35
cbc_gyn = 0.00
cbc_urg = 0.024

lip_hep = 0.00
lip_prim = 0.05
lip_gyn = 0.00
lip_urg = 0.006

gc_hep = 0.00
gc_prim = 0.01
gc_gyn = 0.50
gc_urg = 0.002
