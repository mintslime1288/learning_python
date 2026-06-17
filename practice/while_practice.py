'''treehits=0;
while treehits<10:
    treehits=treehits+1
    print("나무를 %d번 찍었습니다." % treehits);
    if treehits==10:
        print("나무 넘어갑니다.");'''

'''prompt="""
1. add
2. del
3.list
4.quit

enter number : """;
number=0;
while number !=4:
    print(prompt)
    number=int(input())'''

'''coffee=10;
money=300;
while money:
    print("돈을 받았으니 커피를 줍니다.");
    coffee = coffee -1
    print("남은 커피의 양은 %d개 입니다."%(coffee))
    if coffee ==0:
        print("남은 커피의 갯수가 없습니다. 판매를 중지합니다.")
        break'''

money=int(input("얼마를 가지고 있습니까?"));
americano=10;
latte=10;
cappucchino=10;
espresso=10;
while money:
    print("커피 자판기 오픈했습니다. 무엇을 주문하시겠습니까? : ")
    print("1. 아메리카노 - 300원\n2. 라떼 - 400원\n3. 카푸치노 - 400원\n4. 에스프레소. - 200원\n  ")
    dicision=int("무엇을 주문하시겠습니까? : ")
    if dicision == 1:
        print("아메리카노 주문 받았습니다.")
        americano=americano-1
        print("아메리카노 %d개 남았습니다."%(americano))
    elif dicision ==2:
        print("라떼 주문 받았습니다.")
        latte=latte-1
        print("라떼 %d")
    