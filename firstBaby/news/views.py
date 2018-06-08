from django.shortcuts import render
from django.http import HttpResponse
from .models import Artical
import math

# Create your views here.
# Create your views here.
def index(request):
	if request.method == 'GET':
		p=int(request.GET.get('p',1))
		keyword=request.GET.get('keyword','')


		
	
	all_artical=artical=Artical.objects.all().filter(title__icontains=keyword).order_by('-answerCount') # the finnal result
	
	total=all_artical.count()  #all articals size
	
	sigle_page_num=10 #每页显示的数量
	footer_size=10#每页显示多少链接.

	
	artical=all_artical[(p-1)*sigle_page_num:][0:sigle_page_num]  #文章的结果集
	
	# 页脚数的集合.
	all_page_lst=range(1,math.ceil(total/sigle_page_num)+1)
	# p是第几页参数.p_size 用于计算p显示在第几个组里面,从而进行截取.
	p_size=math.ceil(p/footer_size)
	page_lst=all_page_lst[p_size*footer_size-footer_size:p_size*footer_size]

	if p==1 and p<all_page_lst[-1]:
		pdesc=1
		pasc=p+1
	elif p== all_page_lst[-1]:
		pdesc=p-1
		pasc=p
	else:
		pdesc=p-1
		pasc=p+1


	return render(request,'news/index.html',{'artical':artical,'page_lst':page_lst,'keyword':keyword,'pasc':pasc,'pdesc':pdesc,"totals":total,"max_page":all_page_lst[-1]})




