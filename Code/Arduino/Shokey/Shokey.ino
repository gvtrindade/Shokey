/**
 * @file Shokey.ino
 * @author Gabriel Trindade (github.com/gvtrindade)
 * @brief This is the arduino part of the code, 
 * here the button inputs are captured and sent via serial
 * communication to the python part of the code.
 * @version 1.0
 * @date 2021-07-05 
 * 
*/

//Include the libraries that will be used
#include <Keypad.h>
#include <Encoder.h>
#include <Bounce2.h>
#include <Keyboard.h>

//State keys matrix, pins and setup keypad
const byte ROWS = 4;
const byte COLS = 3;
char keys[COLS][ROWS] = {
    {'X', '7', '4', '1'},
    {'*', '8', '5', '2'},
    {'0', '9', '6', '3'}};
byte rowPins[ROWS] = {18, 19, 20, 21};
byte colPins[COLS] = {15, 14, 16};
Keypad keypad = Keypad(makeKeymap(keys), colPins, rowPins, COLS, ROWS);

//Set led pins, led brightness and current selected color
const int redL = 9;
const int greenL = 6;
const int blueL = 5;
const int brightness = 5;
char currColor;

//Set encoder pins, setup encoder and its button, the debounce interval,
// encoder's old position rotation time limit and delay
int SW = 10;
int DT = 2;
int CLK = 3;
Encoder volumeKnob(DT, CLK);
Bounce2::Button encoderButton = Bounce2::Button();
const int debounceInterval = 5;
long oldPosition = -999;
const int rotationDelay = 80;

//Define character to be recieved from the macro script
//and whether or not it's running
char incomingString;
bool scriptRunning = false;

//Function to change shown led color: red, green, blue or white
void changeColor()
{

  switch (currColor)
  {
  case 'W':
    analogWrite(redL, brightness);
    analogWrite(greenL, 0);
    analogWrite(blueL, 0);
    currColor = 'R';
    break;

  case 'R':
    analogWrite(redL, 0);
    analogWrite(greenL, brightness);
    analogWrite(blueL, 0);
    currColor = 'G';
    break;

  case 'G':
    analogWrite(redL, 0);
    analogWrite(greenL, 0);
    analogWrite(blueL, brightness);
    currColor = 'B';
    break;

  case 'B':
    analogWrite(redL, brightness);
    analogWrite(greenL, brightness);
    analogWrite(blueL, brightness);
    currColor = 'W';
    break;
  }
}

// Test communication between keypad and the macro script,
// if the script is on, it returns true, else, false
void testCommunication()
{
  incomingString = Serial.read();
  switch (incomingString)
  {
  case 'I':
    scriptRunning = true;
    break;
  case 'O':
    scriptRunning = false;
    break;
  }
}

void normalKeyPressing(char pressedKey)
{
  //Press key based on assigned key on "keys" matrix
  if (pressedKey != NO_KEY)
  {
    switch (pressedKey)
    {
    case '*':
      changeColor();
      break;
    default:
        Keyboard.press(pressedKey);
        Keyboard.release(pressedKey);
      break;
    }
  }
}

void programKeyPressing(char pressedKey)
{
  //Check if a key is pressed, sending its value to the serial port
  //Depending on the current led color, a different value will be sent,
  //effectively creating a profile for each color.
  //eg. '1R' = number 1 in the red profile
  String keyCode = String(pressedKey) + String(currColor);
  if (pressedKey != NO_KEY)
  {
    switch (pressedKey)
    {
    case '*':
      changeColor();
      break;
    default:
      Serial.println(keyCode);
      break;
    }
  }
}

void encoderButtonPressing()
{
  // Check if the encoder button is pressed, send its value in the same format as the number keys
  if (encoderButton.update() && encoderButton.isPressed())
  {
    String buttonCode = "E" + String(currColor);
    Serial.println(buttonCode);
  }
}

void encoderRotating()
{
  //Check encoder rotation, sending VU when the encoder is rotated clockwise, and VD, when counterclockwise
  long newPosition = volumeKnob.read();
  if (newPosition != oldPosition)
  {
    if ((newPosition - oldPosition) > 0)
    {
      String volumeUpCode = "VU" + String(currColor);
      Serial.println(volumeUpCode);
    }
    else
    {
      String volumeDownCode = "VD" + String(currColor);
      Serial.println(volumeDownCode);
    }
    oldPosition = newPosition;
    delay(rotationDelay);
  }
}

void setup()
{
  //Begin serial communication
  Serial.begin(9600);
  Keyboard.begin();

  //Set led pins, set current color and run changeColor() to set first color as red
  pinMode(redL, OUTPUT);
  pinMode(greenL, OUTPUT);
  pinMode(blueL, OUTPUT);
  currColor = 'W';
  changeColor();

  //Set encoder pins, its pressing interval and pressed state
  pinMode(CLK, INPUT_PULLUP);
  encoderButton.attach(SW, INPUT);
  encoderButton.interval(debounceInterval);
  encoderButton.setPressedState(LOW);
}

void loop()
{
  //Call communication test, key pressing and encoder rotating functions
  testCommunication();
  switch (scriptRunning)
  {
  case true:
    programKeyPressing(keypad.getKey());
    break;
  case false:
    normalKeyPressing(keypad.getKey());
    break;
  }
  encoderButtonPressing();
  encoderRotating();
}
