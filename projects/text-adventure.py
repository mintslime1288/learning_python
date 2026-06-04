genders=int(input("성별을 입력하세요.\n1.남성 \n2.여성\n "));
if genders == 1:
    genders="남성";
else:
    genders="여성";

jobs=int(input("직업을 입력하세요. \n1.검사 \n2.법사 \n3.도적 \n4.사제 \n5.궁수\n "));
if jobs ==1:
    jobs="검사";
    health=100;
    mana=100;
elif jobs==2:
    jobs="법사";
    health=80;
    mana=150;
elif jobs==3:
    jobs="도적";
    health=90;
    mana=80;
elif jobs==4:
    jobs="사제";
    health=80;
    mana=120;
else:
    jobs="궁수";
    health=90;
    mana=110;
print("당신은 깊은 숲 속에서 눈을 떴습니다. 상태창을 열어보니 당신의 직업은 %s 이고 성별은 %s 입니다."% (jobs, genders)); 

print("음... 하지만 여기가 어딘진 잘 모르겠군요. 당신은 길을 선택해야 합니다. \n1. 동쪽 \n 2. 서쪽 \n 3. 남쪽 \n 4. 북쪽\n ");
dicision=int(input("어느 방향으로 가시겠습니까? : "));
if dicision==1:
    print("당신은 동쪽으로 향했습니다. 하지만 슬라임 한 마리가 보입니다.\n 1. 싸운다.\n 2. 도망친다.");
    dicision=int(input("어떤 행동을 하시겠습니까? : "));
    if dicision==1:
        print("당신은 슬라임과 싸워서 이겼습니다. 하지만 체력이 10 감소했습니다. 현재 체력은 %d 입니다."%(health-10));
    else:
        print("당신은 슬라임을 피해 도망쳤습니다. 하지만 돌뿌리에 걸려 넘어져 체력이 5 감소했습니다. 현재 체력은 %d 입니다."%(health-5));
elif dicision==2:
    print("당신은 서쪽으로 향했습니다. 하지만 앞이 낭떠러지 입니다. 뒤에선 괴물이 다가오고 있습니다.\n 1. 낭떠러지로 떨어진다.\n 2. 괴물과 싸운다.");
    dicision=int(input("어떤 행동을 하시겠습니까? : "));
    if dicision==1:
        print("당신은 낭떠러지로 떨어졌습니다. 당신은 죽었습니다.")
        print("게임 오버.");
    else:
        print("당신은 괴물과 싸워서 이겼습니다. 하지만 체력이 20 감소했습니다. 현재 체력은 %d 입니다."%(health-20));
        print("당신은 다시 길을 떠납니다.");
        print("당신은 숲을 빠져나와 마을에 도착했습니다. 어디로 가시겠습니까? \n 1. 여관 \n 2. 마을 광장\n ");
        dicision=int(input("어느 곳으로 가시겠습니까? : "));
        if dicision==1:
           

