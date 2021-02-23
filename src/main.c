#include <wiringPi.h>
//#include <stdio.h>
#include <stdint.h>
#include "definitions.h"
#include "init.h"
#include "spi.h"
#include "adc.h"
#include "pot.h"

void main(void){
	testPins();								//verify the pinout is correct by turning each pin on then off
	initBoard();							//set pins to the drive.c configuration
	blinkBank(GPIO1_CS,GPIO_SELECT_PORTB);	//turns each pin on GPIO1 bank B on then off
}//main

void initBoard(void){
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
	uint8_t pins[] = {MOSI, MISO, CLK, ADC_CS, GPIO2_CS, GPIO3_CS, POT_CS, GPIO1_CS, GPIO4_CS};
	allOutput(pins);																				//Set all pins as outputs
	blink(pins);																					//Turn pins on and off
}//testCS

void blink(uint8_t pins[]){
	uint8_t size = sizeof(pins)/sizeof(pins[0]);
	for (uint8_t i = 0; i<size; i++){
			digitalWrite(pins[i],HIGH);
			sleep(1);
			digitalWrite(pins[i],LOW);
	}
}

void allOutput(uint8_t pins[]){
	/* Changes the direction of the pins in pins[] to output */
	uint8_t size = sizeof(pins)/sizeof(pins[0]);
	for (uint8_t i = 0; i<size; i++){
		pinmode(pins[i],OUTPUT);
	}
}//allOutput

void blinkBank(uint8_t CS, uint16_t bank){
	uint8_t pin = 0b00000001;
	uint8_t clear = 0;
	for (uint8_t i = 0; i<8; i++){
		writeGPIO(CS, bank, pin);
		sleep(1);
		writeGPIO(CS, bank, clear);
		pin = pin << 1;
	}
}
