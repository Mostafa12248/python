input = open("string.txt" , "rt")
output = open("string_output.txt", "wt")

value = ""
for line in input:
   if line.strip() == "I":
      value += " " + line.strip()
   elif line.strip() == "Almdrasa":
      value += " " + line.strip()
   else: 
      value += " " + line.strip().lower()    
print(value.strip() , file=output)
output.close()
