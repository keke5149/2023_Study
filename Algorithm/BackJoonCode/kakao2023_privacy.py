from datetime import datetime
from dateutil.relativedelta import relativedelta

def cal_expire(date, term, term_cases):
    return date + relativedelta(months=term_cases[term])

def calculate_(today_, term_cases, privacies):
    pIdx = []
    for index, privacy in enumerate(privacies, start=1):
        pDate, pTerm = privacy.split()
        pDate = datetime.strptime(pDate, "%Y.%m.%d")
        pExpired = cal_expire(pDate, pTerm, term_cases)
        if today_ >= pExpired:
            pIdx.append(index)
    return pIdx
    
def get_terms(terms):
    term_cases = {}
    for i in terms:
        term_case, term_length = i.split()
        term_cases[term_case] = int(term_length)
    return term_cases

def solution(today, terms, privacies):
    
    today_ = datetime.strptime(today, "%Y.%m.%d")
    term_dic = get_terms(terms)
    answer = calculate_(today_, term_dic, privacies)
    
    return answer