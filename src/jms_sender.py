import json
import stomp

def send_to_jms_queue(payload, queue_name='/queue/accounts', host='localhost', port=61613, username='admin', password='admin'):
    conn = stomp.Connection([(host, port)])
    conn.connect(username, password, wait=True)
    conn.send(body=json.dumps(payload), destination=queue_name)
    print(" [x] Sent 'Account data to ActiveMQ Queue'")
    conn.disconnect()