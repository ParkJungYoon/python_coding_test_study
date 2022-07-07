def solution(id_list, report, k):
    report_dict = {}
    for i in report:
        reporter, target = i.split()
        if target not in report_dict.keys():
            report_dict[target] = [reporter]
        elif reporter not in report_dict[target]:
            report_dict[target].append(reporter)
            
    result = {}
    for j in id_list:
        result[j] = 0

    for m in id_list:
        if m in report_dict.keys() and len(report_dict[m]) >= k:
            for n in report_dict[m]:
                result[n] += 1
    
    return list(result.values())

# 또 다른 풀이

# def solution(id_list, report, k):
#     answer = [0] * len(id_list)    
#     reports = {x : 0 for x in id_list}

#     for r in set(report):
#         reports[r.split()[1]] += 1

#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1

#     return answer