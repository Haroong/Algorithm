import sys

# 각 원자의 질량을 반환한다
def get_element_value(atom):
    if atom == HYDROGEN:
        result = 1
    elif atom == CARBON:
        result = 12
    else: 
        result = 16 # OXYGEN

    return result


# 화학식으로 화학식량을 계산한다
def get_total_chemical_weight(chemical_formula):
    stack = []

    for index, value in enumerate(chemical_formula):
        if value == OPEN_BRACKET:
            stack.append(value) 
        elif value == CLOSE_BRACKET:
            popped_result = 0

            while True:
                top = stack.pop()
                if top == OPEN_BRACKET:
                    break
            
                popped_result += top

            stack.append(popped_result)

        elif str.isdigit(value): # 숫자
            stack.append(stack.pop() * int(value)) # 스택 top 원소에 현재 값을 곱함
        else: # 알파벳
            stack.append(get_element_value(value))     

    return sum(stack)


# main
if __name__ == '__main__':
    chemical_formula = list(sys.stdin.readline().rstrip()) # 화학식
    
    HYDROGEN = 'H'
    CARBON = 'C'
    OXYGEN = 'O'
    OPEN_BRACKET = '('
    CLOSE_BRACKET = ')'
    CHEMICAL_ELEMENTS = [HYDROGEN, CARBON, OXYGEN]
    
    answer = get_total_chemical_weight(chemical_formula) #화학식량 구하기
    print(answer)