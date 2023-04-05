# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 22:22:36 2023

@author: user
"""


def my_view(request):
    email_t = request.post.get("email")
    ref = db.reference('Humandata')
    data = ref.get  # 数据
    reference_list = ['金', '火']  # 参考列表
    return render(request, 'my_template.html', {'data': data, 'reference_list': reference_list})
