import numpy as np
import netCDF4


def get_wrf_field(file_name, file_format, data_field):

    """
    Reads a field from a WRF output file.
    :param file_name: name of file to be read
    :param file_format: netCDF format of file. Can be 'CLASSIC' for version 3 or 'NETCDF4' for version 3
    :param data_field: string that specifies key of the variable to be read from the file.
    :return: either returns the data if the key is valid, or False if there is a key error
    """
    data_file = netCDF4.Dataset(file_name, mode='r', format=file_format)

    try:

        data = np.squeeze(data_file.variables[data_field][:])
        data_file.close()

        return data

    except KeyError:

        data_file.close()
        return False


def get_file_attribute(file_name, file_format, attribute):

    data_file = netCDF4.Dataset(file_name, mode='r', format=file_format)

    return data_file.attribute


def convert_theta_to_temperature(data_theta, data_p, data_pb):

    """
    Converts the potential temperature to temperature (in Kelvin). Uses the standard formula for potential temperature.
    :param data_theta: perturbation potential temperature data. 300K is base state theta in WRF (Kelvin)
    :param data_p: base state pressure (Pascals)
    :param data_pb: perturbation pressure (Pascals)
    :return: returns converted temperature (Kelvin)
    """
    p_0 = 105000.  # reference pressure
    kappa = 0.286  # R/c_p

    temp_converted = (data_theta + 300.)*np.power((data_p + data_pb)/p_0, kappa)

    return temp_converted


def convert_kelvin_to_fahrenheit(kelvin_temp):

    """
    Converts Kelvin to Fahrenheit
    :param kelvin_temp: temperature in Kelvin (may be a numpy array or a single value)
    :return: converted temperature in degrees Fahrenheit
    """
    fahrenheit_temp = 1.8 * (kelvin_temp - 273.15) + 32.

    return fahrenheit_temp


def convert_kelvin_to_celsius(kelvin_temp):

    """
    Converts Kelvin to Celsius
    :param kelvin_temp: temperature in Kelvin (may be a numpy array or single value)
    :return: converted temperature in degrees Celsius
    """
    celsius_temp = kelvin_temp - 273.15

    return celsius_temp







