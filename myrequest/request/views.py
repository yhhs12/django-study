from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.core.paginator import Paginator
from django.core import serializers
from django.contrib.auth.decorators import login_required 
from django.urls import reverse


from json import loads 

from .models import Request

# Create your views here.

def index(request):
    result = None
    context = {}
    
    #검색조건과 검색키워드가 있어야 필터링 실행
    if 'searchType' in request.GET and 'searchWord' in request.GET:
        search_type = request.GET['searchType'] #GET안의 문자열은
        search_word = request.GET['searchWord'] #HTML의 name 속성
        
        print("search_type : {}, search_word : {}".format(search_type, search_word))
        
        #match : Java의 switch랑 비슷함 
        match search_type:
            case 'title': #검색 기준이 제목일 때
                result = Request.objects.filter(title__contains = search_word)
            case 'writer': #검색 기준이 글쓴이일 때
                result = Request.objects.filter(writer__contains = search_word)                
            case 'content': #검색 기준이 내용일 때
                result = Request.objects.filter(content__contains = search_word)
                
        #검색을 했을때만 검색 기준과 키워드를 context에 넣는다
        context['searchType'] = search_type        
        context['searchWord'] = search_word
    else: #QueryDict에 검색 조건과 키워드가 없을 때
        result = Request.objects.all()
    
    #검색 결과 또는 전체 목록을 id의 내림차순 정렬    
    result = result.order_by('-id')            
    
    #페이징 넣기
    #Paginator(목록, 10)
    paginator = Paginator(result, 10)
    
    #Paginator 클래스를 이용해서 자른 목록의 단위에서
    #몇번째 단위를 보여줄 것인지 정한다.
    page_obj = paginator.get_page(request.GET.get('page'))
    
    
    # context['board_list'] = result  
    # 페이징 한 일부 목록을 반환          
    context['page_obj'] = page_obj
        
    return render(request, 'request/index.html', context)

def read(request, id):
    request_obj = Request.objects.get(id = id)
    #고전적인 방법으로 가져오기
    # reply_list = Reply.objects.filter(board_obj = id).order_by('-id')
    #조회수올리기
    request_obj.view_count += 1
    request_obj.save()
    #저장을 해야 update가 반영됨
    
    write_reply_url = reverse('request:write_reply', kwargs={'id': id})
    
    context = {
        'request' : request_obj,
        'write_reply_url': write_reply_url
    
    }
    return render(request, 'request/read.html', context)

@login_required(login_url='common:login')
def write(request):
    if request.method == 'GET': #요청방식이 GET이면 화면표시
        return render(request, 'request/board_form.html')
    else: 
        #요청방식이 POST일 때 할일 , 폼의 데이터를 DB에 저장       
        
        #현재 세션정보의 writer라는 키를 가진 데이터 취득
        title = request.POST['title']
        content = request.POST['content']
        #요청에 들어있는 User 객체
        author = request.user
        
        Request.objects.create(
            title = title,
            content = content,
            author = author
        )
        
        return HttpResponseRedirect('/request/')
    
def find_board(request):
    input_title = request.POST["search_title"]
    condition = request.POST["condition"]
    
    find_boardList = []
    if condition == "all":
        #완전 일치
        find_boardList = Request.objects.filter(title = input_title)
    else:
        #부분 일치
        find_boardList = Request.objects.filter(title__contains = input_title)       
    
    
    context = {
        'board_list' : find_boardList
    }

    return render(request, 'request/index.html', context)

def home(request):
    return HttpResponseRedirect('/request/')

@login_required(login_url='common:login')
def update(request, id):
    board = Request.objects.get(id = id)
    
    #글쓴이와 현재 접속한 사용자의 username이 다르면 목록으로 리다이렉트해줌
    if board.author.username != request.user.username:
        return HttpResponseRedirect('/request/')
    
    if request.method == "GET":
        context ={'board' : board }
        return render(request, 'request/board_update.html', context)
    
    else:
        board.title = request.POST['title']
        board.content = request.POST['content']
            
        board.save()   
        
    return HttpResponseRedirect('/request/')                                    


@login_required(login_url='common:login')
def delete(request, id):
    print(id)
    
    #해당 객체를 가져오기
    board = Request.objects.get(id = id)
    
    #글 작성자의 id와 접속한 사람의 id가 같을 때
    if board.author.username != request.user.username:
        return HttpResponseRedirect('/request/')
    board.delete()
    #다를 때    
    return HttpResponseRedirect('/request/')                                    
            
        

def write_reply(request, id):
    print(request.POST)
    
    user = request.user
    reply_text = request.POST['replyText']
    

    
    # queryset을 이용해봅시다
    Request_obj = Request.objects.get(id=id)
    
    Request_obj.reply_set.create(
        reply_content = reply_text,
        user = user        
    )
    
    return HttpResponseRedirect('/request/' + str(id))  


    

def delete_reply(request, id, rid):
    print(f'id: {id} rid: {rid}')
    
    #Reply.objects.get(id=rid).delete() 같다
    Request.objects.get(id=id).reply_set.get(id=rid).delete()
    
    return HttpResponseRedirect('/request/' + str(id))  
    
    
def update_reply(request, id):    
    if request.method == 'GET':
        rid = request.GET['rid']
        
        board = Request.objects.get(id=id)
        
        context={
            'update' : 'update',
            'board' : request, #id에 해당하는 Board객체
            'reply' : request.reply_set.get(id=rid)  #rid에 해당하는 Reply객체
            
        }
        return render(request, 'request/read.html', context)
    else:
        rid = request.POST['rid']
        
        reply = Request.objects.get(id=id).reply_set.get(id=rid)
        
        #폼에 들어있던 새로운 댓글 텍스트로 갱신한다.
        reply.reply_content = request.POST['replyText']
        
        reply.save()
        
def call_ajax(request):
    print("성공한거같아요")
    print(request.POST)
    #JSON.stringify하면 아래 표현은 사용할수 없음
    # print(request.POST['txt'])
    
    data = loads(request.body)
    print('템플릿에서 보낸 데이터', data)
    print(data['txt'])
    print(type(data))
    
    return JsonResponse({'result': 'ㅊㅋㅊㅋ'})
        
        
def load_reply(request):
    id = request.POST['id']
    print(id)
    
    #해당하는 board id에 달려있는 모든 Reply 가져오기
    #1번방법
    # Reply.objects.filter(board = id)
    
    #2번방법
    reply_list = Request.objects.get(id = id).reply_set.all()
    
    #QuerySet 그 자체는 JS에서는 알수 없는 타입
    #그래서 JSON타입으로 형변환
    serialized_list = serializers.serialize("json", reply_list)
    
    return JsonResponse({'response': serialized_list})
