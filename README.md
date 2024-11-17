# Indoor Environment Sensor Device 

## 1. Project Description/Goals

Our team aims to create a Raspberry Pi-based sensor device that monitors
and displays crucial indoor environmental factors, specifically
temperature, oxygen levels, and humidity. This device is intended to
enhance indoor air quality awareness, promote healthier living
environments, and provide easily accessible, real-time data for users.

## 2. Platform of Choice

Our platform of choice is the Raspberry Pi, chosen for its versatility,
compact size, and extensive compatibility with sensors required for
measuring temperature, oxygen levels, and humidity. Using the Raspberry
Pi allows for flexibility and cost-effectiveness in creating a custom
device suited for indoor air quality monitoring.

## 3. Demonstration Plan

The demonstration will involve setting up the Raspberry Pi with sensors
in a controlled environment to capture and display real-time data on
temperature, oxygen levels, and humidity. The demonstration setup will
use a Virtual Private Server (VPS) to insert the data collected. A
laptop will also be used for data visualization and potential debugging
during the demonstration.

## 4. Requirements

Below is how we plan to meet key requirements:

-   Temperature Measurement: We will use a temperature sensor module
    connected to the Raspberry Pi. Data collected will be processed and
    displayed using python scripts.

-   Oxygen Levels: An oxygen sensor module will be added for measuring
    indoor oxygen concentration, which will be integrated into the
    system for real-time data acquisition.

-   Humidity Measurement: A sensor module will also measure humidity,
    allowing us to track multiple environmental factors.

-   Data Visualization: We plan to visualize the data using a website.
    To do so, we will use Nginx as a web server and use HTML to create
    the page.

## 5. Major Technical Solutions Compared

Web Server: We chose Nginx over other web servers like Apache for its
lightweight, high-performance design, which is optimal for the Raspberry
Pi. Nginx uses fewer resources, allowing us to easily handle the
information received by the sensors.

Programming Language: We decided to go with Python scripts for our
project. Due to its simplicity, library support, and simple codes.
Compared to different languages that might offer higher performance, it
would require more complex code scripts, which would increase
development time.

Visualization: We use HTML and JavaScript with Nginx for its simplicity,
responsiveness and because it is easier on the Raspberry PI due to the
lightweight nature of a simple page with HTML.

## 6. Timeline

### Week 1:

Research and procure sensor components, set up the Raspberry Pi, and
test individual sensors (temperature, oxygen, humidity) for data
accuracy.

### Week 2: 

Develop scripts for sensor data acquisition, set up the web page and
integrate sensors into a single program.

### Week 3: 

Finalize the user interface and refine data visualization. Conduct final
testing and prepare for the project presentation.

## 7. Team Composition

The team members for this project consist of

Rafea, Tarek

Abou Chahin, Tarek

Thao, Phoeuk Sothearoum
