# Create your views here.

from rest.models import Author,Publish,Book
from rest_framework.response import Response


from rest_framework import serializers   #前後端的橋梁，序列化契們

class Authorser(serializers.Serializer):  # 原型序列畫器，與模型無關
    name= serializers.CharField(max_length=5)
    age = serializers.IntegerField()
    def create(self,validated_data):
        Ins=Author.objects.create(**validated_data)   #要打亂參數
        return Ins
    def update(self, instance, validated_data):
        Author.objects.filter(pk=instance.id).update(**validated_data)
        return instance


from rest_framework.views import APIView   #最基礎的APIViews
class AuthorView (APIView):
    
    def get(self, request):
        result= Author.objects.all()  #接著要序列畫 ，配合序列畫主見
        # print("____________")
        # print(result)
        A_ins=Authorser(instance=result , many=True)   # 實例畫  序列畫器
        print("____________")
        print(A_ins)
        print("____________")
        print("a_ins.data",A_ins.data)
        print("____________")
        if A_ins.is_valid:  # 不會對數具庫內容作驗證 ，只會對外面傳來的做驗證
            pass
        return  Response(A_ins.data) 
        
    def post(self, request):
        pos_ins=Authorser(data=request.data )   # 實例畫  序列畫器
        if pos_ins.is_valid():
            
            pos_ins.save()  #這樣寫是把教驗邏輯  後端儲存分開
            return Response("ok")
        else:
            print(pos_ins.data)   #前端怎麼傳 後端怎麼收
            return Response(pos_ins.errors)
        
        
class AuthorDtailView (APIView):
    def get(self,request,id):
        result= Author.objects.get(pk=id)  #接著要序列畫 ，配合序列畫主見
        A_ins=Authorser(instance=result , many=False)   # 實例畫  序列畫器
        if A_ins.is_valid:  # 不會對數具庫內容作驗證 ，只會對外面傳來的做驗證
            pass
        return  Response(A_ins.data) 
    
    def delete(self,request,id):
        Author.objects.get(pk=id).delete()
        return Response("已經刪除")
    
    def put(self,request,id):
        ooo=Author.objects.get(pk=id)
        RRRRRR=Authorser(instance=ooo,data=request.data)#如果兩個都有放 則會跑出實力
        print("確認data跑出後端還前端",RRRRRR.data)  #data有參填入的時候需要驗證才能調
        if RRRRRR.is_valid():
            #print("確認data跑出甚麼",RRRRRR.data)  #跑出數據庫的   如果這個時候調用save就不能用!!
            RRRRRR.save()
            print("確認data  執行save跑出甚麼",RRRRRR.data)  #實例資料
            return Response(RRRRRR.validated_data)
        
        else:
            return Response(Authorser(data=request.data).errors)
        
    
############################################################################################

# class Publish_ser(serializers.ModelSerializer):  # 利用原序列化契，加上與模型相關父類繼承
#     class Meta:
#         model=Publish
#         fields="__all__"

# class PublishView (APIView):
    
#     def get(self, request):
#         result= Publish.objects.all()  #接著要序列畫 ，配合序列畫主見
#         A_ins=Publish_ser(instance=result , many=True)   # 實例畫  序列畫器
#         if A_ins.is_valid:  # 不會對數具庫內容作驗證 ，只會對外面傳來的做驗證
#             pass
#         return  Response(A_ins.data) 
        
#     def post(self, request):
#         pos_ins=Publish_ser(data=request.data )   # 實例畫  序列畫器
#         if pos_ins.is_valid():
#             pos_ins.save()  #這樣寫是把教驗邏輯  後端儲存分開
#             return Response("ok")
#         else:
#             print(pos_ins.data)   #前端怎麼傳 後端怎麼收
#             return Response(pos_ins.errors)
        
# class PublishDtailView (APIView):
#     def get(self,request,id):
#         result= Publish.objects.get(pk=id)  #接著要序列畫 ，配合序列畫主見
#         A_ins=Publish_ser(instance=result , many=False)   # 實例畫  序列畫器
#         if A_ins.is_valid:  # 不會對數具庫內容作驗證 ，只會對外面傳來的做驗證
#             pass
#         return  Response(A_ins.data)   #取實力資料
    
#     def put(self,request,id):
#         updata_Publish=Publish.objects.get(pk=id)
#         Ins_publishser=Publish_ser(instance=updata_Publish,data=request.data)#如果兩個都有放 則會跑出實力
#         #print("++++//////.....",Ins_publishser.data)  過了is valid 才能叫這個函數
        
#         if Ins_publishser.is_valid():
#             Ins_publishser.save()
#             print("opopop/////",Ins_publishser.data) #這個部分與.data .validated_data 一樣
            
#             return Response(Ins_publishser.validated_data)
        
#         else:
#             return Response(Authorser(data=request.data).errors)
        
