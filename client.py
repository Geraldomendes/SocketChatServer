import socket
import threading


class Client:
    def __init__(self, host="127.0.0.1", port=55555):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

    def send_message(self, message):
        self.client.send(message.encode("utf-8"))

    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode("utf-8")
                if message:
                    self.handle_message(message)
                else:
                    print("Connection closed by the server.")
                    self.client.close()
                    break
            except:
                print("An error occurred while receiving a message.")
                self.client.close()
                break

    def handle_message(self, message):
        match message.split(" ")[0]:
            case "!users":
                users_count = message.split(" ")[1]
                users = message.split(" ", 2)[2]
                print(f"Users online ({users_count}): {users}")
            case "!msg":
                sender = message.split(" ")[1]
                msg_content = message.split(" ", 2)[2]
                print(f"{sender}: {msg_content}")
            case "!changenickname":
                old_nick = message.split(" ")[1]
                new_nick = message.split(" ")[2]
                print(f"{old_nick} changed nickname to {new_nick}")
            case "!poke":
                poker_nick = message.split(" ")[1]
                target_nick = message.split(" ")[2]
                print(f"{poker_nick} poked {target_nick}")
            case "!left":
                nickname = message.split(" ")[1]
                print(f"{nickname} has left the chat.")
            case _:
                print(message)

    def connect(self):
        nickname = input("Choose your nickname: ")

        if not nickname:
            print("Invalid nickname, connection lost!")
            self.client.close()
            return

        try:
            self.send_message(f"!nick {nickname}")

            # Start a thread to continuously listen for messages from the server
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.start()
        except:
            print("Connection lost!")
            self.client.close()
            return

        while True:
            try:
                message = input()

                match message.split(" ")[0]:
                    case "!sendmsg":
                        self.send_message(message)
                    case "!changenickname":
                        self.send_message(message)
                    case "!poke":
                        self.send_message(message)
                    case _:
                        print("Invalid command!")
            except:
                print("Connection lost!")
                self.client.close()
                break


if __name__ == "__main__":
    client = Client()
    client.connect()
