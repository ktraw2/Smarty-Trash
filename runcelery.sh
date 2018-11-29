#!/bin/bash
source venv/bin/activate
cd Smarty_Trash
celery -A Smarty_Trash.celery worker --beat -l info
cd ..
