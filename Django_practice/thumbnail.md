# 장고 썸네일
## imagekit
- 이미지 썸네일 helper 장고 앱 (실제 이미지 처리시에는 PILKit 이 사용됨)

```bash
$ pip install pillow # django-imagekit 사용을 위해서 사전 설치 필요
$ pip install pilkit # django-imagekit 사용을 위해서 사전 설치 필요
$ pip install django-imagekit

# settings.INSTALLED_APPS에 imagekit 추가
```

## 원본 O, 썸네일 O
- ImageSpecFeild
```python
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

class Post(models.Model):
	photo = models.ImageField()
	photo_thumbnail = ImageSpecField(
		source = 'photo', 		   # 원본 ImageField 명
		processors = [Thumbnail(100, 100)], # 처리할 작업목록
		format = 'JPEG',		   # 최종 저장 포맷
		options = {'quality': 60}) # 저장 옵션
```

## 원본 X, 썸네일 O
- ProcessedImageField 
```python
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

class Post(models.Model):
	photo_thumbnail = ProcessedImageField(
		upload_to = 'blog/post',
		processors = [Thumbnail(100, 100)], # 처리할 작업 목룍
		format = 'JPEG',					# 최종 저장 포맷
		options = {'quality': 60})  		# 저장 옵션
```

## 템플릿에서 이미지 직접 처리
- widht, height, crop, upscale 설정 가능
```html
<!-- 썸네일 이미지 태그 생성 -->
{% thumbnail "100x100" post.photo %}

<!-- 썸네일 file object 획득 -->
{% thumbnail "100x100" post.photo as thumb %}
<img src="{{ thumb.url }}" alt="" width="{{ thumb.width }}" height="{{ thumb.height }}">

<!-- 추가 속성 정의 -->
{% thumbnail "100x100" post.photo -- style="" onclick="" class="" %}
```