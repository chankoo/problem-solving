# 후보키
# https://www.welcomekakao.com/learn/courses/30/lessons/42890

def get_bit_expr(relation):
    cases = []
    num_of_col = len(relation[0])
    
    for deci in range(1, 2**num_of_col-1):  # not for empty nor all
        case = list(map(lambda s:int(s), list('{:04b}'.format(deci))))
        cases.append(case)
    return cases

def get_transpose_relation(relation):
    num_of_col = len(relation[0])
    t_relation = dict.fromkeys(range(num_of_col))
    
    for row in relation:
        for i, val in enumerate(row):
            try:
                t_relation[i].append(val)
            except:
                t_relation[i] = [val, ]
    return t_relation

def is_case_superkey(case, t_relation):
    selected_attrs = []
    num_of_col = len(t_relation.keys())

    for i, is_attr_selected in enumerate(case):
        if is_attr_selected:
            selected_attrs.append(t_relation[i])

        
    print(selected_attrs)
    return True
    

def get_superkey_cases(cases, t_relation):
    super_cases = []
    for case in cases:
        if is_case_superkey(case, t_relation):
            super_cases.append(case)
    return super_cases


def get_candid_cases(cases):
    pass
    
    
def solution(relation):
    answer = 0
    
    cases = get_bit_expr(relation)
    
    t_relation = get_transpose_relation(relation)

    super_cases = get_superkey_cases(cases, t_relation)
    # candid_cases = get_candid_cases(super_cases)
    
    #return len(candid_cases)