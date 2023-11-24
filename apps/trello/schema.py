import uuid
import graphene
from graphene_django import DjangoObjectType
from apps.trello.models import Task, Column

class ColumnType(DjangoObjectType):
    class Meta:
        model = Column
        fields = '__all__'
        
class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = '__all__'
        
class Query(graphene.ObjectType):
    tasks = graphene.List(TaskType)
    columns = graphene.List(ColumnType)
    column_by_name = graphene.Field(ColumnType, name=graphene.String(required=True))

    def resolve_tasks(root, info):
        return Task.objects.select_related("column").all()
    
    def resolve_columns(root, info):
        return Column.objects.all()
    
    def resolve_column_by_name(root, info, name):
        try:
            return Column.objects.get(name=name)
        except Column.DoesNotExist:
            return None

class CreateColumn(graphene.Mutation):
    column = graphene.Field(ColumnType)

    class Arguments:
        name = graphene.String()
        
    def mutate(self, info, name):
        column_id = uuid.uuid4().hex
        column = Column(column_id=column_id, name=name)
        column.save()
        return CreateColumn(column=column)

class UpdateColumn(graphene.Mutation):
    column = graphene.Field(ColumnType)
    ok = graphene.Boolean()

    class Arguments:
        name = graphene.String()
        column_id = graphene.ID()

    def mutate(self, info, column_id, name):
        column = Column.objects.get(column_id = column_id)
        column.name = name
        column.save()
        return UpdateColumn(column=column, ok=True)
    
class DeleteColumn(graphene.Mutation):
    column = graphene.Field(ColumnType)

    class Arguments:
        name = graphene.String()
        column_id = graphene.ID()
    def mutate(self, info, column_id):
        column = Column.objects.get(column_id=column_id)
        column.delete()
        return DeleteColumn(ok=True)
    
class CreateTask(graphene.Mutation):
    task = graphene.Field(TaskType)
    ok = graphene.Boolean()

    class Arguments:
        text = graphene.String()
        column_id = graphene.ID()

    def mutate(self, info, text,column_id):
        task_id = uuid.uuid4().hex
        task = Task(text=text, task_id=task_id)
        column = Column.objects.get(column_id=column_id)
        task.column = column
        task.save()
        return CreateTask(task=task)

class UpdateTask(graphene.Mutation):
    task = graphene.Field(TaskType)
    ok = graphene.Boolean()

    class Arguments:
        text = graphene.String()
        task_id = graphene.ID()
        column_id = graphene.ID()

    def mutate(self, info, task_id, text, column_id):
        task = Task.objects.get(task_id = task_id)
        task.text = text
        column = Column.objects.get(column_id=column_id)
        task.column = column
        task.save()
        return UpdateTask(task=task, ok=True)

class DeleteTask(graphene.Mutation):
    ok = graphene.Boolean()
    
    class Arguments:
        task_id = graphene.ID()

    def mutate(self, info, task_id):
        task = Task.objects.get(task_id=task_id)
        task.delete()
        return DeleteTask(ok=True)
    
class Mutation(graphene.ObjectType):
    create_column = CreateColumn.Field()
    update_column = UpdateColumn.Field()
    delete_column = DeleteColumn.Field()

    create_task = CreateTask.Field()
    update_task = UpdateTask.Field()
    delete_task = DeleteTask.Field()
        
schema = graphene.Schema(query=Query, mutation=Mutation)