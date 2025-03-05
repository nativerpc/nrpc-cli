import zmq
import nrpc_cli


class TestApplication:
    def start(self):
        context = zmq.Context()
        sock = zmq.Socket(context, zmq.ROUTER)
        print('Binding socket')
        sock.bind('tcp://127.0.0.1:9000')
        routing_id = b'route'
        assert zmq.backend.has("draft")
        print(f'Draft: {zmq.backend.has("draft")}')
        peer_state = zmq.backend.cython._zmq._zmq_socket_get_peer_state(sock, routing_id)
        print(f'Peer status: {peer_state}')
        print('Close socket')
        sock.close()


if __name__ == '__main__':
    nrpc_cli.init()
    app = TestApplication()
    app.start()
