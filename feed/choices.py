from django.db.models import Choices

class VisibilityChoices(Choices):
    PUBLIC = 'Public'
    FOLLOWERS = 'Followers'
    MENTIONNED = 'Mentionned'
