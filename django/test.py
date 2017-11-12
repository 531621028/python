```python
def detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
    extensions=[
    'markdown.extensions.extra',
    'markdown.extensions.codehilite',
    'markdown.extensions.toc',
    ])
    return render(request, 'blog/detail.html', context={'post': post})
```
