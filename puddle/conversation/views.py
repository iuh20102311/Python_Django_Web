from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from item.models import Item

from .forms import ConversationMessageForm
from .models import Conversation

@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk) 
    
    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversation = Conversation.objects.filter(item=item).filter(members__in=[request.user])
    
    if conversation:
        pass
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)   
        
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user, item.created_by)
            conversation.save()
            
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            
            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()
    
    return render(request, 'conversation/new.html', {
        'form': form,
        'item': item,
    }) 
    
@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user])
    
    # lấy trò chuyện mới nhất với mỗi người dùng khác
    latest_conversations = {}
    
    for conversation in conversations:
        # Lấy người tham gia cuộc trò chuyện khác với người dùng hiện tại
        for member in conversation.members.all():
            if member != request.user:
                other_user = member
                break
        
        # Lấy tin nhắn mới nhất của cuộc trò chuyện
        last_message = conversation.messages.last()
        
        # Nếu không có tin nhắn, bỏ qua
        if not last_message:
            continue
            
        # Xác định cuộc trò chuyện mới nhất với other_user
        if other_user.id in latest_conversations:
            existing_conversation = latest_conversations[other_user.id]
            existing_last_message = existing_conversation.messages.last()
            
            # So sánh thời gian để lấy cuộc trò chuyện mới nhất
            if last_message.created_at > existing_last_message.created_at:
                latest_conversations[other_user.id] = conversation
        else:
            latest_conversations[other_user.id] = conversation
    
    # Chuyển đổi dictionary thành danh sách để truyền vào template
    latest_conversations_list = list(latest_conversations.values())
    
    # Sắp xếp theo tin nhắn mới nhất
    latest_conversations_list.sort(key=lambda x: x.messages.last().created_at if x.messages.exists() else x.created_at, reverse=True)
    
    return render(request, 'conversation/inbox.html', {
        'conversations': latest_conversations_list,
    })
    
@login_required
def detail(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk, members__in=[request.user])
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            
            conversation.save()
            
            return redirect('conversation:detail', pk=pk)
    else:
        form = ConversationMessageForm()
    
    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form,
    })