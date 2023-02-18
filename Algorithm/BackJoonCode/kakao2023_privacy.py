#문자열 today
#1차원 문자열 배열 terms
#1차원 무자열 배열 privacies
#1차원 정수 배열 반환
from datetime import datetime
from dateutil.relativedelta import relativedelta

def change_date(today):
    return datetime.strptime(today, "%Y.%m.%d")


def check_expired(pp, policy, date):
    date = change_date(date)
    return date + relativedelta(months=policy[pp])

def check_privacies(today, policies, privacies):
    #for index, privacy in enumerate(privacies, start=1):
    result = []
    for privacy in privacies:
        date, p = privacy.split()
        expired = check_expired(p, policy, date)
        if today >= expired:
            result.append(privacies.index(privacy)+1)
    return result
    
def make_dic(terms):
    policy = {}
    for term in terms:
        p, l = term.split()
        policy[p] = int(l)
    return policy

def solution(today, terms, privacies):
    
    today_ = change_date(today)
    policies = make_dic(terms)
    answer = check_privacies(today_, policies, privacies)
    
    return answer