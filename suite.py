def fibo(limit):
        x = 0
        y = 1
        res = 0
        while y <= limit:
                res =  x + y
                print str(x) + " +" + str(y) + " =" + str(res)
                x = y
                y = res


def main():
        fibo(int(raw_input("Limit :")))
        
main()
