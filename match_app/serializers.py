from rest_framework import serializers
import match_app.models as models


class ChoicesField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self._choices = choices
        super(ChoicesField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return self._choices[obj]

    def to_internal_value(self, data):
        return getattr(self._choices, data)


class HumanSerializer(serializers.ModelSerializer):
    gender = ChoicesField(choices=models.Human.GENDER)
    avatar = serializers.ImageField(use_url=True)

    class Meta:
        model = models.Human
        fields = ['id', 'avatar', 'first_name', 'second_name', 'age', 'gender']


class MatchSerializer(serializers.ModelSerializer):
    gender = ChoicesField(choices=models.Human.GENDER)
    human = HumanSerializer(required=True)

    class Meta:
        model = models.Match
        fields = ['first_name', 'second_name', 'age', 'gender', 'human']