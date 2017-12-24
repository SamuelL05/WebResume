#include<wiringPi.h>
#include<stdio.h>
#include<softTone.h>
#include<time.h>

#define armPin 5 // RPi Pin layout 29
#define alarmPin 6 // RPi Pin layout 31
#define soundPin 13 // RPi Pin layout 33
#define alarmLED 19 // RPi Pin layout 35

int systemSetup();
void systemStatus(int);
void systemArm(int);
void systemAlert(int);

int main() {

	// Main system code
	const int systemCode = 1994;
	int result = systemSetup();

	if (result == -1)
		return 0;

	systemStatus(systemCode);
}

int systemSetup() {

	// Set up PIN modes. Call function once for
	// each new program run. Otherwise Raspberry Pi
	// will not activate GPIO pins. Hardware will not
	// respond to program ques.

	/************************************************
	Broadcom wiring scheme required for the use of
	input pins. Please follow BCM Layout.
	************************************************/

	if (wiringPiSetupGpio() == -1) {
		printf("WiringPi setup failed!\n");
		return -1;
	}
	else if (softToneCreate(soundPin) == -1) {
		printf("SoftTone Create failed!\n");
		return -1;
	}
	else {
		// Setting up PIN modes
		pinMode(armPin, OUTPUT);
		digitalWrite(armPin, LOW); // OFF (HIGH = ON)
		pinMode(alarmLED, OUTPUT);
		digitalWrite(alarmLED, LOW); // LOW = OFF or 1
		softToneWrite(soundPin, 0);
		pinMode(alarmPin, INPUT);
		pullUpDnControl(alarmPin, PUD_DOWN); // Required for Input PINs
	}
}

void systemStatus(int systemCode) {

	/**********************************************
	systemStatus function used recursively to avoid
	calling wiringPiSetup multiple times.
	**********************************************/ 

	// Acquire input from user to activate system.
	// User must enter a 1 to arm system. Program
	// Will loop until a 1 is given. 

	/*******************************************
	Do not enter data types other then integers.
	If you do CTRL+C to end infinite loop.
	*******************************************/

	digitalWrite(armPin, LOW);
	printf("Arm system? (1 = yes, CTRL+C = Exit): ");
	int state = 0;
	scanf("%d", &state);

	while (state != 1) {
		printf("Re-Enter: ");	
		scanf("%i", &state);
		delay(100); // To avoid spamming procressor
		// If user enters a non int value.
	}
	printf("System Arming in...\n");

	for (int count = 5; count > 0; count --) {
		printf("%d\n", count);
		delay(1000);
	}
	systemArm(systemCode);			
}

void systemArm(int systemCode) {

	// System alarm activation. Circuit is energized.
	// If circuit is broken systemAlert function will
	// be called to activate defense pins. 

	/*************************************************
	Once in this state the only way to deactivate the
	system is to close the current program, and re open
	**************************************************/
	
	digitalWrite(armPin, HIGH);
	int complete = 0;	// Circuit Complete = 0
	printf("System On...\n");

	while (complete != 2) { // Junk value for infinite loop
		delay(500); // .5 second
		complete = digitalRead(alarmPin); // Check circuit status
		if (complete != 0) 
			systemAlert(systemCode);
		else
			;
	}
}

void systemAlert(int systemCode) {

	// Security system has been tripped. All GPIO
	// Pins that have been wired for defense systems
	// are activated. 

	/************************************************
	System will remain active until the correct code
	is entered. Defense systems will stay active even
	after program termination.
	************************************************/ 

	time_t curTime;
	curTime = time(NULL);
	int code = 0;
	delay(500);

	softToneWrite(soundPin, 1000);
	digitalWrite(alarmLED, HIGH);

	printf("Intruder Alert.\n");
	printf("Event Time: ");
	printf(ctime(&curTime));
	printf("Enter System Code: ");
	scanf("%d", &code);

	while (code != systemCode) {
		printf("Re-Enter Code: ");
		scanf("%d", &code);
		delay(100);
	}
	softToneWrite(soundPin, 0);
	digitalWrite(alarmLED, LOW);
	systemStatus(systemCode);
}




	

