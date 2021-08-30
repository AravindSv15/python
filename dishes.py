indian=["samosa","chaat","dal","paneer"]
chinese=["noodle","manchurian","soup"]
italian=["pasta","pizza"]

dish=input("enter a dish name")
if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("i don't know the cuisine")
