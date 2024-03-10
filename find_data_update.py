import os
import pyulog


def load_ulogs_2_dicts(desired_channels):
    """Processes ULog files in the current directory, extracts data, and stores it in dictionaries.

    Args:
        desired_channels (list): List of channel names to extract data from.

    Returns:
        list: A list of dictionaries, where each dictionary represents a flight and
              contains data from the specified channels.
     """

    list_flight_dicts = []

    for filename in os.listdir('.'):  # Use '.' for current directory
        if filename.lower().endswith(".ulg"):
            try:
                ulog_data = pyulog.ULog(filename)  # open and parses .ulg files
                flight_dict = {}

                for dataset_name in desired_channels:
                    try:
                        flight_dict[dataset_name] = ulog_data.get_dataset(
                            dataset_name)  # extract data from the desired channel and stores it as a dict

                    except KeyError:
                        print(
                            f"WARNING: Channel '{dataset_name}' not found in ULog file '{filename}'.")
                list_flight_dicts.append(flight_dict)
            except FileNotFoundError:
                print(f"Error: ULog file not found: {filename}")

    return list_flight_dicts


# Example usage

desired_channels = ["vehicle_imu", "actuator_outputs", "ekf_gps_position"]
flight_data = load_ulogs_2_dicts(desired_channels)


normal_flight = flight_data[0]
for flight in flight_data:
    if flight == normal_flight:
        print(f"{flight} is a normal flight")
    else:
        print(f"{flight} is NOT a normal flight")
