from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from . forms import NewItemForm, EditItemForm
from . models import Item, Category

def items(request):
    query = request.GET.get('query', '')
    categories = Category.objects.all()
    category_id = request.GET.get('category', 0)
    items = Item.objects.filter(is_sold=False)
    
    if category_id:
        items = items.filter(category__id=category_id)
        
    
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })
    
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:8]
    
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()
        
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    }) 
    
@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        
        # Kiểm tra xem người dùng có muốn xóa ảnh không
        image_removed = request.POST.get('image_removed') == 'True'
        
        if form.is_valid():
            # Nếu user muốn xóa ảnh nhưng không upload ảnh mới, hiển thị lỗi
            if image_removed and not request.FILES.get('image'):
                form.add_error('image', 'Image is required')
                return render(request, 'item/form.html', {
                    'form': form,
                    'title': 'Edit item',
                    'item': item,
                })

            form.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)
        
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
        'item': item,
    }) 
    
@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    
    if request.method == 'POST':
        item.delete()
        
        return redirect('dashboard:index')
    
    return render(request, 'item/delete.html', {
        'item': item,
    })
