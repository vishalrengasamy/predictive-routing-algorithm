# predictive-routing-algorithm
A routing algorithm that uses the data from an ultrasonic sensor, placed on dustbins across different coordinates, and based on a predictive formula, determines if a dustbin (represented by a coordinate) needs to be emptied the following day, and also returns the optimal route through all the dustbins, starting from the depot.



The CSV files, 'data1.csv' and 'data2.csv' are two example datasets, that contain random future values of sensor data with the following assumptions:
-> The depot (starting point of the garbage collection truck) is always assumed to be at coordinate (0, 0). This can be changed in code     without loss of generality.
-> Only 10 coordinates are randomly generated each time the script is run. This is to match the synthetic data generated.
-> Data exists for a 7-day window. 

These values are manipulated so as to allow the script to reset the internal sum. 
In a practical implementation however, with small modifications to the script, the data can be taken as an input continuously, on a daily basis, and the resulting route (if it exists) can be generated.



Note: The data used is synthetic as the Python script currently does not actually connect to a network that pulls in sensor data.
