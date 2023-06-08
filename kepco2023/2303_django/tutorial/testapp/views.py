from django.shortcuts import render

# 라이브러리 추가
from django.http import HttpResponse

# Create your views here.

# 테스트 페이지 만들기
def test(request):
	msg="""
		<h3>웹프로그램 성공~~!</h3>
		<table border='1'>
			<caption>성공하면 나타나는 표</caption>
			<tr>
				<th>아이디</th>
				<th>패스워드</th>
			</tr>
			<tr>
				<td>a01</td>
				<td>pw01</td>
			</tr>
		</table>
"""

return HttpResponse(msg)