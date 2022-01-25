def solution(records):
    answer = []

    uids = {}
    for record in records:
        splitted = record.split(" ")
        if splitted[0] == "Enter":
            uids[splitted[1]] = splitted[2]
            answer.append((splitted[1], "{0}님이 들어왔습니다."))
        if splitted[0] == "Leave":
            answer.append((splitted[1], "{0}님이 나갔습니다."))
        if splitted[0] == "Change":
            uids[splitted[1]] = splitted[2]

    answer = [
        message.format(uids[uid])
        for uid, message in answer
    ]
    return answer
