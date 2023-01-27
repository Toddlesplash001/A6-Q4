def Pangramcheck(str):
     
     count = 0
     for i in range (97,123):
          if chr(i) in str:
             count = count+1
     if count == 26:
         print("Pangram")
     else:
         print("Not")
Pangramcheck("The quick brown fox jumps over the lazy dog")
Pangramcheck("jndvdsjvnhfdjbvfjvs")



