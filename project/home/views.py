from django.shortcuts import redirect ,render , get_object_or_404
from home.models import Post, Comment
from django.urls import reverse
from home.form import CommentForm, PostForm,CommentDeleteForm
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView

def post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST,author = request.user, post = post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)

    return render(request, 'home/post.html', {'post':post, 'form':form})

def draft(request):
    posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-date')
    return render(request, "home/draft.html", {'ups':posts})

def add_Blog(request):
    if request.method == "POST":
        form = PostForm(data= request.POST, files=request.FILES)
        if form.is_valid():
            blog = form.save(commit= False)
            blog.author = request.user
            blog.save()
            obj = form.instance
            alert = True
            return render(request, "home/draft.html",{'obj':obj, 'alert':alert})
    else:
        form=PostForm()
        return render(request, "home/add_Blog.html", {'form':form})
    
class UpdateBlog(UpdateView):
    model = Post
    template_name = 'home/editBlog.html'
    fields = ['title','body','image','status']
    success_url = '/'

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'home/post_detail.html', {'post': post, 'comments': comments})

# Xóa comment
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        # Xử lý việc xóa Comment ở đây
        comment.delete()
        return redirect('post_detail', post_id=comment.post.id)
    form = CommentDeleteForm()
    return render(request, 'home/delete_comment.html', {'comment': comment})

def DeleteBlog(request, id):
    po_del = Post.objects.get(pk = id)
    if request.method == "POST":
        po_del.delete()
        return redirect('blog')
    return render(request, 'delblog.html',{'do_del':po_del})

# def ViewDraft(reqeust):
#     # tim tat ca cac bai` viet draft`
#     draft_post = Post.objects.filter( status = 'draft')
#     return render(reqeust ,"draft.html",{'draft_post':draft_post})


def push_draft(request,id):
    # bien nay se tim tat ca doi tuong , neu khong co thi tra ve 404 
    post_df = get_object_or_404(Post,pk =id)
    # gan cho no bien nay dc push len
    post_df.status = True
    post_df.save()
    return redirect('/')
