my_char = "PzLaM2ZqOx5Ks3NwIcJ1Sd6NeUvH7WfBrY9AbGgVtTnGhVyTmG8EjVu0TkFi4QClRoDpX"
mac_addr = '00:80:F4:C9:B9:A7'
replaceAll = mac_addr.replace(':', '')


def generatePasswd(str1=replaceAll, i=len(replaceAll), str2=my_char):

    str3 = str1

    i2 = i
    str4 = str2
    cArr = ['']*12  # 12 elements

    if str3 != '':

        i3 = 6
        if i2 >= 6:
            substring = str3[-6:]
            i4 = 0
            while (i4 < i2) & (i4 < i3):

                hexToInt = int(f"0x{substring[i4]}",0)
                i5 = 15 - (hexToInt % 15)
                d2 = float(hexToInt)
                i6 = i4
                d3 = float(i5)

                round_ = int(
                    round(d3 ** 3.0) * 8 +
                    round(d3 ** 2.0) * 3 +
                    (i5 * 5)) % (len(str2) + 1)


                i7 = i6 * 2
                idx = int(round(d2 ** 3.0) * 6 +
                          round(d2 ** 2.0) * 9 +
                          (hexToInt * 7) )% (len(str2) + 1)


                cArr[i7] = str4[idx]
                cArr[i7 + 1] = str4[round_]
                i4 = i6 + 1
                i3 = 6
    return ''.join(cArr)

if __name__ == '__main__':

    import requests


    key = generatePasswd()
    print(key)

    r = requests.get('https://192.168.0.45/rsa1/MeterInstantData', verify=False, auth=('m2madmin', key))
    r.json()


