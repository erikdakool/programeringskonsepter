import schema_in_pb2 as proto


def create_result(self):
    self.result.proto.extend(self.messages)
    print(self.result.SerializeToString())
    return self.result.SerializeToString()


def hello():
    return "Hello, World!"

if __name__ == " __main__ ":
    print("hello world")
    # msg = proto.Square
    # msg.x = 1
    # print(msg)
    # print(create_result(msg))
