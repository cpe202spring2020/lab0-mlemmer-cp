def weight_on_planets():
   earthWeight=float(input("What do you weigh on earth? "))

   mars=("\nOn Mars you would weigh %.2f pounds." %(earthWeight*0.38))
   jupiter=("\nOn Jupiter you would weigh %.2f pounds." %(earthWeight*2.34))

   print(mars, jupiter, sep='')
if __name__ == '__main__':
   weight_on_planets()