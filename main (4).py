p







def linearsearchproduct(product list,targetproduct):
  indices =[]

for index,product in enumerate (productlist):
  if product ==targetproduct:
    indices.append(index)

return  indices 


#Example  usage:
product=["shoes","boot","loafer","shoes","sandal","shoes"]
target = "shoes"
target2 = "apple"
result  = linearsearchproduct (products,target)
print (result))