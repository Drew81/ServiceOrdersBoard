cd sevice_orders
source service_orders/bin/activate
pip3 install django
pip install virtualenv
python3 -m venv ./ServiceOrders
pip3 install graphene_python
python3 manage.py runserver