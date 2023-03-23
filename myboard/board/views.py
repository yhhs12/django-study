from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Board

# Create your views here.
# views.py의 함수에 들어있는 request 파라미터 : 요청객체
# 게시판 목록보기
def index(request):
    print('index() 실행')
    
    #반환되는 queryset에 대해서 order_by함수 이용하면 특정 필드 기준으로 정렬
    #order_by에 들어가는 필드 이름앞에 -를 붙이면 내림차순(DESC) 아니면 오름차순(ASC)
    board_list = Board.objects.all().order_by('-id')
    
    context = {
        'board_list' : board_list
    }
    
    return render(request, 'board/index.html', context)

def read(request, id):
    board = Board.objects.get(id = id)
    board.view_count += 1
    board.save()
    
    context = {
        'board' : board
    }
    
    return render(request, 'board/read.html', context)

def find_board(request):
    input_title = request.POST["search_title"]
    condition = request.POST["condition"]
    
    find_boardList = []
    if condition == "all":
        #완전 일치
        find_boardList = Board.objects.filter(title = input_title)
    else:
        #부분 일치
        find_boardList = Board.objects.filter(title__contains = input_title)       
    
    
    context = {
        'board_list' : find_boardList
    }

    return render(request, 'board/index.html', context)

def home(request):
    return HttpResponseRedirect('/board/')


def write(request):
    if request.method == 'GET': #요청방식이 GET이면 화면표시
        return render(request, 'board/board_form.html')
    else: #요청방식이 POST일 때 할일 , 폼의 데이터를 DB에 저장
        
        #현재 세션정보의 writer라는 키를 가진 데이터 취득
        title = request.POST['title']
        content = request.POST['content']
        
        session_wrtier = request.session.get('writer')
        if not session_wrtier: # 세션에 정보가 없는 경우
            #폼에서 가져온 writer 값 저장
            request.session['writer'] = writer
        print(session_wrtier)        
        
       #객체.save()
        #board = Board(
        #    title = title,
        #    writer = writer,
        #    content = content
        #)        
        #board.save() #db에 insert
        #return HttpResponseRedirect('/board/')
        
        
       #모델.objects.create(값)
        Board.objects.create(
            title = title,
            writer = request.session.get('writer'), #세션에 있는 값 저장
            content = content
        )
         
        return HttpResponseRedirect('/board/')
        
                                    
        
        

#def update_board(request, id):
    
    

# def delete_board(request, id):
#     Board.objects.get(id = id).delete()
#     return HttpResponseRedirect("../../board")


    
    
    
    
    
    
    
    
    
    
    
    
    # id = request.POST['Board_id']
    # title = request.POST['Board_title']
    # content = request.POST['Board_content']
    # writer = request.POST['Board_writer']
    # input_date = request.POST['Board_input_date']
    # view_count = request.POST['Board_view_count']
    
    # Board.objects.create(
    #     board_id = id,
    #     board_title = title,
    #     board_content = content,
    #     board_writer = writer,
    #     board_input_date = input_date,
    #     board_view_count = view_count,
        
    # )
    # return HttpResponseRedirect("../../board")




    
    










    # template = loader.get_template('board/index.html')
    # dictionary타입의 변수 context
    # context = {}
    
    #응답객체안에 템플릿과 표시할 값(context), 요청(request)
    # return HttpResponse(template.render(context, request))

# def call1(request):
#     template = loader.get_template('app/template.html')
#     print(request)
    
#     context = {}
    
#     return HttpResponse(template.render(context, request))

# # RESTful 방식으로 호출된 주소에 대한 함수
# # 요청 객체 뒤의 파라미터에 해당하는 변수명 써줘야함
# def call2(request, number):
#     #파이썬에서는 자료형이 다른 것을 합칠 수 없음
#     # print("number :" + number)
#     print("number :", number)
    
#     template = loader.get_template('app/template.html')
    
#     context = {}
    
#     return HttpResponse(template.render(context, request))

# def call3(request):    
#     #request 객체에서 가져오는 모든 데이터는 str타입
#     name = request.GET['name']
#     age = request.GET['age']
    
#     print(type(age))
#     print("name :", name)
#     print("age : ", age)
    
#     return HttpResponse("호출됨")

# def call4(request):
#     template = loader.get_template('app/template.html')
    
#     context = {
#         #문자열 하나 보내기
#        'item' : "This text is sent from server.",
#        'name' : "김동현",
       
#         # 리스트 보내기
#        'board_list' : [
#            {'title' : '1등', 'writer' : '홍길동'},
#            {'title' : '2등', 'writer' : '전우치'},           
#            {'title' : '3등', 'writer' : '사오정'}           
#        ],
       
#         #딕셔너리 보내기
#        'mydata' : {
#        'name' : '김동현',
#        'age' : 29,
#        'address' : '광주'
#      }       
#     }
    
#     return HttpResponse(template.render(context, request))

# def call5(request):   
#     board_list1 = [ '사과', '딸기', '바나나' ]          
    
#     template = loader.get_template('app/tag.html')
    
#     context = {
#         'list' : board_list1,
#         'number' : 8,
#     }
    
#     return HttpResponse(template.render(context, request))

# def call6(request):
#     template = loader.get_template('app/form.html')
    
#     context = {}
    
#     return HttpResponse(template.render(context, request))

# #폼에 입력된 데이터 가져오기
# def call_submit(request):
#     name = request.POST['name']
#     age = request.POST['age']
    
#     print("name : ", name)
#     print("age : ", age)
    
#     return HttpResponse("submit OK")


# def call7(request):
#     template = loader.get_template('app/call7.html')
    
#     name = '김동현'
#     age = '29'
#     live = '광주'
    
#     context = {
#         "name" : name,
#         "age" : age,
#         "live" : live,
#     }    
    
#     return HttpResponse(template.render(context, request))
    
    
