#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <wiringPi.h>

#include "adc.h"
#include "definitions.h"
#include "init.h"
#include "pot.h"
#include "spi.h"

void blink(uint8_t pins[], uint16_t size){
	for (uint8_t i = 0; i<size; i++){
			printf("Turning on pin %d\n", pins[i]);
			digitalWrite(pins[i],HIGH);
			sleep(1);
			digitalWrite(pins[i],LOW);
	}
}

void allOutput(uint8_t pins[], uint16_t size){
	/* Changes the direction of the pins in pins[] to output */
	for (uint8_t i = 0; i<size; i++){
		pinMode(pins[i],OUTPUT);
	}
}//allOutput

void initBoard(void){
	
	if(wiringPiSetup() > 0)
		exit(EXIT_FAILURE);
	/* Initializes header pins, auxililary chips, and SPI for the drive program	 */
	void initPin(void);		//set direction on header pins
	void initState(void);	//de-select all ICs and clear SPI pins
	void initXPNDR(void);	//configure GPIO expanders
	void initPot(void);		//set potentiometer voltage
}//initBoard

void testPins(void){
	/* Iterates through the list of chip selects, turning each one on for 1 second.
	 * Best used with LEDs attached to the pins
	 */
	printf("Testing Pins\n");
	uint8_t pins[] = {MOSI, MISO, CLK, GPIO1_CS};//, ADC_CS, GPIO2_CS, GPIO3_CS, POT_CS, GPIO4_CS};
	allOutput(pins, 4);																				//Set all pins as outputs
	blink(pins, 4);																					//Turn pins on and off
	printf("Finished test\n");
}//testCS

void blinkBank(uint8_t CS, uint16_t bank){
	uint8_t pin = 0b00000001;
	uint8_t clear = 0;
	printf("Begin the looping\n");
	for (uint8_t j = 0; j<100; j++)
		for (uint8_t i = 0; i<8; i++){
			printf("doing da blinks %d\n", i);
			writeGPIO(CS, bank, pin);
			sleep(1);
			writeGPIO(CS, bank, clear);
			pin = pin << 1;
		}
}

////////////////////////////////////////////////////////////////////////
///////////////////////////// TESTING MAIN /////////////////////////////
////////////////////////////////////////////////////////////////////////
int main(int argc, char** argv){
	printf("\n\n\n\n\nBegin init\n");
	initBoard();							//set pins to the drive.c configuration
	printf("Init finished\n");
	
	//testPins();								//verify the pinout is correct by turning each pin on then off
	
	blinkBank(GPIO1_CS,GPIO_SELECT_PORTB);	//turns each pin on GPIO1 bank B on then off
}//main
