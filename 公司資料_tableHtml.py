# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 22:22:36 2023

@author: user
"""


def my_view(request):
    email_t = request.post.get("email")
    ref = db.reference('完整公司資料_2')
    data = ref.get()  # 数据
    return render(request, 'my_template.html', {'data': data, "email": email_t})

