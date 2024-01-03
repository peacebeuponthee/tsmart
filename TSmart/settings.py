class TSmartSettings():
    IP_Address="192.168.1.19"
    self_run_timer=10
    first_run=True
#Debug Settings
    Log_Level="Error"               #Optional - Enables logging level. Default is "Error", but can be "Info" or "Debug"
    Debug_File_Location=""          #Optional - Location of logs (Default is console)
    Print_Raw_Registers=True        #Optional - Bool - True publishes all available registers.
#MQTT Output Settings
    MQTT_Output= True               #Optional - Bool - True or False
    MQTT_Address="swarm_mqtt"       #Optional - (Required is above set to True) IP address of MQTT broker (local or remote)
    MQTT_Username=""                #Optional - Username for MQTT broker
    MQTT_Password=""                #Optional - Password for MQTT broker
    MQTT_Topic="BoilerBoost"        #Optional - Root topic for all MQTT messages. Defaults to "GivEnergy/<SerialNumber> 
    MQTT_Port=1883                  #Optional - Int - define port that MQTT broker is listening on (default 1883)
    ha_device_prefix="Boiler_Boost"