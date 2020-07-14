## 숫자 야구 게임 
1. 컴퓨터가 0~9사이의 임의의 숫자 3개를 발생한다. (중복을 허용하지 않는다)
2. 사용자로부터 3개의 숫자를 입력 받는다.
    - ex) 123 또는 1,2,3 또는 1 2 3
3. 사용자가 입력한 숫자와 컴퓨터가 발생한 숫자가 일치하는지 검증한다. 
4. 사용자가 입력한 숫자가 컴퓨터가 발생한 숫자에 포함되어 있는지를 검증한다.
    - 숫자의 위치(자리)까지 일치하면 "스트라이크"라고 판정
    - 숫자의 위치를 다르지만, 해당 숫자가 포함되어 있으면 "볼"이라고 판정
    - 전체 판정 결과를 스트라이크와 볼의 숫자로 표현한다. 
    - 해당 숫자가 아무것도 포함되어 있지 않으면, "노 스트라이크, 노 볼"이라고 판정
        - 예) 컴퓨터 숫자 768, 사용자가 입력한 숫자 756 -> 1스트라이크, 1볼
        - 예) 컴퓨터 숫자 456, 사용자가 입력한 숫자 149 -> 0스트라이크, 1볼
        - 예) 컴퓨터 숫자 349, 사용자가 입력한 숫자 125 -> 0스트라이크, 0볼
5. 총 몇번 동안 맞췄는지 결과를 출력해 준다. 
    - 1 ~ 5번 : 당신은 천재입니다.
    - 6 ~ 10번 : 잘 하셨습니다.
    - 11 ~ 15번 : 당신은 더 노력해야 합니다.
    - 15번 ~ : 게임에 소질이 없습니다. 