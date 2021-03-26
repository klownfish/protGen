# python exporter
## structure
The exporter will generate receiver and sender classes. 
receiver classes have the datatype as name
sender classes are named ```{datatype}_from_{source}_to_{target}```

enums are saved as Enums using their name

### receivers
functions
* parse_buf(buf)
    * parses a buf and sets the values
* get_target()
    * gets the units.target entry
* get_source()
    * gets the units.source entry
* get_datatype()
    * gets the datatypes.datatype entry
* get_size()
    * gets the size of the message
* get_id()
    * gets the id
* get_```{field name}```()
    * generated for all fields, gets the value of the field

### senders
functions
* get_target()
    * gets the units.target entry
* get_source()
    * gets the units.source entry
* get_datatype()
    * gets the datatypes.datatype entry
* get_size()
    * gets the size of the message
* get_id()
    * gets the id
* get_buf()
    * builds the buf starting at and sets the index accordingly
* set_```{field name}```(value)
    * generated for all fields, set the value of a field

### functions
* id_to_datatype(id)
    * returns the datatype 