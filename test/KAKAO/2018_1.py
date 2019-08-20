# 오픈채팅방
# https://www.welcomekakao.com/learn/courses/30/lessons/42888

res = []
uid_name_dic = {}
cmd_to_kor = {
    'Enter':'들어왔습니다.',
    'Leave': '나갔습니다.'
}

def exec_cmd_and_append(splited):
    global res, uid_name_dic
    
    try:
        cmd, uid, name = splited
    except:
        cmd, uid = splited

    if cmd == 'Enter':
        uid_name_dic[uid] = name

    elif cmd == 'Leave':
        pass

    elif cmd == 'Change':
        uid_name_dic[uid] = name
        return
    
    res.append( (cmd, uid) )
        
        
def res_to_answer():
    return list(map(lambda tpl: "{name}님이 {cmd_kor}".format(name=uid_name_dic[tpl[1]], cmd_kor=cmd_to_kor[tpl[0]]) , res ))

def solution(record):
    
    for line in record:
        splited = line.split()
        exec_cmd_and_append(splited)
    
    return res_to_answer()