import addressbook.addressbook_pb2 as addressbook_pb2
from google.protobuf.timestamp_pb2 import Timestamp

addressbook = addressbook_pb2.AddressBook()

first_address = addressbook.people.add()
first_address.name = "Persona1"
first_address.id = 1001
first_address.email = "persona1@persona.com"

first_address.phones.add(number="123456", type=1)
first_address.phones.add(number="234567", type=2)

first_timestamp = Timestamp()
first_timestamp.GetCurrentTime()
first_address.last_updated.seconds = first_timestamp.seconds
first_address.last_updated.nanos = first_timestamp.nanos

second_address = addressbook.people.add()
second_address.name = "Persona2"
second_address.id = 1002
second_address.email = "persona2@persona.com"

second_address.phones.add(number="345678", type=1)
second_address.phones.add(number="456789", type=2)

second_timestamp = Timestamp()
second_timestamp.GetCurrentTime()

second_address.last_updated.seconds = second_timestamp.seconds
second_address.last_updated.nanos = second_timestamp.nanos
# print(timestamp.GetCurrentTime())

# print(addressbook)

with open("addressbook.bin", "wb") as f:
    print("Write as binary")
    byteAsString = addressbook.SerializeToString()
    f.write(byteAsString)


with open("addressbook.bin", "rb") as f:
    print("read values")
    addressbook_read = addressbook_pb2.AddressBook().FromString(f.read())


print(addressbook_read)
