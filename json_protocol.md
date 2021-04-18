### basic structure
```
{
    config: {},
    enums: [],
    messages: []
}
```

### config
```
{
    name: "foo",
    idNativeType: "uint8",
}
```
### enums
Enums that are generated and should always exist:

* fields - contains all field names
* messages - contains all message names
* nodes - contains all senders and receivers
* categories - contains all message categories

```
{
    name: "foo",
    nativeType: "uint8",
    size: 1,
    entries: {
        "bar": 0,
        "baz": 1
    },
},
{
    name: "alice",
    nativeType: "uint8",
    size: 1,
    entries: {
        "alice": 0,
        "bob": 1,
        "carol": 2
    },
}
```

### messages
if two messages have the same ID set "duplicate: true" on one of them.
should only be done if they have exactly the same fields

* id: mandatory
* name - mandatory
* sender - mandatory
* receiver - mandatory
* category - mandatory, default to "none"
* totalsize - mandatory
* bitField - optional, array with strings
* bitFieldSize - optional
* bitFieldNativeType - optional
* fields - mandatory, empty array if there are none
* description - optional, for  documentation
```
{
    id: 1
    name: "pressure",
    sender: "rocket",
    receiver: "ground",
    category: "telemetry",
    totalSize: 1,
    bitFieldSize: 1,
    bitFieldNativeType: "uint8"
    bitField: [
        "hello",
        "there
    ],
    fields: []
}
```

### field
should contain
* name
* size
* type
* nativeType

and some other stuff to describe the following types

* packedFloat
* scaledFloat
* uint 
* int
* fixedString
* enum
* double
* float

#### packedFloat

```
{   
    name: "foo",
    type: "packedFloat",
    nativeType: "uint8",
    size: 1,
    min: -5,
    max: 12
}
```

#### scaledFloat
```
{
    name: "cool",
    type: "scaledFloat",
    nativeType: "uint8",
    size: 1,
    scale: 10
}
```

#### uint
```
{
    name: "hej",
    type: "uint",
    nativeType: "uint8",
    size: 1,
}
```

#### int
```
{
    name: "foo",
    type: "uint",
    nativeType: "uint8",
    size: 1,
}
```

#### fixedString
A string. will always be sent as `size` bytes no matter what
```
{
    name: "what_i_had_for_dinner",
    type: "fixedString",
    nativeType: "fixedString",
    size: 10,
}
```

#### enum
```
{
    "name": "fix",
    "type": "enum",
    "enumName": "fix_status",
    "nativeType": "uint8",
    "size": 1,
}
```

#### double

```
{
    "name": "temperature",
    "type": "double",
    "nativeType": "double",
    "size": 8,
}
```
#### float
```
{
    "name": "temperature",
    "type": "float",
    "nativeType": "float",
    "size": 4,
}
```