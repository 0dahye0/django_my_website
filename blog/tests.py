from django.test import TestCase

# Create your tests here.

def create_comment(post, text='a comment', author=anonymous):
  comment = Comment.objects.create(
    post=post,
    text=text,
    author=anonymous,
  )
  
  
def create_post(title, content, author, category = None):
  blog_post = Post.object.create(
    title=title,
    content=content,
    created=timezone.now(),
    author=author,
    category=category,
  )
  
  
def test_comment(self):
  comment = create_comment:
    post= post_000
    
