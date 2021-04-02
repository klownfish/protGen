# C++ exporter
## structure
The exporter will generate receiver and sender classes. 
receiver classes have the datatype as name
sender classes are named ```{datatype}_from_{source}_to_{target}```

messages are parsed by calling PARSE_MESSAGE(id, buf) and creating a callback

enums are saved as ```enums struct``` using their name

everything except macros are in the ```protocol name``` namespace. Macros are prefixed with ```{protocol name}_``` instead.

### receivers
functions
* enum units get_target()
    * gets the target
* enum units get_source()
    * gets the source
* enum datatypes get_datatype()
    * gets the datatype
* get_id()
    * gets the id
* parse_buf()
    * parses a buf and sets the values
* get_size()
    * gets the size of the message
* build_buf(*buf, *index)
    * builds the buf starting at and sets the index accordingly
* set_```{field name}```(value)
    * generated for all fields, set the value of a field
* get_```{field name}```()
    * generated for all fields, gets the value of the field
* get_all_data()
    * returns an array with ```(name, value)``` tuples with all the data

### functions
* id_to_len(id)
    * returns the len according to the id
* id_to_source(id)
    * returns the source according to the id
* id_to_target(id)
    * returns the target according to the id

### macros
* PARSE_MESSAGE(id, buf)
    * parses the msg and calls the ```{protocol name}_rx({datatype} msg)``` function

pro tip: overload your ```{protocol name}_rx()``` to receive messages.\
define a catch all template function that does nothing as well to steer away undefined references
## usage
```node cppExporter.js FILE_IN DIR_OUT```