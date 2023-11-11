def solution(num_list):
    anaswer = 0
    if num_list[-1] > num_list[-2]:  # 배열[-1] 은 배열의 마지막 값을 의미한다
        num_list.append(num_list[-1] - num_list[-2]) # 배열[-2]는 배열의 맨 뒤에서 두번째 값
    else:        # append함수는 배열의 맨 마지막에 값을 추가해서 넣는 것이다
        num_list.append(2 * num_list[-1])
    return num_list
