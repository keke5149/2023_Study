from string import ascii_uppercase
alpha = list(ascii_uppercase)
dic = {} #걍 alpha 리스트 그대로 쓰기;
for i in range(1, 27):
	dic[i] = alpha[i-1]
user_input = input()

def solution(user_input):
	global dic
	count = 1
	answer = []
	
	if user_input[0] == '1':
		answer.append('1')
	
	for i in range(len(user_input)-1):
		if user_input[i] == user_input[i+1]:
			count += 1
		else:
			answer.append(dic[count])
			count = 1
	answer.append(dic[count])
	return ''.join(answer)

print(solution(user_input))