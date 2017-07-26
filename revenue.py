import rates, volumes, sales

# Sums sale volume for a particular test and clinic type over a five-year range based on _______
def SaleVolume(volume, rate, sale):
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
