from django.shortcuts import render, redirect, get_object_or_404
# Import .models database to use below
from .models import Item
# Import form setup in forms.py
from .forms import ItemForm


# Create your views here.
def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            # Should use name tag in urls.py
            return redirect('get_todo_list')
    # Create instance of form
    form = ItemForm
    # Create form to display on add_item.html
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            # Should use name tag from urls.py
            return redirect('get_todo_list')
    form = ItemForm(instance=item)
    # Create form to display on add_item.html
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    # item.done = not item.done
    # item.save()
    if item.done is False:
        item.done = True
        item.save()
    else:
        item.done = False
        item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')
