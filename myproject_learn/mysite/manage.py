#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'mysite.settings')  # 設定環境，抓取mysite資料夾內的settings.py檔。manage.py是程式的進入點、settings.py是整個專案的設定
    try:
        # 從django套件載入function(從command_line去執行)
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # 該function就會去抓sys.argv這個值，進而作執行。
    # sys.argv為對系統灌參數，當我們在這個檔案manage.py，執行python manage.py runserver這個指令時，就把runserver這個參數灌進去了
    # 對manage.py來說，runserver即為參數，即execute_from_command_line這個function就會執行runserver，django就啟動了！！
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
