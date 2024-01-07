# Traffic Light

Rasperry Pi / 4 channel relay / LED Traffic Light / HTML

![alt text](https://github.com/ykSneerG/TrafficLight/blob/main/docs/UI_iphone.PNG "Screenshot iphone App")

![alt text](https://github.com/ykSneerG/TrafficLight/blob/main/docs/IMG_2868.jpg "Photo Setup")

This application uses Python flask and the GPIOs of the Rasperry Pi. The following items must be installed if this is not already the case.

```python
pip install flask
pip install RPi.GPIO
```

The channel setup is defined in the "app.py" by the signals array. A signal is instantiated for each channel of the relay.
The signal class requires the following parameters:
* GPIO pin (for control)
* Name (this is the name of the button in the HTML view)
* Color (the color of the button in the HTML view)
Since I am controlling a traffic light, I have used the colors and names for the corresponding traffic light colors in my example.

```python
signals = [
    Signal(21, "red", "#ff0000"),
    Signal(12, "orange", "#ffa500"),
    Signal(16, "green", "#008000")
]
```

