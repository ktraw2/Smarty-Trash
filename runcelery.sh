#!/bin/bash
cd Smarty_Trash
celery -A Smarty_Trash.celery worker -l info
cd ..