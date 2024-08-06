from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# 기존의 UserCreationForm은 기존 유저 모델을 대상으로 작성되었기 때문에 이를 변경해 줄 필요가 있다.
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        #user 모델을 직접 참조하지 않고 함수를 이용, 확장성과 일관성: user모델이 바귀더라도 수정할 필요가 없다.
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)  #지정 안하면 접근하면 안되는 정보도 수정 가능