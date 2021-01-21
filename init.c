/**
 * INIT_C
 * @author K Gledson
 * @version 2021-01-21
 * Functions needed to initialize the Raspberry Pi header, auxiliary board ICs and SPI communication
 */

///////////////////////////////////////////////////////////////////////////////////////// included files (get rid of these later)
#include "stdint.h" 		//library not found on my computer.
#include "definitions.h"
///////////////////////////////////////////////////////////////////////////////////////// functions
 void initPin(void){
    //Sets direction of header pins

	 	 	 	 	 	 	 	//SPI pins
	pinmode(MOSI,OUTPUT);       //Data output pin
    pinmode(MISO,INPUT);        //Data input pin
    pinmode(CLK,OUTPUT);        //SPI clock

    							//Auxiliary board ICs
    pinmode(GPIO1_CS, OUTPUT);  //GPIO expander 1 chip select
    pinmode(GPIO2_CS, OUTPUT);  //GPIO expander 2 chip select
    pinmode(GPIO3_CS, OUTPUT);  //GPIO expander 3 chip select
    pinmode(GPIO4_CS, OUTPUT);  //GPIO expander 4 chip select
    pinmode(ADC_CS, OUTPUT);    //Analog to digital (ADC) converter chip select
    pinmode(POT_CS, OUTPUT);    //Digital potentiometer chip select

}//initPin

void initState(void){
    //Sets the header pins to their initial states (high or low)
    								//Deselect all ICs
    digitalWrite(GPIO1_CS, HIGH);
    digitalWrite(GPIO2_CS, HIGH);
    digitalWrite(GPIO3_CS, HIGH);
    digitalWrite(GPIO4_CS, HIGH);
    digitalWrite(ADC_CS, HIGH);
    digitalWrite(POT_CS, HIGH);
    								//SPI initial states
    digitalWrite(CLK, LOW);
    digitalWrite(MOSI, LOW);
}//initState

void initXPNDR(void){
    //Sets the direction for all ICs on the expansion board
    initPin();
    initState();
    initGPIO(GPIO1_CS);
    initGPIO(GPIO2_CS);
    initGPIO(GPIO3_CS);
    initGPIO(GPIO4_CS);
}//initXPNDR

void initPot(void){
    //Initializes the potentiometer that controls the gain of the operational amplifier
    uint8_t value = 1;
    writePot(value);
}//initPot



