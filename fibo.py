def fibo(num):
    num1 = 0
    num2 = 1
    for i in range(num):
        yield num1
        temp = num1
        num1 = num2
        num2 = temp + num2

def main():
    fibo_seq = []
    for n in fibo(16):
        fibo_seq.append(n)
    print(f"fibonacci sequence = {fibo_seq}")
        
        
if __name__ =="__main__":
    main()