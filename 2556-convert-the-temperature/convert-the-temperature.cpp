class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        vector<double>temperature;
        double Kelvin = celsius + 273.15;
        double Fahrenheit = celsius * 1.80 + 32.00;
        temperature.push_back(Kelvin);
        temperature.push_back(Fahrenheit);
        return temperature;



        
    }
};