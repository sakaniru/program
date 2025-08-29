class IO:
    s=["console","file"]
    def read(sr):
        if sr not in IO.s:
            print("not in")
        else:
            print("Read from",sr)

print(IO.s)
IO.read("file")
IO.read("internet")