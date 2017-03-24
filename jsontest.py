import json

base = json.dumps({
   "id": "2143242423",
   "addressBook": []
})

newAddress = ({
     "firstName": "Dhenku",
     "lastName": "Behera",
     "numbers": ["+14055671234"]
   })

#deserialize json
data = json.loads(base)

#ppend list with new Address
data["addressBook"].append(newAddress)

#serialize back to string
base = json.dumps(data)
print(base)