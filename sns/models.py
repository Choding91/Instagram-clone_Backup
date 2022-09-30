from django.db import models

class Feed(models.Model):
    #모델 필드
    author = models.CharField(max_length=50, null=False) 
    content = models.TextField(max_length=2200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #모델의 메타정보
    class Meta:
        db_table = 'sns_feed'
        verbose_name = '게시글'  # 단수형 
        verbose_name_plural = '게시글들'  # 복수형
        
    def __str__(self):
        return f'{self.created_at} | {self.author} | {self.content}'



class FeedComment(models.Model):

    feed_id = models.ForeignKey(Feed, on_delete=models.CASCADE)
    author = models.CharField(max_length=50, null=False)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "comment"
        verbose_name = '게시글 댓글'  # 단수형 
        verbose_name_plural = '게시글 댓글들'  # 복수형

    def __str__(self):
        return f'{self.created_at} | {self.author} | {self.content}'