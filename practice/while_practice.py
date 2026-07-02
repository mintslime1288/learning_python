treehits=0;
while treehits<10:
    treehits=treehits+1
    print("나무를 %d번 찍었습니다." % treehits);
    if treehits==10:
        print("나무 넘어갑니다.");

prompt="""
1. add
2. del
3.list
4.quit

enter number : """;
number=0;
while number !=4:
    print(prompt)
    number=int(input())

'''coffee=10;
money=300;
while money:
    print("돈을 받았으니 커피를 줍니다.");
    coffee = coffee -1
    print("남은 커피의 양은 %d개 입니다."%(coffee))
    if coffee ==0:
        print("남은 커피의 갯수가 없습니다. 판매를 중지합니다.")
        break;'''

coffee=10;
while True:
    money =int(input("돈을 넣어 주세요: "))
    if money==300:
        print("커피를 줍니다.")
        coffee=coffee-1
    elif money>300:
        print("거스름돈 %d원을 주고 커피를 줍니다." %(money-300))
    else:
        print("돈이 부족합니다, 돈을 다시 반환하고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다."%(coffee))
    if coffee==0:
        print("커피가 모자랍니다. 판매를 중지합니다.")
        break;




 
