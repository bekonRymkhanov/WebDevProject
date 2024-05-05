from rest_framework import serializers
from .models import MyUser,Bet,Match,Club


class ClubSerializer(serializers.Serializer):
    id     =     serializers.IntegerField(read_only=True)
    name   =     serializers.CharField()
    points =     serializers.IntegerField()

    def create(self, validated_data):

        return Club.objects.create(**validated_data)

    def update(self, instance:Club, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.points = validated_data.get('points', instance.points)
        instance.save()
        return instance

class ClubSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"









class MatchSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    home_club = ClubSerializer()
    away_club = ClubSerializer()
    match_date = serializers.DateTimeField()
    state1 = serializers.IntegerField()
    state2 = serializers.IntegerField()
    state3 = serializers.IntegerField()

    def create(self, validated_data):
        home_club_data = validated_data.pop('home_club')
        away_club_data = validated_data.pop('away_club')

        home_club, _ = Club.objects.get_or_create(**home_club_data)
        away_club, _ = Club.objects.get_or_create(**away_club_data)

        match = Match.objects.create(home_club=home_club, away_club=away_club, **validated_data)
        return match

    def update(self, instance, validated_data):
        home_club_data = validated_data.get('home_club')
        away_club_data = validated_data.get('away_club')

        if home_club_data:
            for attr, value in home_club_data.items():
                setattr(instance.home_club, attr, value)
            instance.home_club.save()

        if away_club_data:
            for attr, value in away_club_data.items():
                setattr(instance.away_club, attr, value)
            instance.away_club.save()

        for attr, value in validated_data.items():
            if attr not in ['home_club', 'away_club']:
                setattr(instance, attr, value)
        instance.save()
        return instance

class MatchSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = "__all__"











class MyUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    balance = serializers.IntegerField()
    email = serializers.EmailField()

    def create(self, validated_data):
        return MyUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
    
class MyUserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'name', 'email','password', 'balance']
        extra_kwargs={
            'password':{'write_only':True}
        } 
    def create(self, validated_data):
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class MyUserSerializer3(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'name', 'email', 'balance']
        extra_kwargs={
            'password':{'write_only':True}
        } 
    def create(self, validated_data):
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance













class BetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    match = serializers.PrimaryKeyRelatedField(queryset=Match.objects.all())
    state_chosen = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=8, decimal_places=2)
    user = serializers.PrimaryKeyRelatedField(queryset=MyUser.objects.all())

    def create(self, validated_data):
        return Bet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.match = validated_data.get('match', instance.match)
        instance.state_chosen = validated_data.get('state_chosen', instance.state_chosen)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance
    
class BetSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = ['id', 'match', 'state_chosen','amount', 'user'] 