#     def delete(self,request,id):
#         Publish.objects.get(pk=id).delete()
#         return Response("已經刪除")


#############################################################################################################
# from rest_framework.generics import GenericAPIView    調用GenericAPIView   配合自己寫的方法

# class Publish_ser(serializers.ModelSerializer):  # 原型序列畫器，與模型無關
#     class Meta:
#         model=Publish
#         fields="__all__"

# class PublishView (GenericAPIView):
    
#     queryset = Publish.objects  # 這邊跟 好怪
#     serializer_class =Publish_ser

#     def get(self, request):
#         result= self.get_queryset()  # 去找一夏 get querser 怎用
#         A_ins=self.get_serializer(instance=result , many=True)   
#         return  Response(A_ins.data) 
        
#     def post(self, request):
#         pos_ins=self.get_serializer(data=request.data )   
#         if pos_ins.is_valid():
#             pos_ins.save()  
#             return Response("ok")
#         else:
#             print(pos_ins.data)  
#             return Response(pos_ins.errors)
        
# class PublishDtailView (GenericAPIView):
        
#     queryset = Publish.objects  # 這邊跟 好怪
#     serializer_class =Publish_ser
#     lookup_field = 'id'
    
#     def get(self,request,id):
#         result= self.get_object()  
#         A_ins=self.get_serializer(instance=result , many=False)   # 實例畫  序列畫器     
#         return  Response(A_ins.data)   
#     def delete(self,request,id):
#         self.get_object().delete()
#         return Response("已經刪除")
    
#     def put(self,request,id):
#         updata_Publish= self.get_object()  
#         Ins_publishser=self.get_serializer(instance=updata_Publish,data=request.data)#如果兩個都有放 則會跑出實力
#     #     #print("++++//////.....",Ins_publishser.data)  過了is valid 才能叫這個函數
        
#         if Ins_publishser.is_valid():
            
#             Ins_publishser.save()
#             print("opopop/////",Ins_publishser.data) #這個部分與.data .validated_data 一樣
#             return Response(Ins_publishser.data)  #這時候就是傳更新的實例
#         else:
#             return Response( Ins_publishser.errors)
        
#############################################################################
# from rest_framework.generics import GenericAPIView
# class Publish_ser(serializers.ModelSerializer): 
#     class Meta:
#         model=Publish
#         fields="__all__"
        
# from rest_framework.mixins import CreateModelMixin ,ListModelMixin     #以下是集成 各種請求要做的事，被封裝到各個類裡面，透過繼承取得方法
# class PublishView (GenericAPIView, CreateModelMixin ,ListModelMixin):
    
#     queryset = Publish.objects 
#     serializer_class =Publish_ser

#     def get(self, request):
#         return  self.list(request)  #繼承CreateModelMixin實現該方法
        
#     def post(self, request):
#         return  self.create()       #繼承ListModelMixin 實現該方法
    
#
# from rest_framework.mixins import  RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# class PublishDtailView (GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):

#     queryset = Publish.objects 
#     serializer_class =Publish_ser
#     lookup_field = 'id'
    
#     def get(self,request,id):
#         return  self.retrieve(request,id)
    
#     def delete(self,request,id):
#        return  self.destroy(request,id)
   
#     def put(self,request,id):
#         return  self.update(request,id)

##########################################################################################################################
from rest_framework.generics import GenericAPIView
class Publish_ser(serializers.ModelSerializer): 
    class Meta:
        model=Publish
        fields="__all__"

from rest_framework.generics import ListCreateAPIView   #高度封裝兩個方法
class PublishView (ListCreateAPIView):
    queryset = Publish.objects 
    serializer_class =Publish_ser

from rest_framework.generics import RetrieveUpdateDestroyAPIView #高度封裝3個方法   四個父類   from rest_framework.mixins import  RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

class PublishDtailView ( RetrieveUpdateDestroyAPIView):
    queryset = Publish.objects 
    serializer_class =Publish_ser
    lookup_field = 'id'


######################################################################################################################
from rest_framework.generics import GenericAPIView
class Publish_ser(serializers.ModelSerializer): 
    class Meta:
        model=Publish
        fields="__all__"


from rest_framework.viewsets import ViewSetMixin  #就是這裡調用 特別高度封裝的class 可以去路由設定訪問的路線
class PublishView_set (ViewSetMixin  ,APIView):   #除了繼承高階ViewSetMixin 不構，因為缺少部分函數在APIView
    queryset = Publish.objects 
    serializer_class =Publish_ser
    lookup_field = 'id'
    def list (self , request) :  
        return  Response(" 這是list" )
    def create (self , request) :
        return  Response(" 這是post" )
    def retrieve (self , request ,id) :
        return  Response(" 這是retrieve" )
    def update(self , request,id) :
        return Response(" 這是update" )
    def delete (self , request,id)  :  
        return Response(" 這是delete" )
    