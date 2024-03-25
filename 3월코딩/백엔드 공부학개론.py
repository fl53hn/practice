# 가위바위보
# https://www.youtube.com/watch?v=m14CzR7iwts
# 미니 프로젝트 만들기
import random

print("어떤 프로젝트를 선택하시나요?")
A_answer = input("1 : 가위바위보, 2 : 구구단 출력기, 3 : 계산기 \n")

if A_answer == "1":
    print("가위바위보")
    def COM_RocksissorPaper():
        RCP = input("가위, 바위, 보 중에 하나를 적어주세요 \n")
        Com_RCP = random.choice(["가위", "바위", "보"])
        if RCP == "가위":
            if Com_RCP == "가위":
                print("비기셨습니다.")
                COM_RocksissorPaper()
            if Com_RCP == "바위":
                print("지셨습니다. ㅋㅋ")
                COM_RocksissorPaper()
            if Com_RCP == "보":
                RCP_ans = input("이기셨습니다. 쳇\n 한번 더 하실 거면 1을 입력해주세요")
                if RCP_ans == "1":
                    COM_RocksissorPaper()
                else:
                    return 0

        if RCP == "바위":
            if Com_RCP == "가위":
                RCP_ans = input("이기셨습니다. 쳇\n 한번 더 하실 거면 1을 입력해주세요")
                if RCP_ans == "1":
                    COM_RocksissorPaper()
                else:
                    return 0
            if Com_RCP == "바위":
                print("비기셨습니다.")
                COM_RocksissorPaper()
            if Com_RCP == "보":
                print("지셨습니다. ㅋㅋ")
                COM_RocksissorPaper()
        if RCP == "보":
            if Com_RCP == "가위":
                print("지셨습니다. ㅋㅋ")
                COM_RocksissorPaper()
            if Com_RCP == "바위":
                RCP_ans = input("이기셨습니다. 쳇\n 한번 더 하실 거면 1을 입력해주세요")
                if RCP_ans == "1":
                    COM_RocksissorPaper()
                else:
                    return 0
            if Com_RCP == "보":
                print("비기셨습니다.")
                COM_RocksissorPaper()
    COM_RocksissorPaper()



elif A_answer == "2":
    print("구구단 출력기")
    NNCalculatior = input("원하는 단을 알려주세요")


elif A_answer == "3":
    print("계산기")
else:
    print("1, 2, 3 과 같은 형식으로 적어주세요")


