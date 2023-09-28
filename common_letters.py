from collections import Counter
def common_letters(input1, input2):

   s1 = Counter(input1)
   s2 = Counter(input2)
  
   for char, count in string.items():
      if (count > 1):
         print(char)

def commonfun(input1, input2):
    return(len((set(input1)).intersection(set(input2))))

if __name__ == "__main__":
   input1 = raw_input("Birinci satiri girin: ")
   input2 = raw_input("Ikinci satiri girin: )

   num_common =commonfun()
   print("Satirlardaki ayni harlerin sayisi: ", num_common)
   common_letters(input1, input2)
