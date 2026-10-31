#!/bin/bash

echo "تحديث النظام..."
apt update && apt upgrade -y

echo "تنزيل الأدوات..."
apt install python3 python3-pip git curl wget nano -y

echo "تنزيل مكتبات بايثون..."
apt install python3-requests python3-bs4 python3-colorama python3-pyfiglet -y

echo "تم خلص كل شي"
