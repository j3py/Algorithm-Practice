#------------------------------------------------------------------
#BUBBLE SORT  O(n^2)

# use this to run quickly -->  #!/user/local/bin/python  chmod +x merge.py  ./merge 1000

my_list = [100, 23, 24, 348, 43, 98, 1, 40]
	
def bubble(bad_list):
    length = len(bad_list) - 1
    sorted = False
	
    while not sorted:
	    sorted = True
	    for i in range(length):
	        if bad_list[i] > bad_list[i+1]:
	            sorted = False
	            bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]
	
bubble(my_list)
print my_list