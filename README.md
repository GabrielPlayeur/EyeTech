# Eye-Tech

Eye-Tech is a project designed to assist visually impaired or blind runners in navigating the lanes of a track independently. Using a Raspberry Pi, a camera, and vibrating motors attached to a harness, Eye-Tech detects track lines and provides directional feedback to the runner through vibrations.

## Project Overview
Eye-Tech aims to make sports more accessible to everyone, particularly by helping blind or partially sighted individuals run independently. By detecting the lines of an athletic track, the system provides directional cues through vibrations, guiding the runner to stay within their lane.

## Motivation
The motivation behind Eye-Tech is to bridge the gap in accessibility for visually impaired athletes. Currently, there are no market solutions that allow blind people to run independently without external assistance. Eye-Tech fills this void by providing real-time guidance during running.

## Key Features
- **Line Detection**: Uses image processing to detect the track lines.
- **Vibration Feedback**: Provides haptic feedback to the runner to keep them on course.
- **Hands-Free Control**: Start, stop, and shut down the system using simple hand gestures in front of the camera.

## Target Audience
Eye-Tech is designed for blind or partially sighted individuals and running associations that can equip their members with this technology.

## Setup Instructions
### Prerequisites
To recreate the Eye-Tech prototype, you will need:
- Raspberry Pi 3
- Raspberry Pi Camera
- Two vibrating motors
- A harness to mount the equipment

### Installation
1. Clone the Eye-Tech repository to your Raspberry Pi.

```bash
git clone https://github.com/GabrielPlayer/Eye-Tech.git
cd Eye-Tech
```

2. Install dependencies using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

3. Install the picamera2 library directly on the Raspberry Pi.

```bash
pip install python3-picamera2
```

### Configuration
There are no additional configuration steps required before running the project.

### Dependencies
Ensure you have the following dependencies installed, as specified in requirements.txt:

- OpenCV
- Numpy
- Other Python libraries listed in the file

## Usage
### Running the Project
To start the project, navigate to the production directory and run the main script:

```bash
cd ./production
python ./main.py
```

### User Instructions
- **Starting Line Detection**: Place your hand in front of the camera to cover it. You will feel a vibration indicating the line detection has started.
- **Stopping Line Detection**: Repeat the gesture to stop the line detection.
- **Shutting Down**: To shut down the system, leave your hand in front of the camera for 5 seconds. You will feel a different vibration indicating the shutdown process.

### Example Scenario
1. **Setup**: Plug the Raspberry Pi into a battery pack. You will feel a vibration once the system is ready.
2. **Starting the Session**: Cover the camera with your hand to initiate line detection.
3. **Taking a Break**: Cover the camera to pause the line detection.
4. **Ending the Session**: To safely power off, cover the camera for 5 seconds to shut down the Raspberry Pi before unplugging it.

## Technical Details
### Code Structure
The project is organized into five folders, each representing different aspects of the project, managed by different teams. The folder names are indicative of their functionality:

- **`camera`**: Code related to camera operations.
- **`detection`**: Line detection algorithms and image processing.
- **`control`**: Feedback control mechanisms for the motors.
- **`integration`**: Integration scripts that combine various components.
- **`utilities`**: Helper functions and utility scripts.

### Algorithms and Techniques
Eye-Tech uses OpenCV for image processing and Hough Transform for detecting lines on the track. These techniques are implemented to ensure robust line detection under various lighting and track conditions.

### Performance
The system's reaction time is adequate for practical use, although we have not conducted detailed performance evaluations.

## Contributions and Development
### Contributing
We welcome contributions from the community. Please refer to the CONTRIBUTING.md file for guidelines on how to contribute, submit issues, or create pull requests.

### Development Setup
This project was developed as part of a second engineering degree over a period of five months. To set up a development environment:

1. Follow the installation instructions to set up the project.
2. Use a development branch for making changes and submit pull requests for review.

## Additional Information
### License
This project is licensed under the MIT License. See the LICENSE file for more details.

### Acknowledgements
We would like to express our gratitude to:

- **Mr Hassan Chamas** for his guidance and support throughout this project.
- The **"A perte de vue" association** for their invaluable time and insights.
- **Polytech Nantes* for funding the project.
- The **Commune of Nantes** for providing access to their running track.

### Future Plans
We plan to continue developing Eye-Tech to improve its performance and enhance the overall product as part of our ongoing engineering studies.

### Contact Information
For inquiries or support, please email us. We strive to respond as quickly as possible.
