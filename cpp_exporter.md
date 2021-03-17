# C++ exporter
## structure
The exporter will generate receiver and sender classes. 
receiver classes have the datatype as name
sender classes are named ```{datatype}_from_{source}_to_{target}```

for the bit field flags will be generated with the capitalized name ```{datatype}_{bit field name}```

messages are parsed by calling PARSE_MSG(id, buf) and creating a callback

enums are saved as ```enums struct``` using their name

### receivers
functions
* enum units get_target()
    * gets the target
* enum units get_source()
    * gets the source
* parse_buf()
    * parses a buf and sets the values
* get_size()
    * gets the size of the message
* get_bit_field()
    * gets the bit field
* get_{field name}()
    * generated for all fields, gets the value of the field

### senders
functions
* enum units get_target()
    * gets the target
* enum units get_source()
    * gets the source
* get_size()
    * gets the size of the message
* set_bit_field(value)
    * sets the bitfield
* build_buf(*buf, *len)
    * builds the buf and sets the length
* set_```{field name}```(value)
    * generated for all fields, set the value of a field
### macros
* ID_TO_LEN(id, len)
    * sets the len according to the id
* ID_TO_SOURCE(id, source)
    * set the source according to the id
* ID_TO_TARGET(id, target)
    * set the target according to the id
* PARSE_MSG(id, buf)
    * parses the msg and calls the ```{protocol name}_rx({datatype} msg)``` function

pro tip: overload your ```{protocol name}_rx()``` to receive messages.\
define a catch all template function that does nothing as well to steer away undefined references
## usage
```node cppExporter.js FILE_IN DIR_OUT```