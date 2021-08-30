def open_file():
    try:
        f=open("C://pycharmpractice//funny.txt","w")
        x=1/0
    except FileNotFoundError as e:
        print("check the path")
    finally:
        f.close()