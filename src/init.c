/**
 * INIT_C
 * @author K Gledson
 * @version 2021-01-21
 * Functions needed to initialize the Raspberry Pi header, auxiliary board ICs and SPI communication
 */

#include "init.h"

 void initPin(void){
    //Sets direction of header pins

	 	 	 	 	 	 	 	//SPI pins
	pinMode(MOSI,OUTPUT);       //Data output pin
    pinMode(MISO,INPUT);        //Data input pin
    pinMode(CLK,OUTPUT);        //SPI clock

    							//Auxiliary board ICs
    pinMode(GPIO1_CS, OUTPUT);  //GPIO expander 1 chip select
    pinMode(GPIO2_CS, OUTPUT);  //GPIO expander 2 chip select
    pinMode(GPIO3_CS, OUTPUT);  //GPIO expander 3 chip select
    pinMode(GPIO4_CS, OUTPUT);  //GPIO expander 4 chip select
    pinMode(ADC_CS, OUTPUT);    //Analog to digital (ADC) converter chip select
    pinMode(POT_CS, OUTPUT);    //Digital potentiometer chip select

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
    initGPIO();
}//initXPNDR

void initPot(void){
    //Initializes the potentiometer that controls the gain of the operational amplifier
    uint8_t value = 1;
    writePot(value);
}//initPot