paths =   {
     "DELETE_INSTANCE_MIO_INPUT" : "/rsa1/MioInput;channel=",
     "DELETE_INSTANCE_MIO_OUTPUT" : "/rsa1/MioOutput;channel=",
     "DELETE_INSTANCE_MPR" : "/rsa1/MprEndpoint;channel=",
     "DELETE_WIRELESS_INPUT" : "/rsa1/MioWirelessInput;slaveId=%d;channel=%d",
     "DELETE_WIRELESS_METER" : "/rsa1/WirelessMeter;deviceAddress=",
     "DELETE_WIRELESS_OUTPUT" : "/rsa1/MioWirelessOutput;slaveId=%d;channel=%d",
     "DELETE_WIRELESS_PRO" : "/rsa1/WirelessProChannel;deviceAddress=",
     "DELETE_WIRELESS_SENSOR" : "/rsa1/WirelessSensor;deviceAddress=",
     "GET_BRANCH_METERS" : "/rsa1/BranchMeters",
     "GET_CONNECTION_STATISTICS" : "/rsa1/WiserConnectionStatistics",
     "GET_CONTROLLER" : "/rsa1/Controller",
     "GET_EP_CONFIG_UPDATE_STATUS" : "/rsa1/EpConfigUpdateStatus ",
     "GET_GATEWAY_KEY" : "/rsa1/GateWayKey",
     "GET_INSTANCES_MPR" : "/rsa1/MprEndpoint/instances",
     "GET_INSTANCE_MIO_INPUT" : "/rsa1/MioInput/instances",
     "GET_INSTANCE_MIO_OUTPUT" : "/rsa1/MioOutput/instances",
     "GET_MEASUREMENT_DATA" : "/rsa1/MeasurementData;sId=%d;ch=%d",
     "GET_METER_CUMULATED_DATA" : "/rsa1/MeterCumulatedData",
     "GET_METER_INSTANT_DATA" : "/rsa1/MeterInstantData",
     "GET_PRODUCT_DETAILS" : "/rsa1/ProductDetails",
     "GET_PRODUCT_INTERFACE" : "/fct/ProductInterface",
     "GET_SYSTEM_UPGRADE_STATUS" : "/rsa1/SystemUpgradeStatus",
     "GET_USAGE_METERS" : "/rsa1/UsageMeters",
     "GET_USER_PREPAIRING" : "/rsa1/UserPreparing",
     "GET_WIRELESS_DIAGNOSTIC" : "/rsa1/WirelessDiagnostic",
     "GET_WIRELESS_INPUT" : "/rsa1/MioWirelessInput;slaveId=%d;channel=%d",
     "GET_WIRELESS_INPUTS" : "/rsa1/MioWirelessInput/instances",
     "GET_WIRELESS_METER" : "/rsa1/WirelessMeter;deviceAddress=",
     "GET_WIRELESS_METERS" : "/rsa1/WirelessMeter/instances",
     "GET_WIRELESS_METERS_LITE" : "/rsa1/WirelessMeterList/instances",
     "GET_WIRELESS_METER_LITE" : "/rsa1/WirelessMeterInfo;dA=",
     "GET_WIRELESS_OUTPUT" : "/rsa1/MioWirelessOutput;slaveId=%d;channel=%d",
     "GET_WIRELESS_OUTPUTS" : "/rsa1/MioWirelessOutput/instances",
     "GET_WIRELESS_PRO_LIST" : "/rsa1/WirelessProChannel/instances",
     "GET_WIRELESS_PRO_LITE" : "/rsa1/WirelessProInfo;dA=",
     "GET_WIRELESS_SENSOR" : "/rsa1/WirelessSensor;deviceAddress=",
     "GET_WIRELESS_SENSORS" : "/rsa1/WirelessSensor/instances",
     "GET_WIRELESS_SENSOR_LITE" : "/rsa1/WirelessSensorInfo;dA=",
     "GET_WIRELESS_SENSOR_TEMPERATURE" : "/rsa1/TemperatureInfo;sId=",
     "POST_BLINK_DEVICE" : "/rsa1/WirelessManager/methods/blinkDevice",
     "POST_BUSINESS_INFO" : "/api/v1/fesb/provision",
     "POST_EVE_METER" : "/rsa1/LoadStatus/methods/SetStandbyThreshold",
     "POST_FIRMWARE_UPLOAD" : "/FirmwareUpload",
     "POST_INIT_SYSTEM_UPGRADE" : "/rsa1/Controller/methods/initSystemUpgrade",
     "POST_INSTANCE_MIO_CONTROL" : "/rsa1/Controller/methods/operateMio",
     "POST_INSTANCE_MIO_INPUT" : "/rsa1/MioInput/instances",
     "POST_INSTANCE_MIO_OUTPUT" : "/rsa1/MioOutput/instances",
     "POST_INSTANCE_MPR" : "/rsa1/MprEndpoint/instances",
     "POST_STATUS" : "/rsa1/LoadStatus/methods/GetStatus",
     "PUT_BRANCH_METERS" : "/rsa1/BranchMeters",
     "PUT_INSTANCE_MIO_INPUT" : "/rsa1/MioInput;channel=",
     "PUT_INSTANCE_MIO_OUTPUT" : "/rsa1/MioOutput;channel=",
     "PUT_INSTANCE_MPR" : "/rsa1/MprEndpoint;channel=",
     "PUT_USER_PREPAIRING" : "/rsa1/UserPreparing",
     "PUT_WIRELESS_CHANNEL" : "/rsa1/WirelessManager",
     "PUT_WIRELESS_INPUT" : "/rsa1/MioWirelessInput;slaveId=%d;channel=%d",
     "PUT_WIRELESS_METER" : "/rsa1/WirelessMeter;deviceAddress=",
     "PUT_WIRELESS_OUTPUT" : "/rsa1/MioWirelessOutput;slaveId=%d;channel=%d",
     "PUT_WIRELESS_SENSOR" : "/rsa1/WirelessSensor;deviceAddress=",
     "SEM_IDENTIFICATION" : "/rsa1/SemIdentificationOpt",
     "START_COMISSIONING" : "/rsa1/WirelessManager/methods/startCommissioning",
     "STOP_COMISSIONING" : "/rsa1/WirelessManager/methods/stopCommissioning",
     }