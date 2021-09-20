from rest_framework import serializers
from django.contrib.auth.models import User 
from course_management.models import Course,Category,Chapter,CourseAlloted,quiz_ques_answer,quiz_question
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ("id","token","first_name","user_role","last_name","username",'email','status','user_image','phone')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = "__all__"
        fields = ("id","title","about","status","category_image","date")

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
       # fields = "__all__"
        fields = ("id","course_title","category_id","author","about","rating","total_hours","total_days","selling_price","original_price","status","course_level","bestseller","course_file","date")

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
       # fields = "__all__"
        fields = ("id", "chapter_name","category_id","course_id","about","discussions","bookmarks","status","chapter_file", "date")

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = quiz_question
       # fields = "__all__"
        fields = ("id","chapter_id","question","marks","question_status","date") 

class QuizQuesAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = quiz_ques_answer
       # fields = "__all__"
        fields = ("id","question_id","answer","answer_status","correct_answer","date") 

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        tokendata = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        tokendata['username'] = user.username
        return tokendata

class ChangePasswordSerializer(serializers.Serializer):
    model = User 
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class CourseAllotedSerializer(serializers.Serializer): 
    class Meta:
        model = CourseAlloted
        # fields = "__all__"
        fields = ("id","category_id", "course_id","course_status","user_id","date")