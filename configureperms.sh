#!/bin/bash
chmod +x ./runcelery.sh
sudo chown pi:www-data Smarty_Trash/
sudo chown pi:www-data Smarty_Trash/db.sqlite3
chmod g+w Smarty_Trash/db.sqlite3