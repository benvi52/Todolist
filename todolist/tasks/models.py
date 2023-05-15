import mongoengine as me

class Task(me.Document):
    title = me.fields.StringField(max_length=100)
    description = me.fields.StringField()
    due_date = me.fields.DateTimeField()
    resources = me.fields.ListField(me.fields.StringField())
    completed = me.fields.BooleanField()
