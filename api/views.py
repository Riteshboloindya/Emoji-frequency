from django.shortcuts import render
import io 
#from rest_framework.parsers import JSONParser
#from .models import Student
#from .serializers import StudentSerializer
#from rest_framework.renderers import JSONRenderer
#from django.http import HttpResponse """
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student, Comment
from rest_framework import status
from .serializers import StudentSerializer,CommentSerializer
from rest_framework import mixins
from rest_framework import generics
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

class CommentAPI(APIView):
    def post(self,request):
        # request.data.pop('csrfmiddlewaretoken')
        print('post comment',request.POST,'\n',request.data)
        
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        q = request.GET.get('q',None)
        print('q',q)
        if q is None:
            comments = Comment.objects.all()
            serializer=CommentSerializer(comments, many=True)
        
        else:
            print('q=',q)
            ##vector = SearchVector('text')
            vector = SearchVector('text', weight ='A') 
            query = SearchQuery(q)
            # comments = Comment.objects.filter(text__contains=q)
            comments = Comment.objects.annotate(search=SearchVector("text"),).filter(search='text')
            # comments = comments.filter(text__search=q)
            #comments = Comment.objects.annotate(rank=SearchRank(vector, query, cover_density=True)).order_by('-rank')
            serializer=CommentSerializer(comments, many=True)
            
        return Response(serializer.data)    







class studentlist(APIView):
   
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist: 
            raise Http404
        except Exception as e:
            print ("get_obj",e)

    
    def get(self,request,pk=None,format=None):
        print('pk',pk)
        if pk is not None:
            stu = self.get_object(pk)
            
            serializer=StudentSerializer(stu)
            #print(stu)
            return Response(serializer.data)
        
        students = Student.objects.all()
        serializer=StudentSerializer(students, many=True)
            #print(stu)
        return Response(serializer.data)
        

    #def post(self):
     #   pass
    
    def post(self, request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def put(self,request, pk,format=None):
        stu = self.get_object(pk)
        #pk = self.kwargs.get('pk')
        print("pk",pk)
        serializer = StudentSerializer(stu, data=request.data)
        #Student = self.get_object(pk)
        #stu = get_object_or_404(Student.objects.all(), pk=pk)
        # data = request.data.get('student')
       
        #serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        print("deleted",pk)
        stu = self.get_object(pk)
        stu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
















#def Student_api(request):
    #if request.method =='GET':
        # json_data =request.body
       # id = request.GET.get("id",None)

       # print("id",id)
        # stream= io.BytesIO(json_data)
        # pythondata =JSONParser().parse(stream)
        # id =pythondata.get('id',None)
       # if id is not None:
           # stu =Student.objects.get(id=id)
           #serializer =StudentSerializer(stu)
           # json_data =JSONRenderer().render(serializer.data)
           # return HttpResponse(json_data, content_type='application/json')
        
        #stu = Student.objects.all()
        #serializer =StudentSerializer(stu,many=True)
        #json_data =JSONRenderer().render(serializer.data)
        #return HttpResponse(json_data, content_type='application/json')
        
def add_comment(request):
    return render(request,"form.html",{})