sudo apt-get install rabbitmq-server
sudo rabbitmq-server restart
sudo rabbitmqctl status

sudo rabbitmqctl add_user jm-user1 sample
sudo rabbitmqctl set_permissions -p jm-vhost jm-user1 ".*" ".*" ".*"
app = Celery('tasks', broker='amqp://jm-user1:sample@localhost/jm-vhost')
celery -A tasks worker --loglevel=info












rabbitmqctl add_vhost my_vhost

rabbitmqctl set_permissions -p my_vhost guest ".*" ".*" ".*"



sudo rabbitmq-plugins enable rabbitmq_management
http://localhost:15672/