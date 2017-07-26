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
lft_prim = 0.35
lft_gyn = 0.00
lft_urg = 0.003

cmp_hep = 0.90
cmp_prim = 0.35
cmp_gyn = 0.00
cmp_urg = 0.018

card_hep = 0.00
card_prim = 0.013
card_gyn = 0.00
card_urg = 0.016

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
