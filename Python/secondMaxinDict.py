comp_dict ={"microsoft":19, "google":16, "bing":4, "chrome":9}

max = max(comp_dict.values())

temp = 0
for v in comp_dict.values():
     if(v>temp and v<max):
            temp = v

print(temp)