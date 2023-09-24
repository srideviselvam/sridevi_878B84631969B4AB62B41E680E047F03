def linearsearchproduct(productlist,targetproduct):
  indices = [] 
  
  for intex, product in enumerate( productlist):
    if product ==  targetproduct:
      indices.append(intex)

  return indices

product =["shoes","boot","loafer","shoes","sandal","shoes"]
target= "shoes"
result= linearsearchproduct(product,target)
print(result)
      